import urllib.request
import urllib.parse
import json

headers = {'User-Agent': 'Mozilla/5.0'}

queries = {
    "7290003491124": ["שקיות אוכל", "שקית אוכל"],
    "7290003495849": ["שקיות אשפה", "אשפה שרוך"],
    "7290020320025": ["כריות קרצוף", "ספוג קרצוף", "סקוטש"]
}

for bc, q_list in queries.items():
    found = False
    for q in q_list:
        url = f"https://www.maxstock.co.il/wp-json/wc/store/v1/products?search={urllib.parse.quote(q)}"
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=5) as resp:
                items = json.loads(resp.read().decode('utf-8'))
                if items:
                    for it in items:
                        imgs = it.get('images', [])
                        if imgs and imgs[0].get('src'):
                            img_url = imgs[0]['src']
                            # download it
                            r = urllib.request.urlopen(urllib.request.Request(img_url, headers=headers), timeout=5)
                            data = r.read()
                            with open(f"images/max_stock/{bc}.jpg", "wb") as f:
                                f.write(data)
                            print(f"Downloaded {bc} via '{q}': {it.get('name')} -> {img_url}")
                            found = True
                            break
            if found:
                break
        except Exception as e:
            print(f"Error {bc} ({q}): {e}")
