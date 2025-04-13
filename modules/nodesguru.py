import requests
from bs4 import BeautifulSoup

def get_nodesguru_testnets():
    """
    Парсит главную страницу nodes.guru и возвращает список активных тестнетов.
    """
    url = "https://nodes.guru"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        testnets = []

        # Поиск таблицы тестнетов
        table = soup.find("table", {"class": "table"})
        if not table:
            print("Не найдена таблица с тестнетами на nodes.guru")
            return []

        rows = table.find_all("tr")[1:]  # Пропускаем заголовок таблицы

        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 2:
                name = cols[0].get_text(strip=True)
                link_tag = cols[0].find("a", href=True)
                href = url + link_tag["href"] if link_tag else url
                testnets.append({"name": name, "url": href})

        return testnets

    except Exception as e:
        print("Ошибка при запросе к Nodes.Guru:", e)
        return []
