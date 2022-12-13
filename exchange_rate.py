import requests

r = requests.get('https://rest.coinapi.io/v1/exchangerate/ETH/EUR?apikey=805F252E-DE6E-4755-98DC-4C480FDEFC18')

print(r.status_code)

print(r.text)
