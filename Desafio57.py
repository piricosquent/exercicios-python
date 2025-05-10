sexo = ''
'''while sexo != 'M' and sexo != 'F':
  sexo = str(input('Sexo:')).upper()
print('Obrigado.')'''
#também pode ser :
sexo = str(input('Sexo:')).strip()
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, digite corretamente. Buro p crl'))
print('Obrigado.')