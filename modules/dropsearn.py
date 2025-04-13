import requests
from bs4 import BeautifulSoup

def get_dropsearn_testnets():
    """
    Парсит https://dropsearn.com/testnets/ и возвращает список тестнетов.
    """
    url = "https://dropsearn.com/testnets/"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        items = soup.find_all("a", class_="project-link")
        results = []

        for item in items:
            name = item.get_text(strip=True)
            href = "https://dropsearn.com" + item.get("href")
            results.append({"name": name, "url": href})

        return results

    except Exception as e:
        print("Ошибка при запросе к DropsEarn:", e)
        return []
