import requests
from urllib.parse import quote

def getTranslation(t, input, API_KEY):
    base = 'https://translation.googleapis.com/language/translate/v2?'

    query = 'q=' + quote(input)
    print(t)
    if t =='ja':
        target = '&target=' + 'ja'
        source = '&source=' + 'en'
    else:
        target = '&target=' + 'en'
        source = '&source=' + 'ja'

    key = '&key=' + API_KEY
    url = base + query + target + source + key

    response = requests.get(url)
    data = response.json()
    return data['data']['translations'][0]['translatedText']