import requests
from config_apikey import apiKey

r = requests.get(f'https://rest.coinapi.io/v1/assets/?apikey={apiKey}') #Esta API me trae todas las monedas que hay

if r.status_code != 200:
    raise Exception( "Error in the enquiry of assets: {}".format(r.status_code))

general_list = r.json()
crypto_list = []

for item in general_list:
    if item["type_is_crypto"] == 1:
        crypto_list.append(item["asset_id"])

crypto_coin = input("Introduce a crypto: ").upper()

print("Crypto: ", len(crypto_list))
print("Crypto: ", len(general_list) - len(crypto_list))

while crypto_coin != "" and crypto_coin.isalpha():
    
    if crypto_coin in crypto_list:
        r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{crypto_coin}/EUR?apikey={apiKey}')
        result = r.json()

        if r.status_code == 200:
            print("{:,.2f}€".format(result["rate"]).replace(',','.'))
        else:
            print(result["error"])

    crypto_coin = input("Introduce a crypto: ").upper()