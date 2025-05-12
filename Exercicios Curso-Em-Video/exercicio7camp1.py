
modelo = ['1.DIB mv7','2.DIB turbo','3.DIB Basico']
acessorios = ['1.Ar condicionado', '2.Dir. Hidraulica','3.Motor 3.1','4.Vidros Eletricos','5.Banco de Couro']
for i in modelo:
  print(i)
c = 0
op = int(input("Qual o modelo Escolhido(1 , 2 ou 3) ? "))
if (op == 1):
    c=20000
elif  (op == 2):
    c=15000
elif  (op == 3):
    c=12000
else :
    print("Opção Invalida !!!")
print(c)
for i in acessorios:
  op = input(f"vc deseja {i} (s/n)?")
  while not (op=='s' or op=='n'):op = input("vc deseja "+i+"(s/n)?")
  if  (i == '1.Ar condicionado') and(op =='s'):
      c+=2000
  elif  i == '2.Dir. Hidraulica' and(op=='s'):
      c+=1500
  elif  i == '3.Motor 3.1' and(op=='s'):
      c+=3000
  elif  i == '4.Vidros Eletricos' and(op=='s'):
      c+=1000
  elif  i == '5.Banco de Couro'and(op=='s') :
      c+=1000

print (f'Valor do Carro: R${c}')