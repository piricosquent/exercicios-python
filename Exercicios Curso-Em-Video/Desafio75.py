#1º Ler 4 números e armazená-los de forma direta na tupla:
numeros = (int(input('Digite o 1º número:')),
           int(input('Digite o 2º número:')),
           int(input('Digite o 3º número:')),
           int(input('Digite o 4º número:')))
#2º Printar os números na tela:
print(f'Os números digitados foram: {numeros}')
#3º Verificar quantos vezes o número 9 foi digitado:
print(f'O número 9 foi digitado {numeros.count(9)} vez(es).')
#4º Verificar em qual posição o n 3 foi digitado a 1ª vez. Lembrar q o programa
#não pode indicar erro se o nº 3 não foi digitado:
if 3 in numeros:
    print(f'O número três foi digitado na {numeros.index(3) + 1}ª posição.') #o termo +1 tem significado pois a contagem inicia em 0.
else:
    print('O número três foi digitado nenhuma vez.')
#5º Verificar quais números pares foram digitados.
print('Os números pares digitados foram: ', end='')
for n in numeros:
    if n%2 == 0:
        print(n, end=' ')