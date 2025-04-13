import requests
from bs4 import BeautifulSoup

def get_airdropalert_testnets():
    """
    Парсит статью с тестнетами на airdropalert.com и вытаскивает ссылки и названия.
    """
    url = "https://airdropalert.com/ru/блоги/список-тестнетов-airdrops-2025/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print("Ошибка при запросе к AirdropAlert:", response.status_code)
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        testnets = []

        # Ищем все ссылки внутри статьи
        content = soup.find("div", class_="blog-single__content")
        if not content:
            print("Не найден основной блок статьи")
            return []

        links = content.find_all("a", href=True)

        for link in links:
            title = link.get_text(strip=True)
            href = link["href"]
            if "http" in href and len(title) > 4:
                testnets.append({
                    "name": title,
                    "url": href,
                    "source": "airdropalert"
                })

        return testnets

    except Exception as e:
        print("Ошибка при парсинге AirdropAlert:", e)
        return []
