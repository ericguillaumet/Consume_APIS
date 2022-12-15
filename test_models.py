from crypto_exchange.models import AllCoinsApiIO, Exchange, ModelError
from config import apiKey
#16156 cripto
#16378 no cripto (222 diferencia)

def test_allcoin():
    all = AllCoinsApiIO()
    assert isinstance(all, AllCoinsApiIO)
    all.getCoins(apiKey)
    assert len(all.cryptos) == 16156
    assert len(all.no_cryptos) == 222

def test_exchange_ok():
    cambio = Exchange("ETH")
    assert cambio.rate is None#True
    assert cambio.time is None#True
    cambio.updateExchange(apiKey)
    assert cambio.rate > 0
    assert isinstance(cambio.time,str)
    
def test_cambio_no_ok():
    not_ok = Exchange("NADA")
    #Conseguir comparar Resultado de la clase ModelError, consultar como lo hicimos en romanos
    #Assert not_ok.updateExchange(apiKey) ==  ModelError( f"status: {noOk.r.status_code} error: {noOk.resultado['error']} ")