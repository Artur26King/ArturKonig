import requests
from bs4 import BeautifulSoup

def get_partnerkin_testnets():

    url = "https://partnerkin.com/ru/cat/crypto"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("a", href=True)

        testnets = []
        for link in links:
            href = link["href"]
            if any(sub in href for sub in ["testnet", "faucet", "quest", "airdrop", "campaign", "layer3", "guild", "mirror", "zora", "lens", "0g.ai", "monad"]):
                full_url = href if href.startswith("http") else f"https://partnerkin.com{href}"
                testnets.append({
                    "title": link.get_text(strip=True) or "Без названия",
                    "url": full_url,
                    "source": "partnerkin"
                })

        return testnets

    except Exception as e:
        print("Ошибка при парсинге Partnerkin:", e)
        return []
