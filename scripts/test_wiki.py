import urllib.request
import urllib.parse
import json

def get_wikimedia_image(query):
    try:
        url = "https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch=" + urllib.parse.quote(query) + "&gsrlimit=1&prop=imageinfo&iiprop=url&format=json"
        req = urllib.request.Request(url, headers={'User-Agent': 'ProductFinder/1.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            for pid, pdata in pages.items():
                return pdata.get('imageinfo', [{}])[0].get('url')
    except Exception as e:
        print("Error:", e)
    return None

print("Glass lemon squeezer:", get_wikimedia_image("lemon squeezer glass"))
print("Cutlery tray:", get_wikimedia_image("cutlery tray drawer"))
print("Stainless steel bowl:", get_wikimedia_image("stainless steel mixing bowl"))
print("Laundry basket:", get_wikimedia_image("plastic laundry basket"))
