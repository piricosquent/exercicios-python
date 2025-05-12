from time import sleep
from random import choice
print('\033[1;36m{:-^40}\033[m'.format('Jo Ken Po'))
sleep(1)
print('\033[1;36m{:-^40}\033[m'.format('Round 1'))
print('''Escolha:
\033[1;36m[1]\033[mPedra
\033[1;36m[2]\033[mPapel
\033[1;36m[3]\033[mTesoura''')
jogador = int(input('\033[1;36m->\033[m '))
if jogador == 1:
    j = 'PEDRA'
elif jogador == 2:
    j = 'PAPEL'
elif jogador == 3:
    j = 'TESOURA'
lista_computador = ['PEDRA', 'PAPEL', 'TESOURA']
computador = choice(lista_computador)
print('\033[1;34m{:-^40}\033[m'.format('Jogador escolheu -> {}'.format(j)))
sleep(0.5)
print('\033[1;33m{:-^40}\033[m'.format('Computador escolheu -> {}'.format(computador)))
sleep(0.5)
if j == computador:
    print('\033[1;33m{:-^40}\033[m'.format('EMPATE'))
elif j == 'PEDRA' and computador == 'PAPEL':
    print('\033[1;31m{:-^40}\033[m'.format('COMPUTADOR WINS'))
elif j == 'PEDRA' and computador == 'TESOURA':
    print('\033[1;32m{:-^40}\033[m'.format('JOGADOR WINS'))
elif j == 'PAPEL' and computador == 'PEDRA':
    print('\033[1;32m{:-^40}\033[m'.format('JOGADOR WINS'))
elif j == 'PAPEL' and computador == 'TESOURA':
    print('\033[1;31m{:-^40}\033[m'.format('COMPUTADOR WINS'))
elif j == 'TESOURA' and computador == 'PEDRA':
    print('\033[1;31m{:-^40}\033[m'.format('COMPUTADOR WINS'))
elif j == 'TESOURA' and computador == 'PAPEL':
    print('\033[1;32m{:-^40}\033[m'.format('JOGADOR WINS'))
else:
    print('\033[1;31m{:-^40}\033[m'.format('OPÇÃO INVÁLIDA'))




