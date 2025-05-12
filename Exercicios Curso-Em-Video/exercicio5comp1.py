def montante_resultante(c, i, n):
    m = c*(1 + i)**n
    return m
c = float(input('Digite o valor da ser investido:'))
i = float(input('Digite a taxa de juros ao mês:'))
n = int(input('Digite o número de meses que o valor será investido:'))
resultado = montante_resultante(c, i, n)
print('Você terá um retorno de R${:.2f}'.format(resultado))