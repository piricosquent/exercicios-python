import requests

def verificar_site(url):
    try:
        resposta = requests.get(url, timeout=5)  # timeout evita travamentos longos
        if resposta.status_code == 200:
            print(f'O site {url} está acessível ✅')
        else:
            print(f'O site {url} respondeu com status {resposta.status_code} ⚠️')
    except requests.exceptions.RequestException as erro:
        print(f'O site {url} não está acessível ❌')
        print(f'Erro: {erro}')

# Exemplo de uso
verificar_site('https://www.google.com')
verificar_site('https://www.pudim.com.br')
