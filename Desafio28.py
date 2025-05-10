import random
from time import sleep
print('='*25)
print('   Jogo da adivinhação')
print('='*25)
escolhido = int(input('Escolha um número entre 0 e 5:'))
print('Pensando . . .')
sleep(0.5)
sorteado = random.randint(0, 5)
if escolhido == sorteado:
    print('Ganhou!')
else:
    print('Perdeu!')