frase = str(input('Digite uma frase:')).lower().strip()
num = frase.count('a')
posicao_1 = frase.find('a') + 1
posicao_final = frase.rfind('a') + 1
print('A frase: "{}" tem {} letras "A", a primeira está na posição {} e a última na posição {}.'.format(frase.title(), num, posicao_1, posicao_final))
