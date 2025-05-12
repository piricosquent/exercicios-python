print('\033[4;36mEscreva dois números e eu vou dizer qual é maior, qual é menor ou se os dois são iguais:\033[m')
n1 = float(input('\033[1;33mPrimeiro número:\033[m'))
n2 = float(input('\033[1;33mSegundo número:\033[m'))
if n1 > n2:
    print('\033[1;32mO primeiro numero é maior do que o segundo.\033[m')
elif n2 > n1:
    print('\033[1;32mO segundo número é maior do que o primeiro.\033[m')
else:
    print('\033[1;31mOs dois números são iguais.\033[m')