palavras = ('Victor', 'Hugo', 'Cordeiro', 'Lombre')#criando a tupla
for p in palavras:#p no caso é cada palavra da tupla. Mas, cada palavra é uma lista, então eu posso analisar cada item dessa lista.
        print(f'\nA palavra {p.upper()} tem as vogais -> ', end='') #  então, cada letra da palavra é armazenada como um item da lista
        for letra in p: #aqui, eu pedi para o programa analisar cada item da lista p, que seria a palavra da lista
                if letra.lower() in 'aeiou':#e aqui eu pedi para me mostrar se tem as vogais
                        print("'",letra, "'", end=' ')#aqui eu pedi para printar as vogais presentes na palavras
#esse programa é simples, mas exige que eu saiba que as palavras que eu coloquei na lista
#também são consideradas lista... é como se palavras fosse um conjunto e p fosse um subconjunto de palavras...
#a lógica é meio chatinha, mas nada difícil... só exige criatividade.
#no termo for letra in p:
#                   if letra.lower() in 'aeiou':
#                           print(letra, end=' ')
#o programa já tinha dividido a palavra em p = ('v', 'i', 'c', 't', 'o', 'r'), por exemplo
#e cada item da lista 'p' que eu criei eu chamei de 'letra'
#se eu digitar print(letra), o programa vai printar 'v   i   c   t   o   r' ... entendeu?
#mas aí eu faço um laço que verifica se o item da lista 'letra'em questão está contido no termo 'aeiou'. 
#se estiver, o programa vai printar o termo x da lista 'letra', entendeu?? é simples demais...

