num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
       'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
       'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
       'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
       'Dezenove', 'Vinte') #criei a tupla com os números de 0 a 20 escritos por extenso.

while True:
    numero = int(input('Digite um número entre 0 e 20:'))#pedir um número para o jogador
    if 0 <= numero <= 20:#verificar se está no intervalo
        print(num[numero])
    else:
        print('O número digitado não está entre 0 e 20.')
    resp = input('Deseja continuar?').strip().upper()#perguntar se quer continuar (strip retira espaço e upper coloca tudo em maiúscula)
    if resp in ('N', 'NÃO', 'NAO'):
        break
print('-----Fim-----')
