import requests
from bs4 import BeautifulSoup

def get_testnet_help_links():
    url = "https://testnet.help/setidioma.php?lang=ru"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        links = []
        for a_tag in soup.find_all("a", href=True):
            href = a_tag["href"]
            text = a_tag.get_text(strip=True)
            if "testnet" in href.lower():
                links.append({"name": text or href, "url": href})
        return links
    except Exception as e:
        print(f"Ошибка при запросе к Testnet Help Hub: {e}")
        return []
