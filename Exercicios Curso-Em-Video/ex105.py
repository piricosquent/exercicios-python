def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['max'] = max(n)
    r['min'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'Boa'
        elif r['média'] >= 5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'Ruim'
    return r


print(notas(10, 6, 7, 5, 4, sit=True))
