import json

rami_levy_items = [
    {
        "id": "rl_1",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "מלח שולחן בשקית 1 ק\"ג",
        "category": "מזון",
        "barcode": "7290004064457",
        "price": 1.80,
        "quantity": 1,
        "image": "images/rami_levy/7290004064457.jpg"
    },
    {
        "id": "rl_2",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "ספגטי אסם מס' 8",
        "category": "מזון",
        "barcode": "7290000060880",
        "price": 9.80,
        "quantity": 2,
        "details": "2 יחידות × 4.90 ₪",
        "image": "images/rami_levy/7290000060880.jpg"
    },
    {
        "id": "rl_3",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "פתיתים אפויים אסם",
        "category": "מזון",
        "barcode": "7290000060903",
        "price": 9.80,
        "quantity": 2,
        "details": "2 יחידות × 4.90 ₪",
        "image": "images/rami_levy/7290000060903.jpg"
    },
    {
        "id": "rl_4",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "קטשופ היינץ 700 גרם",
        "category": "מזון",
        "barcode": "8715700419732",
        "price": 7.90,
        "originalPrice": 14.90,
        "discount": 7.00,
        "quantity": 1,
        "details": "במבצע: 7.90 ₪ (במקום 14.90 ₪)",
        "image": "images/rami_levy/8715700419732.jpg"
    },
    {
        "id": "rl_5",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "שמן קנולה 1 ליטר",
        "category": "מזון",
        "barcode": "7290119672318",
        "price": 8.90,
        "quantity": 1,
        "image": "images/rami_levy/7290119672318.jpg"
    },
    {
        "id": "rl_6",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "שמן זית כתית מעולה 750 מ\"ל",
        "category": "מזון",
        "barcode": "7290117263389",
        "price": 19.80,
        "originalPrice": 29.70,
        "discount": 9.90,
        "quantity": 1,
        "details": "במבצע: 19.80 ₪ (במקום 29.70 ₪)",
        "image": "images/rami_levy/7290117263389.jpg"
    },
    {
        "id": "rl_7",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "רוטב עגבניות",
        "category": "מזון",
        "barcode": "7290000207162",
        "price": 8.80,
        "quantity": 4,
        "details": "4 יחידות × 2.20 ₪",
        "image": "images/rami_levy/7290000207162.jpg"
    },
    {
        "id": "rl_8",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "רביעיית טונה סטארקיסט",
        "category": "מזון",
        "barcode": "7290005287213",
        "price": 21.90,
        "originalPrice": 24.90,
        "discount": 3.00,
        "quantity": 1,
        "details": "במבצע: 21.90 ₪ (במקום 24.90 ₪)",
        "image": "images/rami_levy/7290005287213.jpg"
    },
    {
        "id": "rl_9",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "תרסיס נוזל חלונות 1 ליטר",
        "category": "ניקיון",
        "barcode": "7290006784766",
        "price": 3.90,
        "originalPrice": 5.90,
        "discount": 2.00,
        "quantity": 1,
        "details": "במבצע: 3.90 ₪ (במקום 5.90 ₪)",
        "image": "images/rami_levy/7290006784766.jpg"
    },
    {
        "id": "rl_10",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "שמפו פנטן לחות Pantene",
        "category": "טואלטיקה",
        "barcode": "8700216421881",
        "price": 18.90,
        "quantity": 1,
        "image": "images/rami_levy/8700216421881.jpg"
    },
    {
        "id": "rl_11",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "תחליב רחצה נקה 7",
        "category": "טואלטיקה",
        "barcode": "7290104960338",
        "price": 16.00,
        "originalPrice": 19.80,
        "discount": 3.80,
        "quantity": 2,
        "details": "2 יחידות במבצע: 16.00 ₪ (8.00 ₪ ליח')",
        "image": "images/rami_levy/7290104960338.jpg"
    },
    {
        "id": "rl_12",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "כוסות שתייה חמה חד-פעמי",
        "category": "חד פעמי ולבית",
        "barcode": "7290116055664",
        "price": 7.90,
        "quantity": 1,
        "image": "images/rami_levy/7290116055664.jpg"
    },
    {
        "id": "rl_13",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "יעה עם פס גומי",
        "category": "ניקיון",
        "barcode": "7777886605768",
        "price": 4.90,
        "quantity": 1,
        "image": "images/rami_levy/7777886605768.jpg"
    },
    {
        "id": "rl_14",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "מטליות לניקוי כללי",
        "category": "ניקיון",
        "barcode": "7290000286549",
        "price": 9.90,
        "quantity": 1,
        "image": "images/rami_levy/7290000286549.jpg"
    },
    {
        "id": "rl_15",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "מפיות נייר סנו",
        "category": "חד פעמי ולבית",
        "barcode": "7290005424847",
        "price": 7.50,
        "quantity": 1,
        "image": "images/rami_levy/7290005424847.jpg"
    },
    {
        "id": "rl_16",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "כפפות ניטריל מידה L",
        "category": "ניקיון",
        "barcode": "7290101828815",
        "price": 19.90,
        "quantity": 1,
        "image": "images/rami_levy/7290101828815.jpg"
    },
    {
        "id": "rl_17",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "סוכר לבן 1 ק\"ג",
        "category": "מזון",
        "barcode": "9007829022023",
        "price": 4.90,
        "quantity": 1,
        "image": "images/rami_levy/9007829022023.jpg"
    },
    {
        "id": "rl_18",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "אורז פרסי קלאסי סוגת 1 ק\"ג",
        "category": "מזון",
        "barcode": "7290000211442",
        "price": 11.70,
        "quantity": 1,
        "image": "images/rami_levy/7290000211442.jpg"
    },
    {
        "id": "rl_19",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "נייר טואלט מולט מארז ענק",
        "category": "טואלטיקה",
        "barcode": "7290000262239",
        "price": 39.90,
        "quantity": 1,
        "image": "images/rami_levy/7290000262239.jpg"
    },
    {
        "id": "rl_20",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "נוזל כלים פיירי Fairy",
        "category": "ניקיון",
        "barcode": "8700216811491",
        "price": 17.90,
        "quantity": 1,
        "image": "images/rami_levy/8700216811491.jpg"
    },
    {
        "id": "rl_21",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "תערובת תיבול לבישול",
        "category": "מזון",
        "barcode": "7290014673137",
        "price": 12.40,
        "quantity": 1,
        "image": "images/rami_levy/7290014673137.jpg"
    },
    {
        "id": "rl_22",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "תבלין אורגנו",
        "category": "מזון",
        "barcode": "7290010002382",
        "price": 10.60,
        "quantity": 1,
        "image": "images/rami_levy/7290010002382.jpg"
    },
    {
        "id": "rl_23",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "תבלין צ'ילי גרוס",
        "category": "מזון",
        "barcode": "7290010002214",
        "price": 12.40,
        "quantity": 1,
        "image": "images/rami_levy/7290010002214.jpg"
    },
    {
        "id": "rl_24",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "אקונומיקה סמיכה מבושמת",
        "category": "ניקיון",
        "barcode": "7290000291963",
        "price": 8.90,
        "quantity": 1,
        "image": "images/rami_levy/7290000291963.jpg"
    },
    {
        "id": "rl_25",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "ג'ל לניקוי אסלה עם צוואר ברווז",
        "category": "ניקיון",
        "barcode": "7290000289380",
        "price": 9.90,
        "quantity": 1,
        "image": "images/rami_levy/7290000289380.jpg"
    },
    {
        "id": "rl_26",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "סיף פנטסטיק לניקוי כללי",
        "category": "ניקיון",
        "barcode": "7290116533575",
        "price": 22.90,
        "quantity": 1,
        "image": "images/rami_levy/7290116533575.jpg"
    },
    {
        "id": "rl_27",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "כדוריות סבון לאסלה (שלישייה)",
        "category": "ניקיון",
        "barcode": "7290016865615",
        "price": 8.90,
        "originalPrice": 9.90,
        "discount": 1.00,
        "quantity": 1,
        "details": "במבצע: 8.90 ₪ (במקום 9.90 ₪)",
        "image": "images/rami_levy/7290016865615.jpg"
    },
    {
        "id": "rl_28",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "שישיית מים מינרלים + פיקדון",
        "category": "שתייה",
        "barcode": "7290000688503",
        "price": 14.90,
        "quantity": 1,
        "details": "13.10 ₪ + 1.80 ₪ פיקדון בקבוקים",
        "image": "images/rami_levy/7290000688503.jpg"
    },
    {
        "id": "rl_29",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "מארז 6 קולבי בגדים",
        "category": "לבית",
        "barcode": "7290121042321",
        "price": 14.90,
        "quantity": 1,
        "image": "images/rami_levy/7290121042321.jpg"
    },
    {
        "id": "rl_30",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "פדים עגולים להסרת איפור",
        "category": "טואלטיקה",
        "barcode": "7290003387410",
        "price": 15.90,
        "quantity": 1,
        "image": "images/rami_levy/7290003387410.jpg"
    },
    {
        "id": "rl_31",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "צמרוני אוזניים היגייניים",
        "category": "טואלטיקה",
        "barcode": "7290004078263",
        "price": 9.90,
        "quantity": 1,
        "image": "images/rami_levy/7290004078263.jpg"
    },
    {
        "id": "rl_32",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "מגבות נייר מטבח ניקול",
        "category": "חד פעמי ולבית",
        "barcode": "7290000188355",
        "price": 10.90,
        "quantity": 1,
        "image": "images/rami_levy/7290000188355.jpg"
    },
    {
        "id": "rl_33",
        "store": "רמי לוי",
        "storeKey": "rami_levy",
        "name": "סט כפות במבוק לבישול",
        "category": "מטבח ולבית",
        "barcode": "7290116053905",
        "price": 9.90,
        "quantity": 1,
        "image": "images/rami_levy/7290116053905.jpg"
    }
]

max_stock_items = [
    {
        "id": "ms_1",
        "store": "מקס סטוק",
        "storeKey": "max_stock",
        "name": "מיכל אחסון מזון",
        "category": "מטבח",
        "barcode": "810032523039",
        "price": 30.00,
        "quantity": 3,
        "details": "3 יחידות × 10.00 ₪",
        "image": "images/max_stock/810032523039.jpg"
    },
    {
        "id": "ms_2",
        "store": "מקס סטוק",
        "storeKey": "max_stock",
        "name": "פח דוושה 6.5 ליטר OCEAN",
        "category": "אמבטיה וניקיון",
        "barcode": "9720000682693",
        "price": 20.90,
        "quantity": 1,
        "image": "images/max_stock/9720000682693.jpg"
    },
    {
        "id": "ms_3",
        "store": "מקס סטוק",
        "storeKey": "max_stock",
        "name": "זוג שקיות אוכל",
        "category": "מטבח",
        "barcode": "7290003491124",
        "price": 10.90,
        "quantity": 1,
        "image": "images/max_stock/7290003491124.jpg"
    },
    {
        "id": "ms_4",
        "store": "מקס סטוק",
        "storeKey": "max_stock",
        "name": "שקיות אשפה מוטבעות עם שרוך",
        "category": "ניקיון",
        "barcode": "7290003495849",
        "price": 20.90,
        "quantity": 1,
        "image": "images/max_stock/7290003495849.jpg"
    },
    {
        "id": "ms_5",
        "store": "מקס סטוק",
        "storeKey": "max_stock",
        "name": "צלחות שקופות קשיחות (10 יח')",
        "category": "מטבח ואירוח",
        "barcode": "7299999180395",
        "price": 10.90,
        "quantity": 1,
        "image": "images/max_stock/7299999180395.jpg"
    },
    {
        "id": "ms_6",
        "store": "מקס סטוק",
        "storeKey": "max_stock",
        "name": "מטליות מיקרופייבר",
        "category": "ניקיון",
        "barcode": "7299999202813",
        "price": 31.80,
        "quantity": 2,
        "details": "2 מארזים × 15.90 ₪",
        "image": "images/max_stock/7299999202813.jpg"
    },
    {
        "id": "ms_7",
        "store": "מקס סטוק",
        "storeKey": "max_stock",
        "name": "סקוטש כריות קרצוף אדום",
        "category": "ניקיון",
        "barcode": "7290020320025",
        "price": 21.80,
        "quantity": 2,
        "details": "2 מארזים × 10.90 ₪",
        "image": "images/max_stock/7290020320025.jpg"
    },
    {
        "id": "ms_8",
        "store": "מקס סטוק",
        "storeKey": "max_stock",
        "name": "כרית יפנית איכותית לקרצוף",
        "category": "ניקיון",
        "barcode": "7290019337799",
        "price": 5.90,
        "quantity": 1,
        "image": "images/max_stock/7290019337799.jpg"
    },
    {
        "id": "ms_9",
        "store": "מקס סטוק",
        "storeKey": "max_stock",
        "name": "מגב חלון מקצועי חד להב",
        "category": "ניקיון",
        "barcode": "7290003458868",
        "price": 10.90,
        "quantity": 1,
        "image": "images/max_stock/7290003458868.jpg"
    },
    {
        "id": "ms_10",
        "store": "מקס סטוק",
        "storeKey": "max_stock",
        "name": "מגב לחלון ומקלחון 25 ס\"מ",
        "category": "ניקיון",
        "barcode": "7299999163879",
        "price": 5.90,
        "quantity": 1,
        "image": "images/max_stock/7299999163879.jpg"
    },
    {
        "id": "ms_11",
        "store": "מקס סטוק",
        "storeKey": "max_stock",
        "name": "מתלה קיר OCEAN הדבקה",
        "category": "אמבטיה ולבית",
        "barcode": "7299999179054",
        "price": 5.90,
        "quantity": 1,
        "image": "images/max_stock/7299999179054.jpg"
    },
    {
        "id": "ms_12",
        "store": "מקס סטוק",
        "storeKey": "max_stock",
        "name": "ראש מטאטא ביתי",
        "category": "ניקיון",
        "barcode": "7299999164043",
        "price": 10.90,
        "quantity": 1,
        "image": "images/max_stock/7299999164043.jpg"
    },
    {
        "id": "ms_13",
        "store": "מקס סטוק",
        "storeKey": "max_stock",
        "name": "ניילון נצמד שלישייה",
        "category": "מטבח",
        "barcode": "7290115863963",
        "price": 15.90,
        "quantity": 1,
        "image": "images/max_stock/7290115863963.jpg"
    },
    {
        "id": "ms_14",
        "store": "מקס סטוק",
        "storeKey": "max_stock",
        "name": "מקל מטאטא/מגב 1.5 מטר",
        "category": "ניקיון",
        "barcode": "9720000699141",
        "price": 11.80,
        "quantity": 2,
        "details": "2 יחידות × 5.90 ₪",
        "image": "images/max_stock/9720000699141.jpg"
    },
    {
        "id": "ms_15",
        "store": "מקס סטוק",
        "storeKey": "max_stock",
        "name": "שקיות אשפה לפח שירותים",
        "category": "ניקיון",
        "barcode": "7290003441372",
        "price": 10.90,
        "quantity": 1,
        "image": "images/max_stock/7290003441372.jpg"
    },
    {
        "id": "ms_16",
        "store": "מקס סטוק",
        "storeKey": "max_stock",
        "name": "נייר טישו חמישייה",
        "category": "טואלטיקה",
        "barcode": "7290003478613",
        "price": 5.90,
        "quantity": 1,
        "image": "images/max_stock/7290003478613.jpg"
    },
    {
        "id": "ms_17",
        "store": "מקס סטוק",
        "storeKey": "max_stock",
        "name": "סכומון למגירת מטבח",
        "category": "מטבח",
        "barcode": "7290106441231",
        "price": 10.90,
        "quantity": 1,
        "image": "images/max_stock/7290106441231.jpg"
    },
    {
        "id": "ms_18",
        "store": "מקס סטוק",
        "storeKey": "max_stock",
        "name": "סל נייר דגם שיש",
        "category": "לבית",
        "barcode": "9720000483207",
        "price": 10.00,
        "quantity": 1,
        "image": "images/max_stock/9720000483207.jpg"
    },
    {
        "id": "ms_19",
        "store": "מקס סטוק",
        "storeKey": "max_stock",
        "name": "דיספנסר לסבון דגם שיש",
        "category": "אמבטיה",
        "barcode": "7299999105664",
        "price": 20.90,
        "quantity": 1,
        "image": "images/max_stock/7299999105664.jpg"
    },
    {
        "id": "ms_20",
        "store": "מקס סטוק",
        "storeKey": "max_stock",
        "name": "סל כביסה ענק 45 ליטר",
        "category": "לבית",
        "barcode": "7290003456475",
        "price": 59.00,
        "quantity": 1,
        "image": "images/max_stock/7290003456475.jpg"
    },
    {
        "id": "ms_21",
        "store": "מקס סטוק",
        "storeKey": "max_stock",
        "name": "אזיקונים 50 יחידות",
        "category": "כלי עבודה",
        "barcode": "9720000199191",
        "price": 5.90,
        "quantity": 1,
        "image": "images/max_stock/9720000199191.jpg"
    },
    {
        "id": "ms_22",
        "store": "מקס סטוק",
        "storeKey": "max_stock",
        "name": "מספריים אורטופדיים",
        "category": "כלי עבודה ולבית",
        "barcode": "6920902690663",
        "price": 5.00,
        "quantity": 1,
        "image": "images/max_stock/6920902690663.jpg"
    },
    {
        "id": "ms_23",
        "store": "מקס סטוק",
        "storeKey": "max_stock",
        "name": "מברג שטוח",
        "category": "כלי עבודה",
        "barcode": "7299998849088",
        "price": 3.90,
        "quantity": 1,
        "image": "images/max_stock/7299998849088.jpg"
    },
    {
        "id": "ms_24",
        "store": "מקס סטוק",
        "storeKey": "max_stock",
        "name": "מברג פיליפס (צלב)",
        "category": "כלי עבודה",
        "barcode": "7299998849071",
        "price": 3.90,
        "quantity": 1,
        "image": "images/max_stock/7299998849071.jpg"
    },
    {
        "id": "ms_25",
        "store": "מקס סטוק",
        "storeKey": "max_stock",
        "name": "מאג זכוכית שקופה 350 מ\"ל",
        "category": "מטבח",
        "barcode": "7299999111399",
        "price": 3.90,
        "quantity": 1,
        "image": "images/max_stock/7299999111399.jpg"
    },
    {
        "id": "ms_26",
        "store": "מקס סטוק",
        "storeKey": "max_stock",
        "name": "סלוטייפ סט 8 יחידות",
        "category": "לבית",
        "barcode": "6920902623357",
        "price": 5.00,
        "quantity": 1,
        "image": "images/max_stock/6920902623357.jpg"
    },
    {
        "id": "ms_27",
        "store": "מקס סטוק",
        "storeKey": "max_stock",
        "name": "מסחטת לימון ידנית מזכוכית",
        "category": "מטבח",
        "barcode": "7299999188643",
        "price": 10.90,
        "quantity": 1,
        "image": "images/max_stock/7299999188643.jpg"
    },
    {
        "id": "ms_28",
        "store": "מקס סטוק",
        "storeKey": "max_stock",
        "name": "קערית נירוסטה 24 ס\"מ",
        "category": "מטבח",
        "barcode": "7299998937952",
        "price": 10.00,
        "quantity": 1,
        "image": "images/max_stock/7299998937952.jpg"
    }
]

sum_rl = round(sum(x["price"] for x in rami_levy_items), 2)
sum_ms = round(sum(x["price"] for x in max_stock_items), 2)
total = round(sum_rl + sum_ms, 2)

print(f"Rami Levy items count: {len(rami_levy_items)}, Sum: {sum_rl:.2f} (Expected: 414.40)")
print(f"Max Stock items count: {len(max_stock_items)}, Sum: {sum_ms:.2f} (Expected: 380.50)")
print(f"Total Sum: {total:.2f} (Expected: 794.90)")

all_items = rami_levy_items + max_stock_items

# Check image file existence
import os
missing_images = []
for it in all_items:
    if not os.path.exists(it["image"]):
        missing_images.append(it["image"])

if missing_images:
    print(f"ERROR: {len(missing_images)} images missing: {missing_images}")
else:
    print("ALL 61 IMAGES EXIST ON DISK!")

# Export to data.js
js_content = f"""// רשימת כל המוצרים משתי הקבלות (רמי לוי ומקס סטוק)
// סה"כ רמי לוי: 414.40 ₪ (33 פריטים)
// סה"כ מקס סטוק: 380.50 ₪ (28 פריטים)
// סה"כ כולל: 794.90 ₪ (61 פריטים)

const PRODUCTS_DATA = {json.dumps(all_items, ensure_ascii=False, indent=2)};

const STORE_TOTALS = {{
  rami_levy: 414.40,
  max_stock: 380.50,
  total: 794.90
}};
"""

with open("data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("data.js written successfully!")
