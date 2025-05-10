c = 0
num = 0
soma = 0
print('Somando com Python')
print('Digite os números que voce quer somas. Para finalizar, digite 999.')
while num != 999:
    num = int(input(f'{c + 1}º número:'))
    if num != 999:
        soma += num
        c += 1
print(f'A soma foi {soma}.\nAo todo foram somados {c} números.')
print('Fim. Obrigado.')
