import urllib.request
import urllib.parse
import json
import os
import time

max_stock_items = [
    {"barcode": "810032523039", "name": "מיכל אחסון מזון", "full_name": "מיכל אחסון מזון (3 יחידות)", "price": 30.00, "qty": 3, "unit_price": 10.00, "cat": "מטבח", "search_term": "מיכל אחסון מזון"},
    {"barcode": "9720000682693", "name": "פח דוושה 6.5 ליטר OCEAN", "full_name": "פח דוושה 6.5 ליטר OCEAN", "price": 20.90, "cat": "אמבטיה וניקיון", "search_term": "9720000682693"},
    {"barcode": "7290003491124", "name": "זוג שקיות אוכל", "full_name": "זוג שקיות אוכל", "price": 10.90, "cat": "מטבח", "search_term": "7290003491124"},
    {"barcode": "7290003495849", "name": "שקיות אשפה מוטבעות", "full_name": "שקיות אשפה מוטבעות עם שרוך", "price": 20.90, "cat": "ניקיון", "search_term": "7290003495849"},
    {"barcode": "7299999180395", "name": "צלחות שקופות ארוז", "full_name": "צלחות 10 שקוף ארוז", "price": 10.90, "cat": "מטבח", "search_term": "צלחות שקוף"},
    {"barcode": "7299999202813", "name": "מטליות מיקרופייבר", "full_name": "מטליות מיקרופייבר (2 מארזים)", "price": 31.80, "qty": 2, "unit_price": 15.90, "cat": "ניקיון", "search_term": "מטליות מיקרופייבר"},
    {"barcode": "7290020320025", "name": "סקוטש קרצוף אדום", "full_name": "סקוטש קרצוף אדום (2 מארזים)", "price": 21.80, "qty": 2, "unit_price": 10.90, "cat": "ניקיון", "search_term": "סקוטש קרצוף אדום"},
    {"barcode": "7290019337799", "name": "כרית יפנית איכותית", "full_name": "כרית יפנית איכותית לקרצוף", "price": 5.90, "cat": "ניקיון", "search_term": "כרית יפנית"},
    {"barcode": "7290003458868", "name": "מגב חלון חד להב", "full_name": "מגב חלון חד להב", "price": 10.90, "cat": "ניקיון", "search_term": "מגב חד להב"},
    {"barcode": "7299999163879", "name": "מגב לחלון 25 ס\"מ", "full_name": "מגב לחלון 25 ס\"מ", "price": 5.90, "cat": "ניקיון", "search_term": "מגב לחלון 25"},
    {"barcode": "7299999179054", "name": "מתלה תלייה OCEAN דבק", "full_name": "מתלה תלייה OCEAN דבק", "price": 5.90, "cat": "אמבטיה", "search_term": "מתלה OCEAN"},
    {"barcode": "7299999164043", "name": "מטאטא ביתי", "full_name": "ראש מטאטא", "price": 10.90, "cat": "ניקיון", "search_term": "מטאטא"},
    {"barcode": "7290115863963", "name": "ניילון נצמד שלישייה", "full_name": "ניילון נצמד שלישייה", "price": 15.90, "cat": "מטבח", "search_term": "ניילון נצמד שלישייה"},
    {"barcode": "9720000699141", "name": "מקל מטאטא 1.5 מטר", "full_name": "מקל מטאטא/מגב 1.5 מטר (2 יח')", "price": 11.80, "qty": 2, "unit_price": 5.90, "cat": "ניקיון", "search_term": "מקל מטאטא 1.5"},
    {"barcode": "7290003441372", "name": "שקיות אשפה לפח שירותים", "full_name": "שקיות אשפה לפח שירותים", "price": 10.90, "cat": "ניקיון", "search_term": "7290003441372"},
    {"barcode": "7290003478613", "name": "נייר טישו 5 יחידות", "full_name": "נייר טישו חמישייה", "price": 5.90, "cat": "טואלטיקה", "search_term": "נייר טישו"},
    {"barcode": "7290106441231", "name": "סכומון למגירה", "full_name": "סכומון למגירת מטבח", "price": 10.90, "cat": "מטבח", "search_term": "סכומון למגירה"},
    {"barcode": "9720000483207", "name": "סל נייר דגם שיש", "full_name": "סל נייר דגם שיש", "price": 10.00, "cat": "לבית", "search_term": "סל נייר"},
    {"barcode": "7299999105664", "name": "דיספנסר לסבון שיש", "full_name": "דיספנסר לסבון דגם שיש", "price": 20.90, "cat": "אמבטיה", "search_term": "דיספנסר לסבון"},
    {"barcode": "7290003456475", "name": "סל כביסה 45 ליטר", "full_name": "סל כביסה 45 ליטר", "price": 59.00, "cat": "לבית", "search_term": "7290003456475"},
    {"barcode": "9720000199191", "name": "אזיקונים 50 יחידות", "full_name": "אזיקונים 50 יחידות", "price": 5.90, "cat": "כלי עבודה", "search_term": "אזיקונים"},
    {"barcode": "6920902690663", "name": "מספריים אורטופדיים", "full_name": "מספריים אורטופדיים", "price": 5.00, "cat": "כלי עבודה", "search_term": "מספריים"},
    {"barcode": "7299998849088", "name": "מברג שטוח", "full_name": "מברג שטוח", "price": 3.90, "cat": "כלי עבודה", "search_term": "מברג שטוח"},
    {"barcode": "7299998849071", "name": "מברג פיליפס", "full_name": "מברג פיליפס", "price": 3.90, "cat": "כלי עבודה", "search_term": "מברג פיליפס"},
    {"barcode": "7299999111399", "name": "מאג זכוכית 350 מ\"ל", "full_name": "מאג זכוכית 350 מ\"ל", "price": 3.90, "cat": "מטבח", "search_term": "מאג זכוכית"},
    {"barcode": "6920902623357", "name": "סלוטייפ סט 8 יחידות", "full_name": "סלוטייפ סט 8 יחידות", "price": 5.00, "cat": "לבית", "search_term": "סלוטייפ"},
    {"barcode": "7299999188643", "name": "מסחטת לימון זכוכית", "full_name": "מסחטת לימון זכוכית", "price": 10.90, "cat": "מטבח", "search_term": "מסחטת לימון"},
    {"barcode": "7299998937952", "name": "קערית נירוסטה 24 ס\"מ", "full_name": "קערית נירוסטה 24 ס\"מ", "price": 10.00, "cat": "מטבח", "search_term": "קערית נירוסטה"}
]

os.makedirs("images/max_stock", exist_ok=True)
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def search_max_stock(term):
    url = f"https://www.maxstock.co.il/wp-json/wc/store/v1/products?search={urllib.parse.quote(term)}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=6) as resp:
            items = json.loads(resp.read().decode('utf-8'))
            if items:
                for it in items:
                    images = it.get('images', [])
                    if images and images[0].get('src'):
                        return images[0]['src'], it.get('name')
    except Exception as e:
        print(f"Error searching {term}: {e}")
    return None, None

results = []
for item in max_stock_items:
    bc = item["barcode"]
    img_url, found_name = search_max_stock(item["barcode"])
    if not img_url and item.get("search_term"):
        img_url, found_name = search_max_stock(item["search_term"])
    
    saved = False
    if img_url:
        try:
            req = urllib.request.Request(img_url, headers=headers)
            with urllib.request.urlopen(req, timeout=6) as r:
                data = r.read()
                out_path = f"images/max_stock/{bc}.jpg"
                with open(out_path, "wb") as f:
                    f.write(data)
                item["image"] = out_path
                saved = True
                print(f"SUCCESS: {bc} ({item['name']}) -> {out_path} [{found_name}]")
        except Exception as e:
            print(f"Failed to download image for {bc}: {e}")
    
    if not saved:
        print(f"NOT FOUND: {bc} ({item['name']})")
        item["image"] = None
    
    results.append(item)
    time.sleep(0.3)

with open("max_stock_data.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
