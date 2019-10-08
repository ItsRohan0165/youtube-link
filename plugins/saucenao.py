import requests

def getSauce(image, API_KEY):
    url = 'https://saucenao.com/search.php?db=999&output_type=2&testmode=1&numres=16&api_key=' + API_KEY + '&url=' + image

    try:
        response = requests.get(url)
        data = response.json()

        if data['header']['status'] != 0 or 'anidb_aid' not in data['results'][0]['data']:
            return None

        return data['results'][0]['data']

    except:
        return None