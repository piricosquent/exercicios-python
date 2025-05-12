tabela = ('Botafogo', 'Palmeiras', 'Bragantino',
          'Grêmio', 'Atlético-MG', 'Flamengo',
          'Athlético-PR', 'Fluminense', 'Fortaleza',
          'São Paulo', 'Internacional', 'Cuiabá',
          'Corinthians', 'Santos', 'Bahia', 'Vasco da Gama',
          'Cruzeiro', 'Goiás', 'Curitiba', 'América-MG')
d = 17
c = 1
print('\033[1;32m[a]Os 5 primeiros:\033[m')#cor
for cont in range(0, 5):#Atenção: aqui ele vai printar o time 0, 1, 2, 3 e 4 ... o 5º (último) SEMPRE vai ficar de fora do intervalo
    print(f'{c}º {tabela[cont]}') #print(f'Osprimeiros times são {tabela[0:5]}.')
    c += 1
print('\033[1;32m[b]Os 4 últimos:\033[m')#cor
for cont in range(16, 20):#***mesma coisa da linha 10 !!!
    print(f'{d}º {tabela[cont]}')  #print(f'Os últimos times são {tabela[-4:]}.') faz a mesma coisa com 1 única linha de código ...
    d += 1
print('\033[1;32mEm ordem alfabética:\033[m')#cor
for time in sorted(tabela):#colocar em ordem alfabética
    print(time)
escolha = input('Quer saber a posição de qual time ?').title().strip()
posicao = tabela.index(escolha) + 1 ###observar a linha 10 e a linha 14. a gente soma +1 por que a contagem começa em ZERO !!!
print(f'O {escolha} está na {posicao}ª posição!')
