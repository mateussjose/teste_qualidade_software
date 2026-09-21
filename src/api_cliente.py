import requests

def buscar_dados(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise ConnectionError("Erro ao acessar API")
