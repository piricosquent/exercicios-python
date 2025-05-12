print(f'\033[1;36m~~~~Tabuada mineira~~~~\033[m')
while True:
    num = int(input('Quer calcular a tabuada de qual número ?'))
    if num < 0:
        break
    for c in range(0, 11):
        print(f'{num}x{c} = {num*c}')
print('\033[1;31mOperação finalizada. Volte sempre.\033[m')