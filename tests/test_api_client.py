import pytest
from unittest.mock import patch
from src.api_client import buscar_dados

@patch("src.api_client.requests.get")
def test_buscar_dados_sucesso(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"msg": "ok"}
    resultado = buscar_dados("http://fakeurl.com")
    assert resultado == {"msg": "ok"}

@patch("src.api_client.requests.get")
def test_buscar_dados_falha(mock_get):
    mock_get.return_value.status_code = 404
    with pytest.raises(ConnectionError):
        buscar_dados("http://fakeurl.com")
