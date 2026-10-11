import urllib.request
import json
import os

max_stock_items = [
    {"barcode": "810032523039", "name": "מיכל אחסון מזון (3 יחידות)", "price": 30.00, "qty": 3, "unit_price": 10.00, "cat": "מטבח"},
    {"barcode": "9720000682693", "name": "פח דוושה 6.5 ליטר OCEAN", "price": 20.90, "cat": "אמבטיה וניקיון"},
    {"barcode": "7290003491124", "name": "זוג שקיות אוכל", "price": 10.90, "cat": "מטבח"},
    {"barcode": "7290003495849", "name": "שקיות אשפה מוטבעות עם שרוך", "price": 20.90, "cat": "ניקיון"},
    {"barcode": "7299999180395", "name": "צלחות שקופות קשיחות (10 יח')", "price": 10.90, "cat": "מטבח"},
    {"barcode": "7299999202813", "name": "מטליות מיקרופייבר (2 מארזים)", "price": 31.80, "qty": 2, "unit_price": 15.90, "cat": "ניקיון"},
    {"barcode": "7290020320025", "name": "סקוטש קרצוף אדום (2 מארזים)", "price": 21.80, "qty": 2, "unit_price": 10.90, "cat": "ניקיון"},
    {"barcode": "7290019337799", "name": "כרית יפנית איכותית לקרצוף", "price": 5.90, "cat": "ניקיון"},
    {"barcode": "7290003458868", "name": "מגב חלון חד להב", "price": 10.90, "cat": "ניקיון"},
    {"barcode": "7299999163879", "name": "מגב לחלון 25 ס\"מ", "price": 5.90, "cat": "ניקיון"},
    {"barcode": "7299999179054", "name": "מתלה ואקום/הדבקה OCEAN", "price": 5.90, "cat": "אמבטיה"},
    {"barcode": "7299999164043", "name": "ראש מטאטא", "price": 10.90, "cat": "ניקיון"},
    {"barcode": "7290115863963", "name": "ניילון נצמד (שלישייה)", "price": 15.90, "cat": "מטבח"},
    {"barcode": "9720000699141", "name": "מקל מטאטא/מגב 1.5 מ' (2 יח')", "price": 11.80, "qty": 2, "unit_price": 5.90, "cat": "ניקיון"},
    {"barcode": "7290003441372", "name": "שקיות אשפה לפח שירותים", "price": 10.90, "cat": "ניקיון"},
    {"barcode": "7290003478613", "name": "נייר טישו (מארז 5 יחידות)", "price": 5.90, "cat": "טואלטיקה"},
    {"barcode": "7290106441231", "name": "סכומון למגירת מטבח", "price": 10.90, "cat": "מטבח"},
    {"barcode": "9720000483207", "name": "סל נייר דגם שיש", "price": 10.00, "cat": "לבית"},
    {"barcode": "7299999105664", "name": "דיספנסר לסבון דגם שיש", "price": 20.90, "cat": "אמבטיה"},
    {"barcode": "7290003456475", "name": "סל כביסה 45 ליטר", "price": 59.00, "cat": "לבית"},
    {"barcode": "9720000199191", "name": "אזיקונים 50 יחידות", "price": 5.90, "cat": "כלי עבודה"},
    {"barcode": "6920902690663", "name": "מספריים אורטופדיים", "price": 5.00, "cat": "כלי עבודה"},
    {"barcode": "7299998849088", "name": "מברג שטוח", "price": 3.90, "cat": "כלי עבודה"},
    {"barcode": "7299998849071", "name": "מברג פיליפס (צלב)", "price": 3.90, "cat": "כלי עבודה"},
    {"barcode": "7299999111399", "name": "מאג זכוכית 350 מ\"ל", "price": 3.90, "cat": "מטבח"},
    {"barcode": "6920902623357", "name": "סלוטייפ (סט 8 יחידות)", "price": 5.00, "cat": "לבית"},
    {"barcode": "7299999188643", "name": "מסחטת לימון מזכוכית", "price": 10.90, "cat": "מטבח"},
    {"barcode": "7299998937952", "name": "קערית נירוסטה 24 ס\"מ", "price": 10.00, "cat": "מטבח"}
]

os.makedirs("images/max_stock", exist_ok=True)
headers = {'User-Agent': 'Mozilla/5.0'}

for item in max_stock_items:
    bc = item["barcode"]
    urls = [
        f"https://img.rami-levy.co.il/product/{bc}/large.jpg",
        f"https://img.rami-levy.co.il/product/{bc}/small.jpg",
        f"https://res.cloudinary.com/shufersal/image/upload/f_auto,q_auto/v1551800005/prod/product_images/products_medium/{bc}_1.png",
    ]
    found = False
    for u in urls:
        try:
            req = urllib.request.Request(u, headers=headers)
            with urllib.request.urlopen(req, timeout=3) as resp:
                if resp.status == 200:
                    d = resp.read()
                    if len(d) > 1000:
                        path = f"images/max_stock/{bc}.jpg"
                        with open(path, "wb") as f:
                            f.write(d)
                        found = True
                        print(f"FOUND: {bc} ({item['name']}) -> {path}")
                        break
        except:
            pass
    if not found:
        print(f"NOT FOUND ON CDN: {bc} ({item['name']})")
