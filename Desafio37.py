numero = int(input('Digite um número inteiro:'))
print('[1] - Para \033[1;32mBinário;\033[m')
print('[2] - Para \033[1;32mOctal;\033[m')
print('[3] - Para \033[1;32mHexadecimal.\033[m')
escolha = int(input('Sua opção:'))
if escolha == 1:
    print('{} convertido para BINÁRIO é {}'.format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('{} convertido para OCTAL é {}'.format(numero, oct(numero)[2:]))
elif escolha == 3:
    resultado = print('{} convertido para HEXADECIMAL é {}'.format(numero, hex(numero)[2:]))
else:
    print('\033[2;31mOpção inválida. Tente novamente.\033[m')
