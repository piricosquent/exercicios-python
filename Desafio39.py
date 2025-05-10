nome = str(input('Nome do jovem:'))
idade = int(input('Idade:'))
if idade == 18:
    print(f'{nome} está na época de alistamento.')
elif idade < 18:
    print(f'Ainda falta(m) {18 - idade} ano(s) para {nome} se alistar.')
else:
    print(f'Já se passou/passaram {idade - 18} ano(s) da época de {nome} se alistar.')
print('\033[4;31mProcesso finalizado.\033[m')