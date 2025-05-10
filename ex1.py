def calcular_resistencia_aerobica(nome, idade, nbcr, nbca):
    media = (nbcr * 3 + nbca * 5) / 10
    if media <= 70:
        fator = 3
    elif media <= 100:
        fator = 2
    else:
        fator = 1
    condicionamento_aerobico = fator * idade
    return condicionamento_aerobico
n = str(input('Qual o nome ?'))
i = int(input('Qual a idade?'))
nbr = int(input('NBCR ?'))
nba = int(input('NBCA ?'))
resultado = calcular_resistencia_aerobica(n, i, nbr, nba)
print('O condicionamento aeróbico de {} é {}'.format(n, resultado))
