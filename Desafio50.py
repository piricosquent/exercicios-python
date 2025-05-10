print('Somando números pares.')
soma = 2
for c in range(1, 7):
    n = int(input(f'Digite o {c}º número:'))
    if n%2 == 0:
        soma = soma + n
print(f'A soma dos valores pares digitados é {soma}')
