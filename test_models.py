from crypto_exchange.models import AllCoinsApiIO, Exchange, ModelError
from config import apiKey
import pytest
#16156 cripto
#16378 no cripto (222 diferencia)

def test_allcoin():
    all = AllCoinsApiIO()
    assert isinstance(all, AllCoinsApiIO)
    all.getCoins(apiKey)
    assert len(all.cryptos) == 16156
    assert len(all.no_cryptos) == 222

def test_exchange_ok():
    exchange = Exchange("ETH")
    assert exchange.rate is None#True
    assert exchange.time is None#True
    exchange.updateExchange(apiKey)
    assert exchange.rate > 0
    assert isinstance(exchange.time,str)
    
def test_cambio_not_ok():
    not_ok = Exchange("NOTHING_HERE")
    #Conseguir comparar Resultado de la clase ModelError, consultar como lo hicimos en romanos
    #Assert not_ok.updateExchange(apiKey) ==  ModelError( f"status: {not_ok.r.status_code} error: {noOk.resultado['error']} ")

    with pytest.raises(ModelError) as exceptionInfo:
        not_ok.updateExchange(apiKey)

    assert str(exceptionInfo.value) == "status: 550 error: You requested specific single item that we don't have at this moment."
 