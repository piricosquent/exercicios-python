#095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
#incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
#093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#O programa vai ler o nome do jogador e quantas partidas ele jogou.
#Depois vai ler a quantidade de gols feitos em cada partida.
#No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
dados = dict()
lista = list()
golnapartida = list()
while True:
    totgol = 0
    golnapartida.clear()
    dados['nome'] = str(input('Qual o nome do jogador ?')).title()
    dados['partidas'] = int(input(f'Quantas partidas o jogador {dados["nome"]} jogou?'))
    print(f'Quantos gols o jogador {dados["nome"]} marcou ', end='')
    for c in range(0, dados['partidas']):
        golnapartida.append(int(input(f'Na {c + 1}ª partida?')))
    dados['gol'] = golnapartida[:]
    totgol = sum(dados['gol'])
    dados['totgol'] = totgol
    lista.append(dados.copy())
    resp = str(input('Deseja continuar?[S/N]')).upper()[0]
    if resp not in 'SN':
        print('Erro. Digite S ou N.')
        resp = str(input('Deseja continuar?[S/N]')).upper()[0]
    if resp in 'Nn':
        break
print('-='*25)
for jogador in lista:
    print(f'O jogador {jogador["nome"]} marcou {jogador["totgol"]} gols no campeonato.')
print('')
print('-='*30)
resp = str(input('Deseja mostrar o rendimento de algum jogador em específico [S/N] ?')).upper()
while resp not in 'NS':
    print('ERRO. Digite apenas S ou N!')
    resp = str(input('Deseja mostrar o rendimento de algum jogador em específico [S/N] ?')).upper()
    if resp == 'S':
        nome = str(input('Digite o nome do jogador:')).title()
    for jogador in lista:
        if jogador['nome'] == nome:
            print(f'O jogador {jogador["nome"]} marcou ao todo {jogador["totgol"]} gols, sendo ')
            for c in range(0, len(jogador["gol"])):
                print(f'{jogador["gol"][c]} gol(s) na {c + 1}ª partida')
                print('')
