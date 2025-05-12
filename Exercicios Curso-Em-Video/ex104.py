def leiaint(num):
    try:
        num = int(num)
        return f'O número inteiro digitado foi {num}.'
    except(ValueError, TypeError):
        return '\033[31mErro. Digite um número inteiro por favor.\033[0m'

while True:
    print('-'*10)
    num = input('')
    print(leiaint(num))
