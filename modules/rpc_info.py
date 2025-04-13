import requests
from bs4 import BeautifulSoup

def get_rpc_networks():
    """
    Парсит сайт rpc.info и возвращает список сетей с их типом (Mainnet/Testnet).
    """
    url = "https://rpc.info/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print("Ошибка при получении страницы:", response.status_code)
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        networks = []

        # Ищем заголовки h2 — названия сетей
        network_headers = soup.find_all("h2")
        for header in network_headers:
            network_name = header.get_text(strip=True)
            ul = header.find_next_sibling("ul")
            if ul:
                for li in ul.find_all("li"):
                    network_type = li.get_text(strip=True)
                    networks.append({
                        "name": network_name,
                        "type": network_type
                    })

        return networks

    except Exception as e:
        print("Ошибка при парсинге rpc.info:", e)
        return []
