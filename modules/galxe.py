import requests
from bs4 import BeautifulSoup

def get_galxe_testnets():
    """
    Парсит https://galxe.com/quest и возвращает ссылки на квесты, связанные с тестнетами.
    """
    url = "https://galxe.com/quest"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        quests = []

        for a in soup.find_all("a", href=True):
            href = a["href"]
            text = a.get_text(strip=True)

            if "/quest/" in href and ("testnet" in href.lower() or "testnet" in text.lower()):
                full_url = "https://galxe.com" + href
                quests.append({"title": text or "Тестнет-квест", "url": full_url})

        return quests

    except Exception as e:
        print("Ошибка при запросе к Galxe:", e)
        return []
