import requests

class ModelError(Exception):
    pass

class AllCoinsApiIO: 
    def __init__(self):
        self.cryptos = []
        self.no_cryptos = []

    def getCoins(self, apiKey):
        r = requests.get(f'https://rest.coinapi.io/v1/assets/?apikey={apiKey}') #Esta API me trae todas las monedas que hay

        if r.status_code != 200:
            raise Exception( "Error in the enquiry of assets: {}".format(r.status_code))
        
        general_list = r.json()

        for item in general_list:
            if item["type_is_crypto"] == 1:
                self.cryptos.append(item["asset_id"])
            else:
                self.no_cryptos.append(item["asset_id"])

class Exchange:
    def __init__(self, crypto):
        self.crypto = crypto
        self.rate = None
        self.time = None
        self.r = None
        self.result = None

    def updateExchange(self, apiKey):
        self.r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{self.crypto}/EUR?apikey={apiKey}')
        self.result = self.r.json()

        if self.r.status_code == 200:
            self.rate = self.result ['rate']
            self.time = self.result ['time']

        else:
            raise ModelError(f"status: {self.r.status_code} error: {self.result['error']}")

class ExchangeFiatToBTC:
    def __init__(self, fiat):
        self.fiat = fiat
        self.rate = None
        self.time = None
        self.r = None
        self.result = None

    def updateExchange(self, apiKey):
        self.r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{self.fiat}/BTC?apikey={apiKey}')
        self.result = self.r.json()

        if self.r.status_code == 200:
            self.rate = self.result ['rate']
            self.time = self.result ['time']

        else:
            raise ModelError(f"status: {self.r.status_code} error: {self.result['error']}")