import urllib.request
import urllib.parse

req = urllib.request.Request("https://html.duckduckgo.com/html/?q=maxstock+israel", headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req, timeout=5) as r:
        html = r.read().decode('utf-8', errors='ignore')
        print("HTML len:", len(html))
        print("First 300 chars:", html[:300])
except Exception as e:
    print("Error:", e)
