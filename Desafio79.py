#1º Lendo os valores e adicionando-os à lista:
numeros = list()
resp = ''
while True:
    if resp in 'SIM':
        num = int(input('Digite um número: '))
        if num in numeros:
            print('Número repetido.')
        else:
            print('Número adicionado com sucesso!')
            numeros.append(num)
        resp = input('Quer adicionar mais algum número?').strip().upper()
    else:
        break
numeros.sort()
print('=-'*30)
print(numeros)
print('Acabou')
