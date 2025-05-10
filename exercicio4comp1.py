def imposto_de_renda(nome, cpf, salbruto, ndepend):
    sal = salbruto*0.8
    desc = ndepend*800
    rendaliquida = sal - desc
    if rendaliquida <= 11000:
        aliquota = 0
    elif rendaliquida <= 20000:
        aliquota = 0.05
    elif rendaliquida <= 3000:
        aliquota = 0.1
    else:
        aliquota = 0.15
    pagamento = rendaliquida*aliquota
    return pagamento
nome = str(input('Nome da PF:'))
cpf = str(input('CPF:'))
salbruto = float(input('Salário bruto:R$'))
ndepend = int(input('Número de dependentes:'))
resultado = imposto_de_renda(nome, cpf, salbruto, ndepend)
print('{}\nCPF nº{}\nDeverá pagar R${:.2f} ao imposto de renda.'.format(nome.title(), cpf, resultado))