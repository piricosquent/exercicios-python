#093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#O programa vai ler o nome do jogador e quantas partidas ele jogou.
#Depois vai ler a quantidade de gols feitos em cada partida.
#No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
dados = dict()
gol = list()
dados['Nome'] = str(input('Digite o nome do jogador:')).title()
partidas = int(input('Quantas partidas ele jogou no campeonato?'))
totgols = 0
for c in range(0, partidas):
    gols = int(input(f'Na {1 + c}ª partida ele marcou quantos gols ?'))
    gol.append(gols)
    totgols += gols
dados['gols'] = gol
dados['total'] = totgols
print('~='*25)
print(dados)
print('~='*25)
for key, value in dados.items():
    print(f'O campo {key} tem valor {value}.')
print('~='*25)
print(f'O jogador {dados["Nome"]} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'Na {c + 1}ª partida, marcou {gol[c]} gols.')
print(f'Ao todo marcou {dados["total"]} gols.')