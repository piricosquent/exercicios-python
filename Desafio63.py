print('Fibonacci')
num = int(input('Quantos números da sequência?'))
t1 = 0
t2 = 1
t3 = 0
c = 3
print(f'{t1} {t2}', end=' ')
while c <= num:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    c += 1
    print(t3, end=' ')
