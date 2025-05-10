# Exercício  Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
dados = dict()

dados['Nome'] = str(input('Nome: ')).title()
dados['Media'] = float(input('Média: '))
print('-'*26)
for k, v in dados.items():
    print(f'{k:<12} : {v:>11}')
if dados['Media'] <= 5:
    print(f'{"REPROVADO":-^26}')
else:
    print(f'{"APROVADO":-^26}')
