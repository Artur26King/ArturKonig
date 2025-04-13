import requests
from bs4 import BeautifulSoup

def get_incrypted_testnets():
    """
    Парсит страницу airdrops на incrypted.com и извлекает названия проектов и ссылки.
    """
    url = "https://incrypted.com/airdrops/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print("Ошибка при запросе:", response.status_code)
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        testnets = []

        # Ищем все блоки со статьями (карточки)
        articles = soup.find_all("article")

        for art in articles:
            title_tag = art.find("h2")
            link_tag = art.find("a", href=True)

            if title_tag and link_tag:
                title = title_tag.get_text(strip=True)
                link = link_tag["href"]

                testnets.append({
                    "name": title,
                    "url": link,
                    "tags": ["airdrop"]
                })

        return testnets

    except Exception as e:
        print("Ошибка при парсинге Incrypted:", e)
        return []
