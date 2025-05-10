def total_hotel(diaria):
    if diaria < 15:
        total = diaria*(320)
    elif diaria == 15:
        total = diaria*310
    else:
        total = diaria*307
    return total
diaria = int(input('Olá, boa tarde!\nQuantos dia o(a) senhor(a) ficou hospedado(a) em nossas instalações?'))
resultado = total_hotel(diaria)
print('O valor a ser pago é R${:.2f}.\nObrigado pela preferência e volte sempre.'.format(resultado))

