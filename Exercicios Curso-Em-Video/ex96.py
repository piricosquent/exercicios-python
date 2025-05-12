import time
def linhas():
    print('\033[34m-\033[0m'*30)
def area():
    a = float(input('Primeiramente, preciso do valor da largura:'))
    b = float(input('Agora, o valor do comprimento:'))
    valor = a*b
    time.sleep(0.5)
    print('.'.center(29))
    time.sleep(0.5)
    print('.'.center(31))
    time.sleep(0.5)
    print('.'.center(29))
    time.sleep(0.5)
    print('.'.center(31))
    time.sleep(0.5)
    linhas()
    print('...só um momento...'.center(30))
    linhas()
    time.sleep(0.5)
    print('.'.center(29))
    time.sleep(0.5)
    print('.'.center(31))
    time.sleep(0.5)
    print('.'.center(29))
    time.sleep(0.5)
    print('.'.center(31))
    time.sleep(0.5)
    print('\033[37m' + f'RESULTADO: {a} x {b} = {valor}u.a.²' + '\033[0m')



linhas()
print('\033[37m' + 'CALCULANDO ÁREAS'.center(30) + '\n' + 'COM PYTHON'.center(30) + '\033[0m')
linhas()
print('Vamos calcular áreas?')
while True:
    area()
    resp = input('Quer continuar?').upper()
    if resp in 'NNAONÃOÑ':
        break