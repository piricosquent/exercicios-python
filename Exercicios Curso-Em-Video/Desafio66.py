cont = soma = 0
print('Digite números inteiros para que o computador faça a soma.\nPara finalizar a soma e ver o resultado digite 999.')
while True:
    num = int(input(f'Digite o {cont + 1}º número:'))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Ao todo foram digitados {cont} números, e a soma deles é igual a {soma}.')
