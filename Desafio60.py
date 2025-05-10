print('\033[1;35m-=-\033[m'*6)
print('\033[36mF A T O R I A L\nD O   M I N A S\033[m')
print('\033[1;35m-=-\033[m'*6)
num = int(input('\033[1;34mDigite um número:\033[m'))
print(f'\033[35mO fatorial de {num} é :\033[m')
i = num
from math import factorial
resp = factorial(num)
from time import sleep
while num > 0:
    print(f'{num}', end=' ')
    if num != 1:
        print('x', end=' ')
    else:
        print('=', end=' ')
    num -= 1

print(resp)
