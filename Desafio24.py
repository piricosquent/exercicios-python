cidade = str(input('Digite o nome de alguma cidade:')).title()
palavras = cidade.split()
procura = palavras.count('Santo')
if procura == 0:
    print('Essa cidade não tem Santo no nome.')
else:
    print(cidade)