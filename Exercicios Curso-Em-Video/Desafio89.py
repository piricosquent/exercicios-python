#Exercício  Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
lista = list()
listamenor = list()
while True:
    nome = str(input('Digite o nome do aluno:'))
    listamenor.append(nome)
    nota1 = float(input('Digite a nota 1:'))
    listamenor.append(nota1)
    nota2 = float(input('Digite a nota 2:'))
    listamenor.append(nota2)
    lista.append(listamenor[:])
    listamenor.clear()
    resp = str(input('Deseja registrar mais algum aluno?[S/N]'))
    if resp in 'Nn':
        break
print('-='*30)
print(f'{"BOLETIM":^30}')
print(f'{"No":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for c, v in enumerate(lista):
    print(f'{c:<4}{v[0]:<10}{(v[1]+v[2])/2:>8}')
print('-='*30)
resp2 = input('Você deseja ver a nota de algum aluno em específico?[S/N]')
if resp2 in 'sS':
    while True:
        op = str(input('Qual aluno você deseja ?(999 encerra)'))
        if op == '999':
            break
        for cont, valor in enumerate(lista):
            if op in valor:
                print(lista[cont])

print('<<<<< ENCERRANDO >>>>>')

