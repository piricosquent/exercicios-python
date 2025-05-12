from Quiz.modulos import *
import time
score = 0

quiz = [
    {
        "enunciado": "Qual é a capital do Brasil?",
        "a": "São Paulo",
        "b": "Rio de Janeiro",
        "c": "Brasília",
        "d": "Salvador",
        "gabarito": "C"
    },
    {
        "enunciado": "Qual é o símbolo químico da água?",
        "a": "H2O",
        "b": "O2",
        "c": "CO2",
        "d": "NaCl",
        "gabarito": "A"
    },
    {
        "enunciado": "Em que ano o homem pisou na Lua pela primeira vez?",
        "a": "1965",
        "b": "1969",
        "c": "1972",
        "d": "1959",
        "gabarito": "B"
    }
]

cabecalho('Seja muito bem-vindo ao Quiz do Victor', len('Seja muito bem-vindo ao Quiz do Victor') + 4)
dormir()
print(f'\t\tIniciando o programa em...')
dormir()
print(f'\t\t3...')
dormir()
print(f'\t\t\t\t2...')
dormir()
print(f'\t\t\t\t\t\t1...')
dormir()

for q in quiz:
    resposta = pergunta(q["enunciado"], q["a"] , q["b"], q["c"], q["d"])
    score += verificacao(q["gabarito"], resposta)

print(f'Você acertou {score} de {len(quiz)} perguntas.')
