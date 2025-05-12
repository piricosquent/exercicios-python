somaidade = 0
media = 0
maioridadehomem = 0
totmenos20 = 0
nomevelho = ''

for p in range(1, 3):
    print('{:=>5}{:=<12}'.format(p, 'º pessoa'))
    nome = str(input('Nome:'))
    sexo = str(input('Sexo [M/F]:'))
    idade = int(input('Idade:'))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmenos20 += 1
media = somaidade/4
print(f'''O home mais velho se chama {nomevelho} e tem {maioridadehomem} anos.
A idade média do grupo é {media}.
E ao todo temos {totmenos20} mulheres com menos de 20 anos de idade.''')
