lado1 = float(input('Digite o Lado 1:'))
lado2 = float(input('Digite o Lado 2:'))
lado3 = float(input('Digite o Lado 3:'))
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print('Estes lados podem formar um triângulo.')
else:
    print('Estas retas não podem constituir um triângulo.')