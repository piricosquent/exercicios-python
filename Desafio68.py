from random import randint
print('\033[1;36m='*40)
print(f'{"Par ou ímpar":=^40}')
print('='*40, '\033[m')
v = 0
while True:
    jogador = int(input('Digite um número:'))
    computador = randint(0, 11)
    tipo = ' '
    total = jogador + computador
    while tipo not in 'IP':
        tipo = str(input('Par ou ímpar?[P/I]')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador jogou {computador}. Total de {total}.')
    if tipo == 'P':
        if total % 2 == 0:
            print('Jogador venceu.')
            v += 1
        else:
            print('Jogador perdeu.')
            break
    if tipo == 'I':
        if total % 2 == 0:
            print('Jogador perdeu.')
            break
        else:
            print('Jogador venceu.')
            v += 1
print(f'GAME OVER. Voce vendeu a máquina {v} vezes antes de perder.')