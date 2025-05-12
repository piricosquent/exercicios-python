#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
while True:
    cont += 1
    lista.append(int(input('Digite um número:')))
    print('Número adicionado.')
    resp = input('Quer continuar?').strip().lower()
    if resp in 'naonãoñ':
        break
print('-='*30)
print('Resultados.')
print(f'Você adicionou {len(lista)} números.')
if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')
lista.sort(reverse=True)
print(f'Lista em ordem decrescente: ', lista)



