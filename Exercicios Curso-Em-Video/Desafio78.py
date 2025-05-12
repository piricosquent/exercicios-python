#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual o menor e o maior valor e suas respectivas posições na lista.
listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input('Digite um número:')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('-='*30)
print(f'O maior número digitado foi {mai}, nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end='')
print(f'\nO menor número digitado foi {men}, nas posições ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')

