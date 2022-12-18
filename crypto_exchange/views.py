#VIEWS: Todo lo que interactúe con el usuario


class Views():
    def __init__(self):
        pass

    def insertCoin(self):
        crypto = input("Introduce a crypto: ").upper()
        return crypto

    def availableCoins(self, allcoin): #Lista de monedas disponibles
        print("The amount of crypto is: {} ,\
            the amount of fiat is: {}"\
            .format(len(allcoin.cryptos),len(allcoin.no_cryptos)))

    def getRateExchange(self, exchange):
        print( "{:,.2f}€".format(exchange.rate).replace(",","@").replace(".",",").replace("@",".") )

    def getError(self, error):
        print(error) 