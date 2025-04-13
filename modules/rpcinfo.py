import requests

def get_rpc_chains():
    """
    Получает список блокчейнов с сайта rpc.info
    """
    url = "https://raw.githubusercontent.com/DefiLlama/chainlist/main/constants/evm.json"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get("chains", [])
        else:
            print("Ошибка при запросе к RPC.info:", response.status_code)
            return []
    except Exception as e:
        print("Ошибка подключения к RPC.info:", e)
        return []
