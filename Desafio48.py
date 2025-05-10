#soma dos numeros impares divisiveis por 3 de 0 a 500
print('Defina o intervalo:')
n1 = int(input('A soma vai de:'))
n2 = int(input('Até:')) + 1
cont = 0
soma = 0
for c in range(n1, n2):
    if c%2 == 1 and c%3 == 0:
        soma = soma + c
        cont = cont + 1
print('A soma dos números impares divisíveis por três no intervalo de {} a {} é {}. E nesse intervalo temos {} números.'.format(n1, n2 - 1, soma, cont))

