#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#Guarde esses resultados em um dicionário em Python.
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador 1 ': randint(1, 6),
        'Jogador 2 ': randint(1, 6),
        'Jogador 3 ': randint(1, 6),
        'Jogador 4 ': randint(1, 6)
}
for jogador, resultado in jogo.items():
    print(f'{jogador} tirou {resultado}.')
    sleep(0.5)
print('-='*20)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for indicelista, valortupla in enumerate(ranking):
    print(f'{indicelista + 1}º {valortupla[0]} com {valortupla[1]} pontos.')
    sleep(0.25   )