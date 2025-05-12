from datetime import datetime
def voto(nasc):
    idade = datetime.now().year - nasc
    if idade < 16:
        return f'Idade: {idade}. Voto negado.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Idade: {idade}. Voto opcional.'
    else:
        return f'Idade {idade}. Voto obrigatório.'

def enunciado(texto):
    tam = len(texto) + 4
    print('\033[35m' + '-'*tam)
    print(f'{texto}'.center(tam))
    print('-' * tam, '\033[0m')


enunciado('MÁQUINA DE VOTOS')
nasc = int(input('Digite o seu ano de nascimento:'))
print(voto(nasc))
print('FIM')