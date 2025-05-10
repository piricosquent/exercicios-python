def calcular_valor_carro(modelo, acessorios):
    preco_modelo = 0

    if modelo == "1":
        preco_modelo = 20000
    elif modelo == "2":
        preco_modelo = 15000
    elif modelo == "3":
        preco_modelo = 12000

    preco_acessorios = 0
    for acessorio in acessorios:
        if acessorio == "1":
            preco_acessorios += 2000
        elif acessorio == "2":
            preco_acessorios += 1500
        elif acessorio == "3":
            preco_acessorios += 3000
        elif acessorio == "4" or acessorio == "5":
            preco_acessorios += 1000

    valor_total = preco_modelo + preco_acessorios
    return valor_total
modelo = str(input('Qual o modelo do carro?\n[1]Dib TURBO\n[2]Dib MV7\n[3]Dib Básico'))

acessorios = str(input('Quais acessórios deseja adicionar ao carro?\n[1]Ar condicionado 2.000\n[2]Dir. hidráulica 1.500\n[3]Motor 3.1 3.000\n[4]Vidros elétricos 1.000\n[5]Banco de couro 1.000'))

resultado = calcular_valor_carro(modelo, acessorios)
print(f"O valor do carro é {resultado:.2f}")



