#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os
#em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

numeros = []
for c in range(0, 5):
    n = int(input('Digite um valor:'))
    if c == 0 or n > numeros[-1]:
        numeros.append(n)
        print(f'O número {n} foi adicionado à última posição.')
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                print(f'O número {n} foi adicionado à {pos + 1}ª posição.')
                break
            pos += 1
print('=-'*20)
print(numeros)