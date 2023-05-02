def Romano_decimal(numero):
    
    valor = { 'i' : 1, 'v' : 5, 'x' : 10, 'l': 50, 'c' : 100, 'd' : 500, 'm' : 1000 }

    decimal = 0
    anterior = 0
    for size in numero[::-1]:
        Va = valor[size]
        if Va < anterior:
            decimal -=Va
        else:
            decimal+=Va

        anterior = Va    
    return decimal

print(Romano_decimal('iv'))