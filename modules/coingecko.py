import requests

def get_top_coins(limit=10):
    """
    Получает топ криптовалют по рыночной капитализации.
    """
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": limit,
        "page": 1,
        "sparkline": False
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print("Ошибка запроса к CoinGecko:", response.status_code)
        return []
