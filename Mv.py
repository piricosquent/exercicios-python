lista = list()
mulheres = list()
totid = 0
while True:
    dados = dict()
    dados['nome'] = str(input('Digite o nome: '))
    dados['sexo'] = str(input('Sexo [H/M]: ')).upper()
    while dados['sexo'] not in 'HM':
        print('Erro. Tente novamente:')
        dados['sexo'] = str(input('Sexo [H/M]: ')).upper()
    dados['idade'] = int(input('Idade: '))

    # Se for mulher, adiciona à lista de mulheres
    if dados['sexo'] == 'M':
        mulheres.append(dados['nome'])

    # Adiciona os dados à lista principal
    lista.append(dados.copy())

    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break

# Calcula a soma das idades
for pessoa in lista:
    totid += pessoa['idade']

# Calcula a média das idades
mediaid = totid / len(lista) if len(lista) > 0 else 0

print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'Mulheres cadastradas: {mulheres}')
print(f'Todas as pessoas cadastradas: {lista}')
print(f'A média de idade é {mediaid:.2f}')
