def ficha(nome='', gols=0):
    if not nome:
        nome = 'Sem Nome'
    try:
        gols = int(gols)
    except(ValueError, TypeError):
        gols = 0
    return f'O Jogador {nome} marcou {gols} gol(s).'


nome = input('Qual o nome do jogador?').strip().title()
gols = input(f'Quantos gols o jogador {nome or "Sem Nome"} marcou?').strip()
print(ficha(nome, gols))