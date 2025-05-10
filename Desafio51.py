print('\033[4;31mPROGRESSÃO ARITMÉTICA DO VICTOR\033[m')
razao = int(input('Digite a razão da progressão:'))
primeiro_termo = int(input('Digite o primeiro termo da progressão:'))
ultimo_termo = razao + primeiro_termo
for c in range(primeiro_termo, razao*10 + primeiro_termo, razao):
    print(c, end='\033[32m -> \033[m')
print('\033[1;31mFIM\033[m')