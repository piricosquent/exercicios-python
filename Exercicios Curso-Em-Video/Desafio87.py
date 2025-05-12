#Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = somac = mail = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'[{l},{c}]:'))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        if c == 2:
            somac = somac + matriz[l][c]
        if matriz[1][c] > mail:
            mail = matriz[1][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos números pare digitados foi: {soma}.')
print(f'A soma dos valores da terceira coluna for {somac}.')
print(f'O maior valor da segunda linha foi {mail}')