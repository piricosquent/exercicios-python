nome = str(input('Nome completo:')).title()
palavras = nome.split()
primeiro_nome = palavras[0]
ultimo_nome = palavras[len(palavras) - 1]
print('Seu primeiro nome é:{}'.format(primeiro_nome))
print('Seu último nome é:{}'.format(ultimo_nome))