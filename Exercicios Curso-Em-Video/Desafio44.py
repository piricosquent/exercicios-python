import emoji
print('\033[31m{:=^30}\033[m'.format('\033[35mDe minas SHOP {} \033[31m'.format(emoji.emojize(':thumbs_up:'))))
valor = float(input('Qual o valor a ser pago ? R$'))
print('''Qual a forma de pagamento ?
\033[1;31m[1]\033[m -> à vista dinheiro/cheque: \033[1;32m10% de desconto\033[m

\033[1;31m[2]\033[m -> à vista no cartão: \033[1;32m5% de desconto\033[m

\033[1;31m[3]\033[m -> em até 2x no cartão: \033[1;32mpreço formal\033[m 

\033[1;31m[4]\033[m -> 3x ou mais no cartão: \033[1;32m20% de juros\033[m''')
escolha = int(input('\033[4;31mOpção ->'))
if escolha == 1:
    valorfinal = valor*0.9
elif escolha == 2:
    valorfinal = valor*0.95
elif escolha == 3:
    valorfinal = valor
elif escolha == 4:
    valorfinal = valor*1.2
else:
    valorfinal = 0
    print('\033[4;31mOpção inválida. Tente novamente.\033[m')
print('O valor final a ser pago é R${:.2f}'.format(valorfinal))
