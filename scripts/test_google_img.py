import urllib.request
import urllib.parse
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

def get_google_img(query):
    url = "https://www.google.com/search?tbm=isch&q=" + urllib.parse.quote(query)
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=6) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
    
    # find images
    matches = re.findall(r'\["(https://[^"]+)",\s*\d+,\s*\d+\]', html)
    real_imgs = [m for m in matches if m.endswith(('.jpg', '.jpeg', '.png', '.webp')) or 'encrypted-tbn0' in m]
    if real_imgs:
        return real_imgs[0]
    
    # or look for gstatic
    tbns = re.findall(r'(https://encrypted-tbn0\.gstatic\.com/images\?q=[^"]+)', html)
    if tbns:
        return tbns[0].replace('\\u003d', '=').replace('\\x3d', '=')
    return None

test = get_google_img("פח דוושה 6.5 ליטר ocean מקס סטוק")
print("Google img:", test)
test2 = get_google_img("קערית נירוסטה 24 סמ מקס סטוק")
print("Google img 2:", test2)
test3 = get_google_img("סל כביסה 45 ליטר מקס סטוק")
print("Google img 3:", test3)
