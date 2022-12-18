#VIEWS: Todo lo que interactúe con el usuario


class Views():
    def __init__(self):
        pass

    def insertCoin(self):
        crypto = input("Introduce a fiat: ").upper()
        return crypto

    def availableCoins(self, allcoin): #Lista de monedas disponibles
        print("The amount of crypto is: {} ,\
            the amount of fiat is: {}"\
            .format(len(allcoin.cryptos),len(allcoin.no_cryptos)))

    def getRateExchange(self, exchange):
        print( "{:,.8f}€".format(exchange.rate).replace(",","@").replace(".",",").replace("@",".") )

    def getError(self, error):
        print(error) 