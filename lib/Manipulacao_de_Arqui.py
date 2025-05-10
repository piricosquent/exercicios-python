from lib.interface import *

# Adiciona uma linha ao arquivo
with open('cadastros.txt', 'a+') as arquivo:
    nome = input('Digite o nome:')
    idade = ler_idade()
    arquivo.write(f'{nome};{idade}\n')

# Lê e imprime todo o conteúdo
with open('cadastros.txt', 'r') as arquivo:
    print('\n' + arquivo.read())
