numero = int(input('Digite um número:'))
unidade = numero%10
dezena = numero//10%10
centena = numero//100%10
milhar = numero//1000%10
print('-> Unidade: {}\n-> Dezena: {}\n-> Centena: {}\n-> Milhar: {}'.format(unidade, dezena, centena, milhar))