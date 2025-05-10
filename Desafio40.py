n1 = float(input('Digite a nota da Primeira Avaliação:'))
n2 = float(input('Digite a nota da Segunda Avaliação:'))
media = (n1 + n2)/2
if media < 5.0:
    print('A média foi {:.2f} e o aluno está \033[1;31mREPROVADO.\033[m'.format(media))
elif media >= 5.0 and media < 7.0:
    print('A media foi {:.2f} e o aluno está \033[1;33mEM RECUPERAÇÃO\033[m'.format(media))
else:
    print('A media foi {:.2f} e o aluno está \033[1;32mAPROVADO\033[m\n\033[1;35mPARABÉNS PELO DESEMPENHO !\033[m'.format(media))


