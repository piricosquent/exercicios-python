produtos = ('Alface', 0.79,
            'Tomate', 3.99,
            'Batata inglesa', 2.89,
            'Maçã', 5.99,
            'Aipim', 2.49,
            'Brócolis', 6.99)
print('-'*37)#imprime - 37 vezes (37 = 30 casas q usei para mostrar o produto +
#                                      5 casas que usei para mostrar o preço +
#                                      2 casas q decimais que usei para representar o valor do item.)
print(f'{"Listagem":-^37}')#imprime a palavra Listagem centralizada em 37 casas e os espaços são preenchidos com -
print('-'*37)
for pos in range(0, len(produtos)):
    if pos%2==0:#note que os produtos sempre estão em posição par, ex: pos alface = 0, pos tomate = 2 ...
        print(f'{produtos[pos]:.<30}', end='')#já os preços estão em posições ímpares
    else:
        print(f'R${produtos[pos]:>5.2f}')
print('-'*37)

