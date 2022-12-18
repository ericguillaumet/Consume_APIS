from crypto_exchange.models import AllCoinsApiIO, Exchange, ModelError
from crypto_exchange.views import Views
from config import apiKey

class CryptoExchangeController():

    def executeSoftware(self):

        #Creamos objeto de AllCoinApiIO
        allcoins = AllCoinsApiIO()
        #Ejecutar el metodo getCoins que consulta y carga lista de coins
        allcoins.getCoins(apiKey)

        viewsTool = Views()
        viewsTool.availableCoins(allcoins)
        crypto = viewsTool.insertCoin()

        while crypto != "" and crypto.isalpha():
            if crypto in allcoins.cryptos:
                exchange = Exchange(crypto)
                try:
                    #Si todo va bien esto se ejecuta
                    exchange.updateExchange(apiKey)
                    viewsTool.getRateExchange(exchange) 

                except ModelError as error:# Si falla imprime error
                    viewsTool.getError(error)

            crypto = viewsTool.insertCoin()