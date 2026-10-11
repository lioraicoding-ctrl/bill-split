import urllib.request
import os
import json

rami_levy_items = [
    {"barcode": "7290004064457", "name": "מלח שולחן בשקית", "price": 1.80, "cat": "מזון"},
    {"barcode": "7290000060880", "name": "ספגטי אסם מס' 8 (2 יחידות)", "price": 9.80, "qty": 2, "unit_price": 4.90, "cat": "מזון"},
    {"barcode": "7290000060903", "name": "פתיתים אפויים אסם (2 יחידות)", "price": 9.80, "qty": 2, "unit_price": 4.90, "cat": "מזון"},
    {"barcode": "8715700419732", "name": "קטשופ היינץ 700 גרם", "price": 7.90, "orig_price": 14.90, "discount": 7.00, "cat": "מזון"},
    {"barcode": "7290119672318", "name": "שמן קנולה 1 ליטר", "price": 8.90, "cat": "מזון"},
    {"barcode": "7290117263389", "name": "שמן זית כתית מעולה 750 מ\"ל", "price": 19.80, "orig_price": 29.70, "discount": 9.90, "cat": "מזון"},
    {"barcode": "7290000207162", "name": "רוטב עגבניות (4 יחידות)", "price": 8.80, "qty": 4, "unit_price": 2.20, "cat": "מזון"},
    {"barcode": "7290005287213", "name": "רביעיית טונה סטארקיסט", "price": 21.90, "orig_price": 24.90, "discount": 3.00, "cat": "מזון"},
    {"barcode": "7290006784766", "name": "נוזל חלונות 1 ליטר", "price": 3.90, "orig_price": 5.90, "discount": 2.00, "cat": "ניקיון"},
    {"barcode": "8700216421881", "name": "שמפו פנטן לחות Pantene", "price": 18.90, "cat": "טואלטיקה"},
    {"barcode": "7290104960338", "name": "נקה 7 תחליב רחצה (2 יחידות)", "price": 16.00, "orig_price": 19.80, "discount": 3.80, "qty": 2, "cat": "טואלטיקה"},
    {"barcode": "7290116055664", "name": "כוסות שתיה חמה", "price": 7.90, "cat": "חד פעמי"},
    {"barcode": "7777886605768", "name": "יעה עם פס גומי", "price": 4.90, "cat": "ניקיון"},
    {"barcode": "7290000286549", "name": "מטליות לניקוי", "price": 9.90, "cat": "ניקיון"},
    {"barcode": "7290005424847", "name": "מפיות נייר סנו", "price": 7.50, "cat": "חד פעמי"},
    {"barcode": "7290101828815", "name": "כפפות ניטריל מידה L", "price": 19.90, "cat": "ניקיון"},
    {"barcode": "9007829022023", "name": "סוכר לבן 1 ק\"ג", "price": 4.90, "cat": "מזון"},
    {"barcode": "7290000211442", "name": "אורז פרסי קלאסי סוגת 1 ק\"ג", "price": 11.70, "cat": "מזון"},
    {"barcode": "7290000262239", "name": "נייר טואלט מולט", "price": 39.90, "cat": "טואלטיקה"},
    {"barcode": "8700216811491", "name": "נוזל כלים פיירי Fairy", "price": 17.90, "cat": "ניקיון"},
    {"barcode": "7290014673137", "name": "תערובת תיבול לבישול", "price": 12.40, "cat": "מזון"},
    {"barcode": "7290010002382", "name": "תבלין אורגנו", "price": 10.60, "cat": "מזון"},
    {"barcode": "7290010002214", "name": "תבלין צ'ילי גרוס", "price": 12.40, "cat": "מזון"},
    {"barcode": "7290000291963", "name": "אקונומיקה סמיכה מבושמת", "price": 8.90, "cat": "ניקיון"},
    {"barcode": "7290000289380", "name": "ג'ל לניקוי אסלה", "price": 9.90, "cat": "ניקיון"},
    {"barcode": "7290116533575", "name": "סיף פנטסטיק לניקוי כללי", "price": 22.90, "cat": "ניקיון"},
    {"barcode": "7290016865615", "name": "כדוריות סבון לאסלה (שלישייה)", "price": 8.90, "orig_price": 9.90, "discount": 1.00, "cat": "ניקיון"},
    {"barcode": "7290000688503", "name": "שישיית מים מינרלים (כולל פיקדון)", "price": 14.90, "details": "13.10 ₪ + 1.80 ₪ פיקדון", "cat": "שתייה"},
    {"barcode": "7290121042321", "name": "מארז 6 קולבים", "price": 14.90, "cat": "לבית"},
    {"barcode": "7290003387410", "name": "פדים להסרת איפור", "price": 15.90, "cat": "טואלטיקה"},
    {"barcode": "7290004078263", "name": "צמרוני אוזניים", "price": 9.90, "cat": "טואלטיקה"},
    {"barcode": "7290000188355", "name": "מגבות נייר ניקול", "price": 10.90, "cat": "לבית"},
    {"barcode": "7290116053905", "name": "סט כפות במבוק לבישול", "price": 9.90, "cat": "לבית"},
]

os.makedirs("images/rami_levy", exist_ok=True)
headers = {'User-Agent': 'Mozilla/5.0'}

results = []
for item in rami_levy_items:
    bc = item["barcode"]
    urls_to_try = [
        f"https://img.rami-levy.co.il/product/{bc}/large.jpg",
        f"https://img.rami-levy.co.il/product/{bc}/small.jpg",
        f"https://res.cloudinary.com/shufersal/image/upload/f_auto,q_auto/v1551800005/prod/product_images/products_medium/{bc}_1.png",
    ]
    saved = False
    for url in urls_to_try:
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=5) as resp:
                if resp.status == 200:
                    data = resp.read()
                    if len(data) > 1000: # not empty/error
                        ext = ".png" if "shufersal" in url else ".jpg"
                        out_path = f"images/rami_levy/{bc}{ext}"
                        with open(out_path, "wb") as f:
                            f.write(data)
                        item["image"] = out_path
                        saved = True
                        print(f"SUCCESS: {bc} ({item['name']}) -> {out_path} ({len(data)} bytes)")
                        break
        except Exception as e:
            continue
    if not saved:
        print(f"MISSING: {bc} ({item['name']})")
        item["image"] = None
    results.append(item)

with open("rami_levy_data.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
