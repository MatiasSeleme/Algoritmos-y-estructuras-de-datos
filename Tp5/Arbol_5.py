class Nodo:
    def __init__(self, nombre, heroe):
        self.nombre = nombre
        self.heroe = heroe
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre, heroe):
        self.raiz = self._insertar(self.raiz, nombre, heroe)

    def _insertar(self, nodo, nombre, heroe):
        if nodo is None:
            return Nodo(nombre, heroe)
        if nombre < nodo.nombre:
            nodo.izquierda = self._insertar(nodo.izquierda, nombre, heroe)
        elif nombre > nodo.nombre:
            nodo.derecha = self._insertar(nodo.derecha, nombre, heroe)
        return nodo

    def villanos_alfabeticos(self):
        personajes = self.personajes_alfabeticos(self.raiz, False)
        return personajes

    def heroes_c(self):
        heroes = self.personajes_c(self.raiz)
        return heroes

    def contador_heroes(self):
        return self._contador_heroes(self.raiz)

    def renombrar_personaje(self, nombre_objetivo, nuevo_nombre):
        self.raiz = self._renombrar(self.raiz, nombre_objetivo, nuevo_nombre)

    def lista_personajes_descendente(self):
        personajes = self._lista_personajes_descendente(self.raiz)
        return personajes

    def bosque(self):
        HeroesT = ArbolBinarioBusqueda()
        VillanosT = ArbolBinarioBusqueda()
        self._bosque(self.raiz, HeroesT, VillanosT)
        return HeroesT, VillanosT

    def personajes_alfabeticos(self, nodo, heroe):
        if nodo is None:
            return []
        personajes = []
        if not heroe:
            personajes.append(nodo.nombre)
        personajes += self.personajes_alfabeticos(nodo.izquierda, heroe)
        personajes += self.personajes_alfabeticos(nodo.derecha, heroe)
        return personajes

    def personajes_c(self, nodo):
        if nodo is None:
            return []
        heroes = []
        if nodo.heroe and nodo.nombre.startswith('C'):
            heroes.append(nodo.nombre)
        heroes += self.personajes_c(nodo.izquierda)
        heroes += self.personajes_c(nodo.derecha)
        return heroes

    def _contador_heroes(self, nodo):
        if nodo is None:
            return 0
        count = 0
        if nodo.heroe:
            count += 1
        count += self._contador_heroes(nodo.izquierda)
        count += self._contador_heroes(nodo.derecha)
        return count

    def _renombrar(self, nodo, nombre_objetivo, nuevo_nombre):
        if nodo is None:
            return None
        if nodo.nombre == nombre_objetivo:
            nodo.nombre = nuevo_nombre
        nodo.izquierda = self._renombrar(nodo.izquierda, nombre_objetivo, nuevo_nombre)
        nodo.derecha = self._renombrar(nodo.derecha, nombre_objetivo, nuevo_nombre)
        return nodo

    def _lista_personajes_descendente(self, nodo):
        if nodo is None:
            return []
        personajes = []
        personajes += self._lista_personajes_descendente(nodo.derecha)
        personajes.append((nodo.nombre, nodo.heroe))
        personajes += self._lista_personajes_descendente(nodo.izquierda)
        return personajes

    def _bosque(self, nodo, HeroesT, VillanosT):
        if nodo is None:
            return
        if nodo.heroe:
            HeroesT.insertar(nodo.nombre, True)
        else:
            VillanosT.insertar(nodo.nombre, False)
        self._bosque(nodo.izquierda, HeroesT, VillanosT)
        self._bosque(nodo.derecha, HeroesT, VillanosT)

arbol = ArbolBinarioBusqueda()
arbol.insertar("Black Widow", True)
arbol.insertar("Iron Man", True)
arbol.insertar("Loki", False)
arbol.insertar("Spider-Man", True)
arbol.insertar("Doctor Strange", True)
arbol.insertar("Thanos", False)
arbol.insertar("Captain America", True)
arbol.insertar("Starlord", True)
arbol.insertar("Duende Verde", False)

villanos = arbol.villanos_alfabeticos()
print("Villanos ordenados alfabéticamente:", villanos)

heroes_con_c = arbol.heroes_c()
print("Superhéroes que empiezan con C:", heroes_con_c)

cantidad_heroes = arbol.contador_heroes()
print("Cantidad de superhéroes:", cantidad_heroes)

arbol.renombrar_personaje("Doctor Strange", "Dr. Strange")

personajes_descendentes = arbol.lista_personajes_descendente()
print("Superhéroes ordenados de manera descendente:", personajes_descendentes)

heroes_arbol, villanos_arbol = arbol.bosque()

cantidad_nodos_heroes = heroes_arbol.contador_heroes()
cantidad_nodos_villanos = villanos_arbol.contador_heroes()
print("Nodos en el árbol de superhéroes:", cantidad_nodos_heroes)
print("Nodos en el árbol de villanos:", cantidad_nodos_villanos)

heroes_alfabeticos = heroes_arbol.villanos_alfabeticos()
villanos_alfabeticos = villanos_arbol.villanos_alfabeticos()
print("Barrido alfabético de superhéroes:", heroes_alfabeticos)
print("Barrido alfabético de villanos:", villanos_alfabeticos)