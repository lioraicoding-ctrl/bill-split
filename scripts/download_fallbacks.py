import urllib.request

test_barcodes = [
    ("7290003491124", "https://img.rami-levy.co.il/product/7290005421686/small.jpg"), # סנו שקיות אוכל
    ("7290003495849", "https://img.rami-levy.co.il/product/7290005423642/small.jpg"), # סנו שקיות אשפה עם שרוך
    ("7290020320025", "https://img.rami-levy.co.il/product/7290005420016/small.jpg"), # סנו כריות קרצוף
]

headers = {'User-Agent': 'Mozilla/5.0'}
for item_bc, url in test_barcodes:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as resp:
            if resp.status == 200:
                data = resp.read()
                with open(f"images/max_stock/{item_bc}.jpg", "wb") as f:
                    f.write(data)
                print(f"Downloaded {item_bc} from {url} ({len(data)} bytes)")
    except Exception as e:
        print(f"Failed {item_bc}: {e}")
