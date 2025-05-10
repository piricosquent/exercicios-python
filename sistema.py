from lib.interface import *


while True:
    escolha = menu(['Ver Pessoas Cadastradas.', 'Cadastrar Nova Pessoa', 'Sair do sistema.'])
    dormir()
    try:
        escolha_int = int(escolha)
    except ValueError or TypeError:
        print(f'{cor(1)}ERRO! Selecione uma opção válida.{cor(0)}')
        continue
    if escolha_int == 1:
        opcao_1()
        with open('cadastros.txt', 'r') as arquivo:
            print('\n' + arquivo.read())
    elif escolha_int == 2:
        opcao_2()
        with open('cadastros.txt', 'a+') as arquivo:
            nome = input('Digite o nome:')
            idade = ler_int('a idade')
            arquivo.write(f'{nome};{idade}\n')
        dormir()
        with open('cadastros.txt', 'r') as arquivo:
            print('\n' + arquivo.read())
    elif escolha_int == 3:
        opcao_3()
        break
    else:
        print(f'{cor(1)}Opção inválida. Tente novamente.{cor(0)}')

