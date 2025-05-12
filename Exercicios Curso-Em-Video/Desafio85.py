#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos
#e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
#No final, mostre os valores pares e ímpares em ordem crescente.
lista = [[], []]
valor = 0
for c in range(0, 7):
    valor = int(input('Digite um número:'))
    if valor % 2 == 0:
        lista[0].append(valor)
    if valor % 2 != 0:
        lista[1].append(valor)
print('=-'*30)
lista[0].sort()
lista[1].sort()
print(f'Números pares digitados: {lista[0]}.')
print(f'Números ímpares digitados: {lista[1]}.')