import urllib.request
import urllib.parse
import json

def get_wiki_img(q):
    url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(q)}&gsrnamespace=6&gsrlimit=3&prop=imageinfo&iiprop=url&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'ProductApp/1.0 (contact@example.com)'})
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            data = json.loads(r.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            for pid, pinfo in pages.items():
                img = pinfo.get('imageinfo', [{}])[0].get('url')
                if img and (img.endswith('.jpg') or img.endswith('.png')):
                    return img
    except Exception as e:
        print("err", e)
    return None

print("Lemon squeezer:", get_wiki_img("glass lemon squeezer"))
print("Broom:", get_wiki_img("broom cleaning"))
print("Screwdriver:", get_wiki_img("phillips screwdriver"))
print("Dish scrubber:", get_wiki_img("sponge dishwashing"))
