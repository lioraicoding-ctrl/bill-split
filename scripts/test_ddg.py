import urllib.request
import urllib.parse
import json
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://duckduckgo.com/'
}

def get_ddg_image(query):
    try:
        url = "https://duckduckgo.com/?q=" + urllib.parse.quote(query)
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=7) as resp:
            content = resp.read().decode('utf-8', errors='ignore')
        
        # Look for vqd token
        vqd_match = re.search(r'vqd=([0-9-]+)&', content) or re.search(r'vqd="([^"]+)"', content) or re.search(r'vqd=([a-zA-Z0-9_-]+)', content)
        if not vqd_match:
            # try finding vqd in javascript
            vqd_match = re.search(r'vqd=[\'"]?([0-9a-zA-Z_-]+)[\'"]?', content)
        if not vqd_match:
            print("No vqd found for query:", query)
            return None
        vqd = vqd_match.group(1)
        
        img_url = f"https://duckduckgo.com/i.js?l=wt-wt&o=json&q={urllib.parse.quote(query)}&vqd={vqd}&f=,,,&p=1"
        req2 = urllib.request.Request(img_url, headers=headers)
        with urllib.request.urlopen(req2, timeout=7) as resp2:
            data = json.loads(resp2.read().decode('utf-8'))
            results = data.get('results', [])
            if results:
                return results[0].get('image')
    except Exception as e:
        print("Error:", e)
    return None

print("Result:", get_ddg_image("פח דוושה 6.5 ליטר ocean מקס סטוק"))
