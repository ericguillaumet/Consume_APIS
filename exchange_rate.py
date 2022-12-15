import requests
from config_apikey import apiKey

crypto_coin = input("Introduce a crypto: ").upper()

while  crypto_coin != "" and crypto_coin.isalpha():

    r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{crypto_coin}/EUR?apikey={apiKey}')

    #print(r.status_code)
 
    #print(r.text)

    #Ejercicio 1: como capturamos resultados correctos
    result = r.json() #guardamos r.json en resultado (diccionario en python)

    if r.status_code == 200:
        #value = round(result["rate"], 4)
        print("{:,.2f}€".format(result["rate"]).replace(',','.'))

    #Ejercicio 2: como capturamos errores

    else:
        print(result["error"])

    #Ejercico 3: como formateamos el valor rate // Hecho con format

    #Ejercicio 4: como controlo input vacio, que no realice consulta si el input está vacio // Con un while
    crypto_coin = input("Introduce a crypto: ").upper()