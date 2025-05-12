#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
#guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
pessoas = list()
dados = list()
men = mai = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        men = mai = dados[1]
    if dados[1] > mai:
        mai = dados[1]
    if dados[1] < men:
        men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = input('Deseja continuar?[S/N]: ').lower()
    if resp in 'nao':
        break
print('=-'*30)
print(f'Você cadastrou {len(pessoas)} pessoas.')
print(f'O menor peso foi de {men}Kg.', 'Foi o peso de: ', end=' ')
for c in pessoas:
    if c[1] == men:
        print(f'{c[0]}', end=' ')
print()
print(f'O maior peso foi de {mai}Kg. Foi o peso de: ', end=' ')
for c in pessoas:
    if c[1] == mai:
        print(f'{c[0]}', end=' ')