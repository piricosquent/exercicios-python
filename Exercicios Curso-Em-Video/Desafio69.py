print('='*20)
print(f'{"INSS":-^20}')
print('='*20)
contador = pessoa_velha = homem = mulher_nova = 0
while True:
    contador += 1
    print(f'{contador}ª pessoa:')
    idade = int(input('Idade:'))
    if idade > 18:
        pessoa_velha += 1
    sexo = str(input('Sexo[H/M]:')).strip().upper()[0]
    if sexo in 'H':
        homem += 1
    if sexo in 'M':
        if idade < 20:
            mulher_nova += 1
    opcao = str(input('Quer continuar[S/N]:')).strip().upper()[0]
    if opcao in 'N':
        break
print(f'Ao todo foram cadastrados {mulher_nova} mulheres com menos de 20 anos, {homem} pessoas do sexo masculino e {pessoa_velha} pessoas com mais de 18 anos.')