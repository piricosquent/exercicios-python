import modulos


num = float(input('Digite o valor:'))
taxa_aumento = float(input('Digite a taxa de aumento (em porcentagem):'))
taxa_diminuicao = float(input('Digite a taxa de diminuição:'))

print(f'Você escolheu o número {num}.\nA taxa de aumento é {taxa_aumento}%.\nE a taxa de diminuição é {taxa_diminuicao}%.')
print(f'O valor aumentado {modulos.aumento(num, taxa_aumento)}')
print(f'O valor diminuído é {modulos.aumento(num, taxa_diminuicao)}')
print(f'O dobro é {modulos.dobro(num)}')
print(f'A metade é {modulos.metade(num)}')

