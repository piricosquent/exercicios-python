maior = 0
menor = 0
for c in range(1, 6):
    idade = int(input(f'A idade da {c}ª pessoa:'))
    if c == 1:
        maior = idade
        menor = idade
    if idade > maior:
        maior = idade
    elif idade < menor:
        menor = idade

print(f'A menor idade é {menor}.')
print(f'A maior idade é {maior}.')