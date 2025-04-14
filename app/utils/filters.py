def filter_testnets(data):
    """
    Оставляет только те элементы, которые содержат ключевые слова в названии или URL.
    """
    keywords = ['testnet', 'faucet', 'airdrop', 'quest', 'campaign', 'layer3', 'lens', 'guild', 'zora', '0g', 'monad']
    filtered = []

    for item in data:
        text = f"{item.get('title', '').lower()} {item.get('url', '').lower()}"
        if any(keyword in text for keyword in keywords):
            filtered.append(item)

    return filtered
