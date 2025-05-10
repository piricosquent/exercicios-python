print('\033[1;36m-=-\033[m'*6)
n1 = float(input('Primeiro valor:'))
n2 = float(input('Segundo valor:'))
print('\033[1;36m-=-\033[m'*6)
opcao = 0
while opcao != 5:
    print('''\033[36mEscolha uma opção:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa\033[m''')
    opcao = int(input('\033[31m>>>> Qual a sua opção ?\033[m'))
    if opcao == 1:
        resposta = n1 + n2
        print(f'{n1} + {n2} = {resposta}')
    elif opcao == 2:
        resposta = n1 * n2
        print(f'{n1} x {n2} = {resposta}')
    elif opcao == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}.')
        elif n1 == n2:
            print('Números iguais.')
        else:
            print(f'{n2} é maior que {n1}.')
    elif opcao == 4:
        print('\033[1;36m-=-\033[m' * 6)
        n1 = float(input('Primeiro valor:'))
        n2 = float(input('Segundo valor:'))
        print('\033[1;36m-=-\033[m' * 6)
    elif opcao == 5:
        print('\033[1;34mObrigado, até logo.\033[m')
    else:
        print('\033[1;31mOpção inválida. Tente novamente.\033[m')
print('\033[35mFim do programa. Volte sempre.\033[m')



