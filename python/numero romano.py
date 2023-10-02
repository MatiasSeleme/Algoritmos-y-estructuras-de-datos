valor = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}

def numerosRomanos(numero):
    if len(numero) == 1:
        return valor[numero[0]]
    elif valor[numero[0]] >= valor[numero[1]]:
        return valor[numero[0]] + numerosRomanos(numero[1:])
    else:
        return -valor[numero[0]] + numerosRomanos(numero[1:])

print(numerosRomanos('xiv'))
