resp = 'S'
cont = 0
total = 0
maior = 0
menor = 0
while resp in 'Ss':
    número = int(input(f'Digite o {cont + 1}º número:'))
    resp = str(input('Quer continuar?[S/N]')).upper().strip()[0]
    cont += 1
    total += número
    if cont ==1:
        maior = menor = número
    else:
        if número > maior:
            maior = número
        if número < menor:
            menor = número
media = total/cont
print(f'Você digitou {cont} números, a média foi {media}. O maior número foi {maior} e o menor foi {menor}.')
