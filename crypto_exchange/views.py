#VIEWS: Todo lo que interactúe con el usuario


class Views():
    def __init__(self):
        pass

    def insertCoin():
        crypto = input("Introduce a crypto: ").upper()
        return crypto

    def availableCoins(allcoins):
        print("The amount of crypto is: {} ,\
            the amount of fiat is: {}"\
            .format(len(allcoins.cryptos),len(allcoins.no_cryptos)))

    def getRateExchange(exchange):
        print( "{:,.2f}€".format(exchange.rate).replace(",","@").replace(".",",").replace("@",".") )

    def getError(error):
        print(error)