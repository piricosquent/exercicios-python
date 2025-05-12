frase = str(input('Digite um frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo.')
else:
    print('Nao é um palíndromo.')
