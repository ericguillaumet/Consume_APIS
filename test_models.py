from crypto_exchange.models import AllCoinsApiIO
from config_apikey import apiKey
#16156 cripto
#16378 no cripto (222 diferencia)

def test_allcoin():
    all = AllCoinsApiIO()
    assert isinstance(all, AllCoinsApiIO)
    all.getCoins(apiKey)
    assert len(all.cryptos) == 16156
    assert len(all.no_cryptos) == 222