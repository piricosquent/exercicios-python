ano_atual = int(input('Em que ano estamos?'))
tot_maior = 0
tot_menor = 0
for c in range(0, 7):
    nome = str(input('Nome:'))
    ano_de_nascimento = int(input('Ano de nascimento:'))
    idade = ano_atual - ano_de_nascimento
    if idade >= 18:
        tot_maior += 1
    else:
        tot_menor += 1
print(f'Ao todo são {tot_maior} maiores e {tot_menor} menores.')