print('\033[33m-=\033[m'*10)
print('\033[35m-=-P.A Do mineiro=-=')
print('\033[33m-=\033[m'*10)
primeiro = int(input('Digite um número qualquer:'))
termo = primeiro
razao = int(input('Agora, dê a razão da P.A:'))
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo = termo + razao
    cont = cont + 1
print('Fim')