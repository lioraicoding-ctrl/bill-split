import urllib.request
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

endpoints = [
    "https://www.maxstock.co.il/wp-json/wc/store/v1/products?search=9720000682693",
    "https://www.maxstock.co.il/wp-json/wp/v2/product?search=9720000682693",
    "https://www.maxstock.co.il/wp-json/wp/v2/search?search=9720000682693"
]

for ep in endpoints:
    try:
        req = urllib.request.Request(ep, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as resp:
            print(ep, "Status:", resp.status)
            txt = resp.read().decode('utf-8')
            print("Response length:", len(txt), "Sample:", txt[:200])
    except Exception as e:
        print(ep, "Error:", e)
