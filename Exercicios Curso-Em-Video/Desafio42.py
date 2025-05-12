l1 = float(input('Digite o Lado 1:'))
l2 = float(input('Digite o Lado 2:'))
l3 = float(input('Digite o Lado 3:'))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('Estes lados podem formar um triângulo.')
    if l1 == l2 and l2 == l3:
        print('Triângulo EQUILÁTERO.')
    elif l1 != l2 and l2 != l3 and l3 != l1:
        print('Triângulo ESCALENO.')
    else:
        print('Triângulo ISÓSCELES.')
else:
    print('Estas retas não podem constituir um triângulo.')