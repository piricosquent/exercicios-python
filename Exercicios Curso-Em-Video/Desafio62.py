print('Gerador de P.A')
print('-='*10)
primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão da P.A:'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer?'))
print('FIM')
print(f'Progressão finalizada com {total} termos.')