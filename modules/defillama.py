import requests

def get_top_defi_protocols(limit=10):
    """
    Получает топ DeFi-протоколов с TVL (total value locked).
    """
    url = "https://api.llama.fi/protocols"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # Возвращаем только первые `limit` протоколов
            return data[:limit]
        else:
            print("Ошибка запроса к DeFiLlama:", response.status_code)
            return []
    except Exception as e:
        print("Ошибка подключения к DeFiLlama:", e)
        return []
