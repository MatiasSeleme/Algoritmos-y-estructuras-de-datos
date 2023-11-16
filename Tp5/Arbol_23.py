class NodoArbol:
    def __init__(self, nombre, capturador=None, descripcion=""):
        self.nombre = nombre
        self.capturador = capturador
        self.descripcion = descripcion
        self.izquierda = None
        self.derecha = None

def insertar(raiz, criatura, capturador=None, descripcion=""):
    if raiz is None:
        return NodoArbol(criatura, capturador, descripcion)
    if criatura < raiz.nombre:
        raiz.izquierda = insertar(raiz.izquierda, criatura, capturador, descripcion)
    elif criatura > raiz.nombre:
        raiz.derecha = insertar(raiz.derecha, criatura, capturador, descripcion)
    return raiz

def descripcion(raiz, criatura, descripcion):
    nodo = buscar(raiz, criatura)
    if nodo:
        nodo.descripcion = descripcion

def buscar(raiz, criatura):
    if raiz is None or raiz.nombre == criatura:
        return raiz
    if criatura < raiz.nombre:
        return buscar(raiz.izquierda, criatura)
    return buscar(raiz.derecha, criatura)

def mostrar_Criatura(raiz, criatura):
    nodo = buscar(raiz, criatura)
    if nodo:
        print(f"Nombre: {nodo.nombre}")
        print(f"Descripción: {nodo.descripcion}")
        print(f"Capturador: {nodo.capturador}")
    else:
        print(f"Criatura '{criatura}' no encontrada")

def listado(raiz):
    if raiz:
        listado(raiz.izquierda)
        print(f"Nombre: {raiz.nombre}, Capturador: {raiz.capturador}")
        listado(raiz.derecha)

def capturadores_Mas_Comunes(raiz):
    capturadores = {}
    contador_capturadores(raiz, capturadores)
    return sorted(capturadores.items(), key=lambda x: x[1], reverse=True)[:3]

def contador_capturadores(raiz, capturadores):
    if raiz:
        contador_capturadores(raiz.izquierda, capturadores)
        capturador = raiz.capturador
        if capturador:
            if capturador in capturadores:
                capturadores[capturador] += 1
            else:
                capturadores[capturador] = 1
        contador_capturadores(raiz.derecha, capturadores)

def capturadas_Por(raiz, capturador):
    criaturas = []
    Criaturas_Capturadas(raiz, capturador, criaturas)
    return criaturas

def Criaturas_Capturadas(raiz, capturador, criaturas):
    if raiz:
        Criaturas_Capturadas(raiz.izquierda, capturador, criaturas)
        if raiz.capturador == capturador:
            criaturas.append(raiz.nombre)
        Criaturas_Capturadas(raiz.derecha, capturador, criaturas)

def Criaturas_no_capturadas(raiz):
    no_capturadas = []
    buscar_criaturas_no_capturadas(raiz, no_capturadas)
    return no_capturadas

def buscar_criaturas_no_capturadas(raiz, no_capturadas):
    if raiz:
        buscar_criaturas_no_capturadas(raiz.izquierda, no_capturadas)
        if raiz.capturador is None:
            no_capturadas.append(raiz.nombre)
        buscar_criaturas_no_capturadas(raiz.derecha, no_capturadas)

def capturar_criatura(raiz, criatura, capturador):
    nodo = buscar(raiz, criatura)
    if nodo:
        nodo.capturador = capturador

def eliminar_criatura(raiz, criatura):
    if raiz is None:
        return raiz
    if criatura < raiz.nombre:
        raiz.izquierda = eliminar_criatura(raiz.izquierda, criatura)
    elif criatura > raiz.nombre:
        raiz.derecha = eliminar_criatura(raiz.derecha, criatura)
    else:
        if raiz.izquierda is None:
            return raiz.derecha
        elif raiz.derecha is None:
            return raiz.izquierda
        sucesor = encontrar_sucesor(raiz.derecha)
        raiz.nombre = sucesor.nombre
        raiz.derecha = eliminar_criatura(raiz.derecha, sucesor.nombre)
    return raiz

def encontrar_sucesor(nodo):
    while nodo.izquierda:
        nodo = nodo.izquierda
    return nodo

def modificar_nombre(raiz, criatura, nuevo_nombre):
    nodo = buscar(raiz, criatura)
    if nodo:
        nodo.nombre = nuevo_nombre

def listado_por_nivel(raiz):
    if not raiz:
        return
    nivel_actual = [raiz]
    while nivel_actual:
        nivel_siguiente = []
        for nodo in nivel_actual:
            print(f"Nombre: {nodo.nombre}, Capturador: {nodo.capturador}")
            if nodo.izquierda:
                nivel_siguiente.append(nodo.izquierda)
            if nodo.derecha:
                nivel_siguiente.append(nodo.derecha)
        nivel_actual = nivel_siguiente

raiz = None
datos_iniciales = [
    ("Cerbero", "Heracles"),
    ("Toro de Creta", "Heracles"),
    ("Cierva Cerinea", "Heracles"),
    ("Jabalí de Erimanto", "Heracles"),
    ("Basilisco", "Zeus"),
    ("Sirenas", "Ulises"),
    ("Aves del Estínfalo", "Heracles"),
    ("Ladón", "Hera"),
]

for criatura, capturador in datos_iniciales:
    raiz = insertar(raiz, criatura, capturador)

capturar_criatura(raiz, "Aves del Estínfalo", "Heracles")

modificar_nombre(raiz, "Ladón", "Dragón Ladón")

raiz = eliminar_criatura(raiz, "Basilisco")
raiz = eliminar_criatura(raiz, "Sirenas")

criaturas_capturadas_por_heracles = capturadas_Por(raiz, "Heracles")
print("Capturadas por Heracles:", criaturas_capturadas_por_heracles)

print()

print("Listado:")
print()
listado(raiz)

print()

mostrar_Criatura(raiz, "Talos")

print()

capturadores_top3 = capturadores_Mas_Comunes(raiz)
print("3 héroes o dioses que capturaron más criaturas:")
for capturador, cantidad in capturadores_top3:
    print(f"{capturador}: {cantidad}")

print()

Criaturas_no_capturadas = Criaturas_no_capturadas(raiz)
print("Criaturas no capturadas:", Criaturas_no_capturadas)

print()

print("Listado por nivel del árbol:")
print()

listado_por_nivel(raiz)