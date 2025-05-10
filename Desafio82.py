#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# #Ao final, mostre o conteúdo das três listas geradas.
numeros = []
impares = []
pares = []
while True:
    numeros.append(int(input('Digite um número:')))
    resp = input('Numero adicionado. Deseja continuar?[S/N]').strip().lower()
    if resp in 'n':
        break
for i, v in enumerate(numeros):
    if v%2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'Números digitados: {numeros}.')
print(f'Números impares digitados: {impares}.')
print(f'Números pares digitados: {pares}')