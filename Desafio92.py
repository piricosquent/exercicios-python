#092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
#Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
dados = dict()
print('~='*15)
print(f'{"INSS":~^30}')
print('~='*15)
dados['Nome'] = str(input('Nome:')).title()
anonascimento = int(input('Ano de nascimento:'))
dados['Idade'] = datetime.now().year - anonascimento
dados['Ctps'] = int(input('Número carteira de trabalho:'))
if dados['Ctps'] != 0:
    anocontratacao = int(input('Ano de contratação:'))
    dados['Aposentadoria'] = anocontratacao - anonascimento + 35
for k, v in dados.items():
    print(f'{k} tem o valor {v}.')