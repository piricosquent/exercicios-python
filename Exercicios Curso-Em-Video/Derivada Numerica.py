resp = int(input('Extremidade ou Ponto Médio?[1/2]'))
if resp == 1:
    print('EXTREMIDADE')
    h = float(input('Digite h:'))
    fx0 = float(input('Digite f(x0):'))
    fx0maish = float(input('Digite f(x0 + h):'))
    fx0mais2h = float(input('Digite f(x0 + 2h)'))
    resposta = (-3*fx0 + 4*fx0maish - fx0mais2h)/(2*h)
    print(f'{resposta}')
else:
    print('PONTO MÉDIO')
    h = float(input('Digite h:'))
    fx0maish = float(input('Digite f(x0 + h):'))
    fx0menosh = float(input('Digite f(x0 - h):'))
    resposta = (fx0maish - fx0menosh)/(2*h)
    print(f'{resposta:.4f}')
1
1