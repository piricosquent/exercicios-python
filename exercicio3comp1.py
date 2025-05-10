import math
def fatorial(n):
    a = math.factorial(n)
    return a
def potencia(x, n):
    b = x**n
    return b
n = int(input('Digite o número "n":'))
x = int(input('Digite o número "x":'))
fat = fatorial(n)
pot = potencia(x, n)
k = fat/pot
print('(a) = {}\n(b) = {}\n(c) = {}'.format(fat, pot, k))

