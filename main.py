from modules.coingecko import get_top_coins
from modules.defillama import get_top_defi_protocols
from modules.rpcinfo import get_rpc_chains
from modules.testnet_faucet import get_testnets_from_faucet
from modules.rpc_info import get_rpc_networks
from modules.incrypted import get_incrypted_testnets
from modules.cryptorank import get_cryptorank_testnets
from modules.airdropalert import get_airdropalert_testnets
from modules.partnerkin import get_partnerkin_testnets
from modules.testnet_help import get_testnet_help_links
from modules.nodesguru import get_nodesguru_testnets
from modules.dropsearn import get_dropsearn_testnets
from modules.galxe import get_galxe_testnets
from modules.coinmarketcap import get_coinmarketcap_testnets
from modules import partnerkin

def main():
    coins = get_top_coins(limit=10)

    print("🧪 Найденные тестнеты с Partnerkin:")
    for item in partnerkin.get_partnerkin_testnets():
        print(f"- {item['title']}: {item['url']}")

    print("\n🧪 Найденные тестнеты с Galxe:")
    galxe = get_galxe_testnets()
    for quest in galxe:
        print(f"- {quest['title']}: {quest['url']}")


    print("\n🧪 Найденные тестнеты с DropsEarn:")
    drops = get_dropsearn_testnets()
    for d in drops:
        print(f"- {d['name']}: {d['url']}")


    print("\n🧪 Найденные тестнеты с Nodes.Guru:")
    guru = get_nodesguru_testnets()
    for net in guru:
        print(f"- {net['name']}: {net['url']}")


    print("\n🧪 Найденные тестнеты с Testnet Help Hub:")
    testnet_help_links = get_testnet_help_links()
    for link in testnet_help_links:
        print(f"- {link['name']}: {link['url']}")

    print("\n🧪 Найденные тестнеты с Partnerkin:")
    testnets = get_partnerkin_testnets()
    for t in testnets:
        print(f"- {t['name']}: {t['url']}")


    print("\n🧪 Найденные тестнеты с AirdropAlert:")
    airdrops = get_airdropalert_testnets()
    for drop in airdrops:
        print(f"- {drop['name']}: {drop['url']}")


    print("\n🧪 Найденные тестнеты с CryptoRank.io:")
    drops = get_cryptorank_drops()
    for drop in drops:
        print(f"- {drop['name']}: {drop['url']}")


    print("\n🧪 Найденные тестнеты с incrypted.com:")
    testnets = get_incrypted_testnets()
    for t in testnets:
        print(f"- {t['name']}: {t['url']}")


    print("\n🌐 Сети с сайта rpc.info:")
    networks = get_rpc_networks()
    for net in networks[:10]:  # показываем только первые 10
        print(f"- {net['name']}: {net['type']}")


    print("\n📡 Найденные тестнеты с сайта testnet-faucet.com:")
    testnets = get_testnets_from_faucet()
    for t in testnets[:10]:  # Показываем первые 10 для примера
        print(f"- {t['name']}: {t['url']}")


    print("\nСписок доступных сетей с RPC (первые 10):")
    rpc_chains = get_rpc_chains()
    for chain in rpc_chains[:10]:
        name = chain.get('name')
        chain_id = chain.get('chainId')
        rpc_list = chain.get('rpc', [])
        rpc_url = rpc_list[0] if rpc_list else 'Нет RPC'
        print(f"{name} (Chain ID: {chain_id}) → RPC: {rpc_url}")


    print("\nТоп 10 DeFi-протоколов по TVL:")
    defi_protocols = get_top_defi_protocols(limit=10)
    for protocol in defi_protocols:
        name = protocol['name']
        tvl = protocol['tvl']
        print(f"{name}: TVL = ${tvl:,.2f}")


    print("Топ 10 криптовалют по рыночной капитализации:")
    for coin in coins:
        name = coin['name']
        symbol = coin['symbol'].upper()
        price = coin['current_price']
        market_cap = coin['market_cap']
        print(f"{name} ({symbol}) — Цена: ${price} | Капитализация: ${market_cap}")

def collect_all_testnet_data():
    all_testnets = []

    try:
        from modules import partnerkin, cryptorank, incrypted, airdropalert, coinmarketcap, galxe, dropsearn
        all_testnets += partnerkin.get_partnerkin_testnets()
        all_testnets += cryptorank.get_cryptorank_testnets()
        all_testnets += incrypted.get_incrypted_testnets()
        all_testnets += airdropalert.get_airdropalert_testnets()
        all_testnets += coinmarketcap.get_coinmarketcap_testnets()
        all_testnets += galxe.get_galxe_testnets()
        all_testnets += dropsearn.get_dropsearn_testnets()

        filtered_testnets = filter_testnets(all_testnets)
        return filtered_testnets



    except Exception as e:
        print(f"❌ Ошибка при сборе тестнетов: {e}")

    return all_testnets


if __name__ == "__main__":
    main()
