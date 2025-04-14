import requests
from bs4 import BeautifulSoup

def get_cryptorank_testnets():
    """
    Парсит CryptoRank Drophunting и возвращает проекты с пометкой Testnet.
    """
    url = "https://cryptorank.io/ru/drophunting"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print("Ошибка при запросе к CryptoRank:", response.status_code)
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        testnets = []

        items = soup.find_all("div", class_="airdrop-item__content")

        for item in items:
            title_tag = item.find("div", class_="airdrop-item__title")
            tags = item.find_all("div", class_="airdrop-item__tag")
            link_tag = item.find_parent("a")

            if not title_tag or not link_tag:
                continue

            title = title_tag.get_text(strip=True)
            link = "https://cryptorank.io" + link_tag["href"]
            tag_texts = [t.get_text(strip=True).lower() for t in tags]

            if "тестнет" in tag_texts or "testnet" in tag_texts:
                testnets.append({
                    "name": title,
                    "url": link,
                    "tags": tag_texts
                })

        return testnets

    except Exception as e:
        print("Ошибка при парсинге CryptoRank:", e)
        return []
