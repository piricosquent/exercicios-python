import random
from time import sleep
tentativa = 1
computador = random.randint(0, 10)
jogador = int(input('\033[1;35mTente adivinhar o número sorteado pela máquina:\033[m\n \033[1;32m->\033[m'))
sleep(0.5)
print('\033[1;36mPensando\033[31m .\033[32m.\033[33m.\033[m')
sleep(0.5)
while jogador != computador:
    jogador = int(input('\033[1;31mErrou, tente novamente:\033[m\n \033[1;32m->\033[m'))
    print('\033[36mPensando ...\033[m')
    sleep(0.5)
    tentativa += 1
print(f'\033[1;32mParabéns, você acertou na {tentativa}º tentativa.\nFim do jogo.\033[m')