import urllib.request
import json

extra_rami = [
    ("9007829022023", "https://img.rami-levy.co.il/product/9007829022023/347339/medium.jpg"),
    ("7777886605768", "https://img.rami-levy.co.il/product/7777886605768/372101/medium.jpg"),
    ("7290101828815", "https://ksp.co.il/shop/items/512/282455.jpg"),
    ("7290121042321", "https://img.rami-levy.co.il/product/7777886602972/297682/medium.jpg")
]

headers = {'User-Agent': 'Mozilla/5.0'}
for bc, url in extra_rami:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = resp.read()
            with open(f"images/rami_levy/{bc}.jpg", "wb") as f:
                f.write(data)
            print(f"Downloaded {bc} ({len(data)} bytes)")
    except Exception as e:
        print(f"Error {bc}: {e}")
