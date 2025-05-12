#094: Crie um programa que leia nome,
#sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
#No final, mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média
lista = list()
mulheres = list()
menosmedia = list()
totid = 0
while True:
    dados = dict()
    dados['nome'] = str(input('Digite o nome:'))
    dados['sexo'] = str(input('Sexo [H/M]):')).upper()
    while dados['sexo'] not in 'HM':
        print('Erro. Tente novamente:')
        dados['sexo'] = str(input('Sexo [H/M]: ')).upper()
    dados['idade'] = int(input('Idade:'))
    if dados['sexo'] == 'M':
        mulheres.append(dados['nome'])
    lista.append(dados.copy())
    resp = str(input('Deseja continuar [S/N]?')).upper()
    while resp not in 'SN':
        print('Erro. Tente novamente.')
        resp = str(input('Deseja continuar[S/N]?')).upper()
    if resp in 'Nn':
        break
for pessoa in lista:
    totid += pessoa['idade']
mediaid = totid/len(lista) if len(lista) > 0 else 0
for pessoa in lista:
    if pessoa['idade'] < mediaid:
        menosmedia.append(pessoa['nome'])
print(f'Foram cadastradas {len(lista)} pessoas.')
print(mulheres)
print(lista)
print(mediaid)
print(menosmedia)