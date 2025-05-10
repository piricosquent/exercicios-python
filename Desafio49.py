n = int(input('''{:=^40}
Escolha um número:'''.format('TABUADA DO MINEIRO')))
for c in range(0, 11):
    r = n*c
    print(f'{n}x{c} = {r}')