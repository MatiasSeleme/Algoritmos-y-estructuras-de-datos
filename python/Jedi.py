mochila = ["agua", "peluche", "tiramisu", "cafe", "Sable de luz", "comunicador", "dinero", "espada"]
Sable = 0
cantidad = 0

def usar_la_fuerza():
    global cantidad, Sable, i
    
    if i < 0:
        print('La cantidad de objetos hallados fue', cantidad)
        if Sable == 1:
            print('Se ha encontrado el sable')
        else:
            print('No se ha encontrado el sable')
        return
    
    cantidad += 1
    print("Se encontro", mochila[i], "en la mochila despues de sacar")
    if mochila[i] == "Sable de luz":
        Sable = 1
    i -= 1
    usar_la_fuerza()

i = len(mochila) - 1
usar_la_fuerza()