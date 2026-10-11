/**
 * SplitMate - Tinder Bill Split App
 * Interactive Tinder swipe card deck with realistic physics,
 * sound effects, WhatsApp settlement generator, and fast list view.
 */

// State Object
const state = {
  items: [...PRODUCTS_DATA], // All 61 products
  activeFilter: 'all',       // 'all' | 'rami_levy' | 'max_stock'
  currentIndex: 0,          // Index in the filtered deck
  decisions: {},            // { [itemId]: 'half' | 'pass' | 'full' }
  history: [],              // Stack for undo: [{ itemId, prevDecision }]
  isListView: false,
  soundEnabled: true
};

// Web Audio API Sound Synthesizer (Zero external dependencies)
class SoundFX {
  constructor() {
    this.ctx = null;
  }

  init() {
    if (!this.ctx && (window.AudioContext || window.webkitAudioContext)) {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      this.ctx = new AudioCtx();
    }
    if (this.ctx && this.ctx.state === 'suspended') {
      this.ctx.resume();
    }
  }

  playShare() {
    this.init();
    if (!this.ctx) return;
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'sine';
    const now = this.ctx.currentTime;
    osc.frequency.setValueAtTime(440, now);
    osc.frequency.exponentialRampToValueAtTime(880, now + 0.12);
    gain.gain.setValueAtTime(0.15, now);
    gain.gain.exponentialRampToValueAtTime(0.01, now + 0.12);
    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start(now);
    osc.stop(now + 0.12);
  }

  playPass() {
    this.init();
    if (!this.ctx) return;
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'triangle';
    const now = this.ctx.currentTime;
    osc.frequency.setValueAtTime(320, now);
    osc.frequency.exponentialRampToValueAtTime(160, now + 0.12);
    gain.gain.setValueAtTime(0.15, now);
    gain.gain.exponentialRampToValueAtTime(0.01, now + 0.12);
    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start(now);
    osc.stop(now + 0.12);
  }

  playFull() {
    this.init();
    if (!this.ctx) return;
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'sine';
    const now = this.ctx.currentTime;
    osc.frequency.setValueAtTime(523.25, now);
    osc.frequency.setValueAtTime(659.25, now + 0.08);
    osc.frequency.setValueAtTime(783.99, now + 0.16);
    gain.gain.setValueAtTime(0.15, now);
    gain.gain.exponentialRampToValueAtTime(0.01, now + 0.24);
    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start(now);
    osc.stop(now + 0.24);
  }

  playUndo() {
    this.init();
    if (!this.ctx) return;
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'sine';
    const now = this.ctx.currentTime;
    osc.frequency.setValueAtTime(300, now);
    osc.frequency.linearRampToValueAtTime(500, now + 0.08);
    gain.gain.setValueAtTime(0.12, now);
    gain.gain.linearRampToValueAtTime(0.01, now + 0.08);
    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start(now);
    osc.stop(now + 0.08);
  }
}
const sfx = new SoundFX();

// DOM Elements
const cardDeck = document.getElementById('card-deck');
const liveShareAmount = document.getElementById('live-share-amount');
const progressText = document.getElementById('progress-text');
const progressPercent = document.getElementById('progress-percentage');
const progressBarFill = document.getElementById('progress-bar-fill');
const tinderView = document.getElementById('tinder-view');
const listView = document.getElementById('list-view');
const listItemsContainer = document.getElementById('list-items-container');
const listSearchInput = document.getElementById('list-search-input');
const btnToggleMode = document.getElementById('btn-toggle-mode');
const modeIcon = document.getElementById('mode-icon');
const modeText = document.getElementById('mode-text');
const summaryModal = document.getElementById('summary-modal');
const toastMsg = document.getElementById('toast-msg');

// Action Buttons
const btnUndo = document.getElementById('btn-undo');
const btnPass = document.getElementById('btn-pass');
const btnShare = document.getElementById('btn-share');
const btnFull = document.getElementById('btn-full');
const btnOpenSummary = document.getElementById('btn-open-summary');
const btnCloseSummary = document.getElementById('btn-close-summary');
const btnViewSummaryFromList = document.getElementById('btn-view-summary-from-list');
const btnSendWhatsapp = document.getElementById('btn-send-whatsapp');
const btnCopySummary = document.getElementById('btn-copy-summary');
const btnRestartApp = document.getElementById('btn-restart-app');

// LocalStorage Persistence
function loadStoredState() {
  try {
    const raw = localStorage.getItem('splitmate_roommate_decisions');
    if (raw) {
      const parsed = JSON.parse(raw);
      state.decisions = parsed.decisions || {};
      state.history = parsed.history || [];
      state.currentIndex = parsed.currentIndex || 0;
    }
  } catch (e) {
    console.warn('Could not read from localStorage', e);
  }
}

function saveStoredState() {
  try {
    localStorage.setItem('splitmate_roommate_decisions', JSON.stringify({
      decisions: state.decisions,
      history: state.history,
      currentIndex: state.currentIndex
    }));
  } catch (e) {
    console.warn('Could not save to localStorage', e);
  }
}

// Get Items currently filtered
function getFilteredItems() {
  if (state.activeFilter === 'all') return state.items;
  return state.items.filter(it => it.storeKey === state.activeFilter);
}

// Compute Totals
function computeTotals() {
  let partnerOwes = 0;
  let itemsApproved = 0;
  const filtered = getFilteredItems();

  filtered.forEach(it => {
    const dec = state.decisions[it.id];
    if (dec === 'half') {
      partnerOwes += (it.price / 2);
      itemsApproved++;
    } else if (dec === 'full') {
      partnerOwes += it.price;
      itemsApproved++;
    }
  });

  const totalFilteredSpent = filtered.reduce((acc, it) => acc + it.price, 0);
  const myShare = totalFilteredSpent - partnerOwes;

  return {
    partnerOwes: Math.round(partnerOwes * 100) / 100,
    myShare: Math.round(myShare * 100) / 100,
    itemsApproved,
    totalCount: filtered.length,
    totalSpent: Math.round(totalFilteredSpent * 100) / 100
  };
}

// Update Top Live Header & Progress
function updateLiveDisplay() {
  const totals = computeTotals();
  liveShareAmount.textContent = `${totals.partnerOwes.toFixed(2)} ₪`;

  const filtered = getFilteredItems();
  const total = filtered.length;
  const current = Math.min(state.currentIndex + 1, total);

  // Count decided in this filter
  let decidedCount = 0;
  filtered.forEach(it => {
    if (state.decisions[it.id]) decidedCount++;
  });

  const pct = total > 0 ? Math.round((decidedCount / total) * 100) : 0;
  progressText.textContent = `מוצר ${current} מתוך ${total}`;
  progressPercent.textContent = `${pct}% הושלם (${decidedCount}/${total})`;
  progressBarFill.style.width = `${pct}%`;

  // Enable/disable undo
  btnUndo.style.opacity = state.history.length > 0 ? '1' : '0.4';
  btnUndo.style.pointerEvents = state.history.length > 0 ? 'auto' : 'none';
}

// Render the Tinder Card Stack
function renderDeck() {
  cardDeck.innerHTML = '';
  const filtered = getFilteredItems();

  if (state.currentIndex >= filtered.length) {
    // Deck complete!
    cardDeck.innerHTML = `
      <div class="tinder-card card-active" style="display: flex; align-items: center; justify-content: center; text-align: center; padding: 30px; background: rgba(30, 41, 59, 0.95);">
        <div style="font-size: 58px; margin-bottom: 12px;">🎉</div>
        <h2 style="font-size: 22px; font-weight: 800; margin-bottom: 8px;">סיימת את כל המוצרים!</h2>
        <p style="color: var(--text-muted); font-size: 14px; margin-bottom: 24px;">כל הכבוד, עברת על כל הקבלות בהצלחה.</p>
        <button class="btn-cta whatsapp" style="width: 100%; max-width: 260px;" onclick="openSummaryModal()">
          <span>📊</span>
          <span>צפה בסיכום הסופי</span>
        </button>
      </div>
    `;
    return;
  }

  // Render up to 3 cards in stack for 3D depth
  const maxStack = Math.min(3, filtered.length - state.currentIndex);
  for (let i = maxStack - 1; i >= 0; i--) {
    const itemIndex = state.currentIndex + i;
    const item = filtered[itemIndex];
    const cardEl = createCardElement(item, i);
    cardDeck.appendChild(cardEl);

    if (i === 0) {
      attachCardInteractions(cardEl, item);
    }
  }
}

// Create Card DOM Element
function createCardElement(item, stackLayer) {
  const card = document.createElement('article');
  card.className = `tinder-card ${stackLayer === 0 ? 'card-active' : (stackLayer === 1 ? 'card-next-1' : 'card-next-2')}`;
  card.id = `card-${item.id}`;

  const storeClass = item.storeKey === 'rami_levy' ? 'rami-levy' : 'max-stock';
  const halfPrice = (item.price / 2).toFixed(2);
  const totalFormatted = item.price.toFixed(2);

  card.innerHTML = `
    <!-- Stamps -->
    <div class="card-stamp stamp-share" id="stamp-share-${item.id}">💚 משתתף חצי</div>
    <div class="card-stamp stamp-pass" id="stamp-pass-${item.id}">❌ לא משתתף</div>
    <div class="card-stamp stamp-full" id="stamp-full-${item.id}">👑 משלם מלא</div>

    <!-- Product Image Box -->
    <div class="card-image-box">
      <img src="${item.image}" alt="${item.name}" class="card-img" loading="eager" onerror="this.onerror=null; this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%2250%22 font-size=%2240%22>📦</text></svg>';">
      
      <!-- Badges -->
      <div class="store-tag ${storeClass}">
        <span>${item.store === 'רמי לוי' ? '🛒' : '🏬'}</span>
        <span>${item.store}</span>
      </div>
      <div class="category-tag">${item.category}</div>
    </div>

    <!-- Details Box -->
    <div class="card-details">
      <div class="card-header-info">
        <h2 class="card-product-name">${item.name}</h2>
        ${item.details ? `<div class="card-product-details"><span>🏷️</span> ${item.details}</div>` : ''}
        <div class="card-barcode-note">ברקוד: ${item.barcode}</div>
      </div>

      <!-- Price Box -->
      <div class="card-price-grid">
        <div class="price-item">
          <span class="price-label">מחיר בקבלה</span>
          <span class="price-value-total">${totalFormatted} ₪</span>
        </div>
        <div class="price-item highlight">
          <span class="price-label">חלקך בחצי (50%)</span>
          <span class="price-value-half">${halfPrice} ₪</span>
          <span class="price-sub">החלקה ימינה</span>
        </div>
      </div>
    </div>
  `;

  return card;
}

// Drag & Touch Gesture Physics for Top Active Card
function attachCardInteractions(card, item) {
  let isDragging = false;
  let startX = 0;
  let startY = 0;
  let currentX = 0;
  let currentY = 0;

  const stampShare = card.querySelector(`#stamp-share-${item.id}`);
  const stampPass = card.querySelector(`#stamp-pass-${item.id}`);
  const stampFull = card.querySelector(`#stamp-full-${item.id}`);

  function onPointerDown(e) {
    if (e.target.closest('button')) return;
    isDragging = true;
    startX = e.clientX || (e.touches && e.touches[0].clientX);
    startY = e.clientY || (e.touches && e.touches[0].clientY);
    card.style.transition = 'none';
  }

  function onPointerMove(e) {
    if (!isDragging) return;
    const clientX = e.clientX || (e.touches && e.touches[0].clientX);
    const clientY = e.clientY || (e.touches && e.touches[0].clientY);
    currentX = clientX - startX;
    currentY = clientY - startY;

    const rotate = currentX * 0.08;
    card.style.transform = `translate(${currentX}px, ${currentY}px) rotate(${rotate}deg)`;

    // Update Stamps Opacity
    if (currentX > 25) {
      // Swiping Right -> Share Half
      stampShare.style.opacity = Math.min(1, (currentX - 25) / 80);
      stampShare.style.transform = `rotate(14deg) scale(${0.8 + Math.min(0.3, currentX / 300)})`;
      stampPass.style.opacity = 0;
      stampFull.style.opacity = 0;
    } else if (currentX < -25) {
      // Swiping Left -> Pass
      stampPass.style.opacity = Math.min(1, (-currentX - 25) / 80);
      stampPass.style.transform = `rotate(-14deg) scale(${0.8 + Math.min(0.3, -currentX / 300)})`;
      stampShare.style.opacity = 0;
      stampFull.style.opacity = 0;
    } else if (currentY < -40 && Math.abs(currentX) < 50) {
      // Swiping Up -> Full 100%
      stampFull.style.opacity = Math.min(1, (-currentY - 40) / 70);
      stampShare.style.opacity = 0;
      stampPass.style.opacity = 0;
    } else {
      stampShare.style.opacity = 0;
      stampPass.style.opacity = 0;
      stampFull.style.opacity = 0;
    }
  }

  function onPointerUp() {
    if (!isDragging) return;
    isDragging = false;
    card.style.transition = 'transform 0.35s cubic-bezier(0.18, 0.89, 0.32, 1.28), opacity 0.3s ease';

    const threshold = 90;
    if (currentX > threshold) {
      // Confirmed Right Swipe (50% Share)
      triggerCardDecision(card, item, 'half');
    } else if (currentX < -threshold) {
      // Confirmed Left Swipe (Pass)
      triggerCardDecision(card, item, 'pass');
    } else if (currentY < -threshold && Math.abs(currentX) < 70) {
      // Confirmed Up Swipe (100% Full)
      triggerCardDecision(card, item, 'full');
    } else {
      // Snap back to initial center
      card.style.transform = 'translate(0px, 0px) rotate(0deg)';
      stampShare.style.opacity = 0;
      stampPass.style.opacity = 0;
      stampFull.style.opacity = 0;
    }
  }

  // Mouse Listeners
  card.addEventListener('mousedown', onPointerDown);
  window.addEventListener('mousemove', onPointerMove);
  window.addEventListener('mouseup', onPointerUp);

  // Touch Listeners
  card.addEventListener('touchstart', onPointerDown, { passive: true });
  window.addEventListener('touchmove', onPointerMove, { passive: true });
  window.addEventListener('touchend', onPointerUp);
}

// Trigger Decision with realistic exit animation
function triggerCardDecision(card, item, decision) {
  const prevDecision = state.decisions[item.id] || null;
  state.decisions[item.id] = decision;
  state.history.push({ itemId: item.id, prevDecision, itemIndex: state.currentIndex });
  saveStoredState();

  // Play Sound Effect
  if (decision === 'half') sfx.playShare();
  else if (decision === 'pass') sfx.playPass();
  else if (decision === 'full') sfx.playFull();

  // Fly off animation
  card.style.transition = 'transform 0.4s ease-out, opacity 0.35s ease';
  if (decision === 'half') {
    card.style.transform = 'translate(600px, 40px) rotate(35deg)';
  } else if (decision === 'pass') {
    card.style.transform = 'translate(-600px, 40px) rotate(-35deg)';
  } else if (decision === 'full') {
    card.style.transform = 'translate(0px, -600px) rotate(0deg)';
  }
  card.style.opacity = '0';

  setTimeout(() => {
    state.currentIndex++;
    renderDeck();
    updateLiveDisplay();
    renderListView();

    // If completed all cards, open summary modal with confetti!
    const filtered = getFilteredItems();
    if (state.currentIndex >= filtered.length) {
      setTimeout(openSummaryModal, 300);
    }
  }, 260);
}

// Undo Last Swipe
function handleUndo() {
  if (state.history.length === 0) return;
  const last = state.history.pop();
  if (last.prevDecision) {
    state.decisions[last.itemId] = last.prevDecision;
  } else {
    delete state.decisions[last.itemId];
  }

  if (state.currentIndex > 0) {
    state.currentIndex--;
  }

  sfx.playUndo();
  saveStoredState();
  renderDeck();
  updateLiveDisplay();
  renderListView();
  showToast('הפעולה בוטלה');
}

// Render Fast List View
function renderListView() {
  const query = (listSearchInput.value || '').trim().toLowerCase();
  const filtered = getFilteredItems();

  const matched = filtered.filter(it => {
    if (!query) return true;
    return it.name.toLowerCase().includes(query) ||
           it.barcode.includes(query) ||
           it.category.includes(query) ||
           (it.details && it.details.toLowerCase().includes(query));
  });

  listItemsContainer.innerHTML = '';
  if (matched.length === 0) {
    listItemsContainer.innerHTML = `
      <div style="text-align: center; color: var(--text-dim); padding: 30px;">
        לא נמצאו מוצרים התואמים את החיפוש
      </div>
    `;
    return;
  }

  matched.forEach(it => {
    const dec = state.decisions[it.id];
    const itemCard = document.createElement('div');
    itemCard.className = 'list-item-card';

    itemCard.innerHTML = `
      <img src="${it.image}" alt="${it.name}" class="list-item-thumb" onerror="this.onerror=null; this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%2250%22 font-size=%2240%22>📦</text></svg>';">
      
      <div class="list-item-info">
        <div class="list-item-title">${it.name}</div>
        <div class="list-item-meta">
          <span>${it.store}</span>
          <span>•</span>
          <span style="color: #fff; font-weight: 700;">${it.price.toFixed(2)} ₪</span>
          <span>•</span>
          <span style="color: #34d399;">חצי: ${(it.price / 2).toFixed(2)} ₪</span>
        </div>
      </div>

      <div class="list-item-actions">
        <button class="btn-list-opt ${dec === 'pass' ? 'active-pass' : ''}" data-id="${it.id}" data-action="pass" title="לא משתתף">❌</button>
        <button class="btn-list-opt ${dec === 'half' ? 'active-half' : ''}" data-id="${it.id}" data-action="half" title="משתתף חצי">🤝 50%</button>
        <button class="btn-list-opt ${dec === 'full' ? 'active-full' : ''}" data-id="${it.id}" data-action="full" title="מלא">👑 100%</button>
      </div>
    `;

    // Button event listeners
    const actionBtns = itemCard.querySelectorAll('.btn-list-opt');
    actionBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const action = btn.dataset.action;
        const itemId = btn.dataset.id;
        state.decisions[itemId] = action;
        saveStoredState();
        updateLiveDisplay();
        renderListView();
      });
    });

    listItemsContainer.appendChild(itemCard);
  });
}

// Open Summary Modal & Launch Confetti
function openSummaryModal() {
  const totals = computeTotals();
  document.getElementById('summary-partner-owes').textContent = `${totals.partnerOwes.toFixed(2)} ₪`;
  document.getElementById('summary-total-spent').textContent = `${totals.totalSpent.toFixed(2)} ₪`;
  document.getElementById('summary-my-share').textContent = `${totals.myShare.toFixed(2)} ₪`;
  document.getElementById('summary-approved-count').textContent = `${totals.itemsApproved} / ${totals.totalCount}`;

  // Populate Breakdown List
  const breakdownList = document.getElementById('breakdown-list');
  breakdownList.innerHTML = '';

  const filtered = getFilteredItems();
  filtered.forEach(it => {
    const dec = state.decisions[it.id] || 'pass';
    const row = document.createElement('div');
    row.className = 'breakdown-item';

    let badgeText = 'לא משתתף';
    let badgeClass = 'passed';
    let userPays = '0.00 ₪';

    if (dec === 'half') {
      badgeText = 'משתתף חצי (50%)';
      badgeClass = 'shared';
      userPays = `${(it.price / 2).toFixed(2)} ₪`;
    } else if (dec === 'full') {
      badgeText = 'משלם מלא (100%)';
      badgeClass = 'full';
      userPays = `${it.price.toFixed(2)} ₪`;
    }

    row.innerHTML = `
      <div class="breakdown-item-left">
        <img src="${it.image}" alt="${it.name}" class="breakdown-thumb">
        <div>
          <div style="font-weight: 700;">${it.name}</div>
          <div style="color: var(--text-dim); font-size: 11px;">
            ${it.store} • מחיר: ${it.price.toFixed(2)} ₪
          </div>
        </div>
      </div>
      <div style="display: flex; flex-direction: column; align-items: flex-end; gap: 4px;">
        <span class="breakdown-badge ${badgeClass}">${badgeText}</span>
        <span style="font-weight: 700; color: #10b981; font-family: Outfit;">${userPays}</span>
      </div>
    `;

    breakdownList.appendChild(row);
  });

  summaryModal.style.display = 'block';
  launchConfetti();
}

function closeSummaryModal() {
  summaryModal.style.display = 'none';
}

// Generate & Open WhatsApp Message
function sendWhatsappMessage() {
  const totals = computeTotals();
  const filtered = getFilteredItems();
  
  let msg = `היי אחי, עברתי על הקניות לדירה (רמי לוי ומקס סטוק) 🛒✨\n\n`;
  msg += `💰 סה"כ קניות בקבלות: ₪${totals.totalSpent.toFixed(2)}\n`;
  msg += `🤝 החלק שלי לתשלום: ₪${totals.partnerOwes.toFixed(2)}\n\n`;
  msg += `📦 מוצרים שאישרתי להשתתף בהם (${totals.itemsApproved} מוצרים):\n`;

  filtered.forEach(it => {
    const dec = state.decisions[it.id];
    if (dec === 'half') {
      msg += `• ${it.name} - ₪${(it.price / 2).toFixed(2)} (חצי מ-₪${it.price.toFixed(2)})\n`;
    } else if (dec === 'full') {
      msg += `• ${it.name} - ₪${it.price.toFixed(2)} (מלא)\n`;
    }
  });

  msg += `\nמעביר לך בביט / פייבוקס! תודה רבה 🙏`;

  const url = `https://api.whatsapp.com/send?text=${encodeURIComponent(msg)}`;
  window.open(url, '_blank');
}

// Copy Summary Text
function copySummaryText() {
  const totals = computeTotals();
  const text = `סיכום קניות לדירה:\nסה"כ: ${totals.totalSpent.toFixed(2)} ₪\nחלק השותף לתשלום: ${totals.partnerOwes.toFixed(2)} ₪\nמוצרים שאושרו: ${totals.itemsApproved} מתוך ${totals.totalCount}`;
  
  navigator.clipboard.writeText(text).then(() => {
    showToast('הסיכום הועתק ללוח!');
  }).catch(() => {
    showToast('העתקה נכשלה');
  });
}

// Restart App
function restartApp() {
  if (confirm('האם אתה בטוח שברצונך לאפס את כל ההחלטות ולהתחיל מחדש?')) {
    state.decisions = {};
    state.history = [];
    state.currentIndex = 0;
    saveStoredState();
    closeSummaryModal();
    renderDeck();
    updateLiveDisplay();
    renderListView();
    showToast('האפליקציה אופסה בהצלחה');
  }
}

// Toast Display
function showToast(msg) {
  toastMsg.textContent = msg;
  toastMsg.classList.add('show');
  setTimeout(() => toastMsg.classList.remove('show'), 2200);
}

// Confetti Particle Effect
function launchConfetti() {
  const canvas = document.getElementById('confetti-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;

  const particles = [];
  const colors = ['#f43f5e', '#10b981', '#3b82f6', '#f59e0b', '#8b5cf6', '#ec4899'];

  for (let i = 0; i < 90; i++) {
    particles.push({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height * 0.4,
      w: Math.random() * 8 + 4,
      h: Math.random() * 8 + 4,
      color: colors[Math.floor(Math.random() * colors.length)],
      vx: (Math.random() - 0.5) * 5,
      vy: Math.random() * 3 + 2,
      rot: Math.random() * 360,
      vrot: (Math.random() - 0.5) * 8
    });
  }

  let animationFrame;
  let start = Date.now();

  function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    const elapsed = Date.now() - start;

    particles.forEach(p => {
      p.x += p.vx;
      p.y += p.vy;
      p.rot += p.vrot;

      ctx.save();
      ctx.translate(p.x, p.y);
      ctx.rotate((p.rot * Math.PI) / 180);
      ctx.fillStyle = p.color;
      ctx.fillRect(-p.w / 2, -p.h / 2, p.w, p.h);
      ctx.restore();
    });

    if (elapsed < 3200) {
      animationFrame = requestAnimationFrame(render);
    } else {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      cancelAnimationFrame(animationFrame);
    }
  }

  render();
}

// Event Listeners Initialization
function initEventListeners() {
  // Action Buttons
  btnUndo.addEventListener('click', handleUndo);
  
  btnPass.addEventListener('click', () => {
    const filtered = getFilteredItems();
    if (state.currentIndex < filtered.length) {
      const activeCard = document.querySelector('.tinder-card.card-active');
      if (activeCard) triggerCardDecision(activeCard, filtered[state.currentIndex], 'pass');
    }
  });

  btnShare.addEventListener('click', () => {
    const filtered = getFilteredItems();
    if (state.currentIndex < filtered.length) {
      const activeCard = document.querySelector('.tinder-card.card-active');
      if (activeCard) triggerCardDecision(activeCard, filtered[state.currentIndex], 'half');
    }
  });

  btnFull.addEventListener('click', () => {
    const filtered = getFilteredItems();
    if (state.currentIndex < filtered.length) {
      const activeCard = document.querySelector('.tinder-card.card-active');
      if (activeCard) triggerCardDecision(activeCard, filtered[state.currentIndex], 'full');
    }
  });

  // Keyboard Shortcuts
  window.addEventListener('keydown', (e) => {
    if (e.target.tagName === 'INPUT') return;
    if (e.key === 'ArrowRight') {
      btnShare.click();
    } else if (e.key === 'ArrowLeft') {
      btnPass.click();
    } else if (e.key === 'ArrowUp') {
      btnFull.click();
    } else if (e.key.toLowerCase() === 'z' || e.key === 'Backspace') {
      handleUndo();
    }
  });

  // Store Filter Pills
  const filterPills = document.querySelectorAll('.filter-pill[data-filter]');
  filterPills.forEach(pill => {
    pill.addEventListener('click', () => {
      filterPills.forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      state.activeFilter = pill.dataset.filter;
      state.currentIndex = 0; // restart filtered stack from beginning
      renderDeck();
      updateLiveDisplay();
      renderListView();
    });
  });

  // Mode Toggle (Deck vs List)
  btnToggleMode.addEventListener('click', () => {
    state.isListView = !state.isListView;
    if (state.isListView) {
      tinderView.style.display = 'none';
      listView.style.display = 'flex';
      modeIcon.textContent = '🔥';
      modeText.textContent = 'טינדר';
      renderListView();
    } else {
      listView.style.display = 'none';
      tinderView.style.display = 'flex';
      modeIcon.textContent = '📋';
      modeText.textContent = 'רשימה';
      renderDeck();
    }
  });

  // List search
  listSearchInput.addEventListener('input', renderListView);

  // Summary Modals
  btnOpenSummary.addEventListener('click', openSummaryModal);
  btnCloseSummary.addEventListener('click', closeSummaryModal);
  btnViewSummaryFromList.addEventListener('click', openSummaryModal);
  btnSendWhatsapp.addEventListener('click', sendWhatsappMessage);
  btnCopySummary.addEventListener('click', copySummaryText);
  btnRestartApp.addEventListener('click', restartApp);

  // Close modal when clicking outside
  summaryModal.addEventListener('click', (e) => {
    if (e.target === summaryModal) closeSummaryModal();
  });
}

// App Initialization
document.addEventListener('DOMContentLoaded', () => {
  loadStoredState();
  initEventListeners();
  renderDeck();
  updateLiveDisplay();
  renderListView();
});
