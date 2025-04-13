import requests
from bs4 import BeautifulSoup

def get_testnets_from_faucet():
    """
    Парсит сайт testnet-faucet.com и возвращает список тестнетов с их кранами.
    """
    url = "https://testnet-faucet.com"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print("Ошибка при получении страницы:", response.status_code)
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        faucet_list = []

        # Каждый тестнет находится в карточке сайта (обычно тег <a> внутри <div>)
        links = soup.find_all("a", class_="card")

        for link in links:
            name = link.get_text(strip=True)
            href = link.get("href")
            full_url = f"{url}{href}" if href.startswith("/") else href
            faucet_list.append({"name": name, "url": full_url})

        return faucet_list

    except Exception as e:
        print("Ошибка при парсинге testnet-faucet.com:", e)
        return []
