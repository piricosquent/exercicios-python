from Quiz.modulos import *
from random import randint
cont = 0
cabecalho('Roleta Russa')
limite = sorteio_escolha('Digite o limite do sorteio:')
numero_sorteado = randint(0, limite)
while True:
    cont += 1
    numero_escolhido = sorteio_escolha(f'De 0 a {limite}, qual número você acha que a máquina sorteou?')
    if numero_escolhido == numero_sorteado:
        cabecalho(f'{cor(2)}ACERTOU !!!{cor(0)}')
        print(f'Você é incrível, acertou na {cont}ª tentativa!')
        dormir()
        cabecalho(f'\t{cor(4)}Finalizando o programa...\n\t\tAté logo...{cor(0)}')
        break
    elif numero_escolhido > numero_sorteado:
        linhas()
        print(f'{cor(1)}QUASE! Tente um número menor.{cor(0)}')
    else:
        linhas()
        print(f'{cor(1)}Quase! Tente um número maior.{cor(0)}')



