import urllib.request
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'locale': 'he'
}

# Test Rami Levy API
try:
    url = "https://www.rami-levy.co.il/api/v2/site/clubs/search?q=9007829022023"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=5) as resp:
        print("Rami Levy API status:", resp.status)
        data = json.loads(resp.read().decode('utf-8'))
        print("Rami Levy API result keys:", list(data.keys()))
        if 'data' in data:
            print("Items found:", len(data['data']))
            if len(data['data']) > 0:
                print("Item 0:", data['data'][0].get('name'), data['data'][0].get('images'))
except Exception as e:
    print("Rami levy API error:", e)

# Test Shufersal API
try:
    url = "https://www.shufersal.co.il/online/he/search/results?q=7290003491124"
    # Or search query
except Exception as e:
    pass
