import requests
from bs4 import BeautifulSoup

def get_partnerkin_testnets():
    """
    Парсит статью с сайта partnerkin.com и достает названия и ссылки тестнетов.
    """
    url = "https://partnerkin.com/blog/stati/top-testnets-2025"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print("Ошибка при запросе к Partnerkin:", response.status_code)
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        testnets = []

        content = soup.find("div", class_="article_text")
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
                    "source": "partnerkin"
                })

        return testnets

    except Exception as e:
        print("Ошибка при парсинге Partnerkin:", e)
        return []
