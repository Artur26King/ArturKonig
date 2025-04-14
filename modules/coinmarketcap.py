import requests
from bs4 import BeautifulSoup

def get_coinmarketcap_testnets():
    url = "https://coinmarketcap.com/airdrop/"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        airdrops = soup.find_all("a", class_="svowul-5 czQlor a")
        print("🧪 Найденные тестнеты с CoinMarketCap Airdrops:")
        found = False
        for drop in airdrops:
            name = drop.get_text(strip=True)
            link = "https://coinmarketcap.com" + drop.get("href", "")
            if "testnet" in name.lower():
                print(f"- {name}: {link}")
                found = True
        if not found:
            print("Не найдено тестнетов в активных airdrop'ах")
    except Exception as e:
        print("Ошибка при запросе к CoinMarketCap:", e)
