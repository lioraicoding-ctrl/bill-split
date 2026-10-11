import urllib.request
import urllib.parse
import re
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7'
}

def search_bing_image(query):
    try:
        url = "https://www.bing.com/images/search?q=" + urllib.parse.quote(query) + "&FORM=HDRSC2"
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=8) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
        
        matches = re.findall(r'murl&quot;:&quot;(http[^&]+)&quot;', html)
        if matches:
            return matches[0]
        # alternative pattern: "murl":"https://..."
        matches2 = re.findall(r'"murl":"(http[^"]+)"', html)
        if matches2:
            return matches2[0]
    except Exception as e:
        print("Error:", e)
    return None

test_query = "פח דוושה 6.5 ליטר ocean מקס סטוק"
img = search_bing_image(test_query)
print("Query:", test_query)
print("Image found:", img)
