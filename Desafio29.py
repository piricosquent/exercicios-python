velocidade = float(input('Qual foi a velocidade medida?'))
if velocidade > 80:
    print('Você excedeu o limite de velocidade e a multa a ser paga é RS{:.2f}.'.format((velocidade - 80)*7))
print('Dirija com segurança.')