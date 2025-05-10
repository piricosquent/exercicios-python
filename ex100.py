def sorteio(lista):
    for c in range(0, 5):
        lista.append(randint(0, 10))
def somapar():
    soma = 0
    for v in sorteados:
        print(v, end=' ')
        if v % 2 == 0:
            soma += v
    print('\nSoma:', soma)


#programa principal
from random import randint
sorteados = list()
sorteio(sorteados)
print()
somapar()
