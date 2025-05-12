print('{:=^40}'.format('Olá'))
print('Vamos descobrir os números pares em um determinado intervalo.')
n1 = int(input('Defina o intervalo.\n De ->'))
n2 = int(input('Até ->')) + 1
for c in range(n1, n2):
    if c%2 == 0:
        print(c)
print('FIM')

