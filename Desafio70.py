c = valor_baixo1000 = total = 0
while True:
    nome = str(input('Nome do produto:')).title()
    valor = float(input('Valor do produto:R$'))
    c += 1
    if c == 1:
        menor_valor = valor
        menor_nome = nome
    if valor < menor_valor:
        menor_nome = nome
    if valor < 1000:
        valor_baixo1000 += 1
    total += valor
    opcao = str(input('Quer continuar?[S/N]')).strip().upper()[0]
    if opcao in 'N':
        break
print(f'O produto mais barato foi {menor_nome}, foram {valor_baixo1000} produtos com preço abaixo de R$1000.00 e o total da compra foi R${total:.2f}.')
