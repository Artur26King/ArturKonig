import os
import json
import time
from app.utils.filters import filter_testnets
from main import collect_all_testnet_data


CACHE_PATH = os.path.join("data", "testnets.json")
CACHE_DURATION = 600  # 10 минут

def load_testnet_data():
    # Если файл существует и не устарел
    if os.path.exists(CACHE_PATH):
        last_modified = os.path.getmtime(CACHE_PATH)
        if time.time() - last_modified < CACHE_DURATION:
            with open(CACHE_PATH, "r", encoding="utf-8") as f:
                return json.load(f)

    # Загружаем новые данные
    data = collect_all_testnet_data()
    filtered = filter_testnets(data)

    with open(CACHE_PATH, "w", encoding="utf-8") as f:
        json.dump(filtered, f, ensure_ascii=False, indent=2)

    return filtered
