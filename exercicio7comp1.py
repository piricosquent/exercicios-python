nome = input("Digite seu nome: ")
funcionario = ['1.Diretor','2.Gerente','3.Outros']
print(funcionario)
op = int(input("Digite o cargo (1,2 ou 3): "))
if op == 1 : gx = 0.2
elif op==2 : gx = 0.1
elif op==3 : gx = 0.05
setor = input("Qual o seu setor: C, R, B ou Outro?")
salario = float(input("Qual o seu salário? "))
tdv = float(input("Qual o seu total de vendas? "))

if setor == "C" and tdv >= 1000: co = tdv * 0.15
elif setor == "R" and  tdv >= 800:  co = tdv * 0.2
elif setor == "B" and  tdv >=1500: co = tdv * 0.35
elif setor == "OUTROS" and tdv >= 2000: co = tdv * 0.37
Sfinal = (salario + co)*(1+gx)
print('Salario Final:',Sfinal)
