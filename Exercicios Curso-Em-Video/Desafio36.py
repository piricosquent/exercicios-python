nome = str(input('Digite o seu nome:'))
valor = float(input('Qual o valor a ser financiado?R$'))
anos = int(input('Em quantos anos você deseja parcelar o financiamento?'))
salario = float(input('Qual o valor do seu salário?R$'))
vezes = anos*12
prestacao = valor/vezes
if prestacao > salario*0.3:
    print('\033[1;31mEmpréstimo negado.\033[m')
else:
    print('\033[1;32mEmpréstimo aprovado.\033[m')
    print('Valor da prestação: \033[1;32mR${:.2f}\033[m.'.format(prestacao))
print('Obrigado, Sr(a) {}.'.format(nome))
