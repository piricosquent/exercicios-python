def escreva(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'{msg}'.center(tam))
    print('-' * tam)


mensagem = input('Digite aqui sua mensagem:')
escreva(mensagem)
