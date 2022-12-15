from crypto_exchange.models import AllCoinsApiIO, Exchange, ModelError
from config import apiKey

#Creamos objeto de AllCoinApiIO
allcoins = AllCoinsApiIO()
#Ejecutar el metodo getCoins que consulta y carga lista de coins
allcoins.getCoins(apiKey)

print("La cantidad de criptos son {} ,\
       y la de no criptos son {}"\
      .format(len(allcoins.cryptos),len(allcoins.no_cryptos)))

crypto = input("Ingrese moneda digital conocida: ").upper()

while crypto != "" and crypto.isalpha():
    if crypto in allcoins.cryptos:
        exchange = Exchange(crypto)
        try:
            #Si todo va bien esto se ejecuta
            exchange.updateExchange(apiKey)
            print( "{:,.2f}€".format(exchange.rate).replace(",","@").replace(".",",").replace("@",".") )

        except ModelError as error:# Si falla imprime error
            print(error)    

    crypto = input("Ingrese moneda digital conocida: ").upper()