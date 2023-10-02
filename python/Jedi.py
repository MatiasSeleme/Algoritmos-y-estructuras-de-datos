mochila = ["agua", "peluche", "tiramisu", "cafe", "sable de luz", "comunicador", "dinero", "espada"]

def sacarSable(a, c = 0):
    if a[-1] != "sable de luz" and len(a) != 1:
        c = c + 1
        return sacarSable(a[:-1], c)
    else:
        if a[-1] != "sable de luz":
            print("No se ha encontrado el sable de luz")
        else:
            print("Se ha encontrado el sable de luz")
        return c

print(sacarSable(mochila))
