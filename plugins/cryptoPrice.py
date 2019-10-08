import requests

def getPrice(coin):
    url = "https://api.coinmarketcap.com/v1/ticker/" + coin
    response = requests.get(url)
    data = response.json()

    if "error" in data:
        return None

    return data[0]