num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        tot += 1
        print('\033[32m', end=' ')
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end='')
print(f'\n\033[mO número {num} foi divisivel {tot} vezes.')
if tot == 2:
    print('E por isso ele é primo.')
else:
    print('E por isso ele não é primo.')