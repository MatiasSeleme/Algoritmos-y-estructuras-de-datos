from lista import Lista as ListaSimple
from random import randint

def criterio_comparacion(value, criterio):
    if isinstance(value, (int, str, bool)):
        return value
    else:
        dic_atributos = value.__dict__
        if criterio in dic_atributos:
            return dic_atributos[criterio]
        else:
            print('no se puede ordenar por este criterio')


class Lista():

    def __init__(self):
        self.__elements = []

    def insert(self, value, criterio=None):
        # print('criterio de insercion', criterio)
        if len(self.__elements) == 0 or criterio_comparacion(value, criterio) >= criterio_comparacion(self.__elements[-1][0], criterio):
            self.__elements.append([value, ListaSimple()])
        elif criterio_comparacion(value, criterio) < criterio_comparacion(self.__elements[0][0], criterio):
            self.__elements.insert(0, [value, ListaSimple()])
        else:
            index = 1
            while criterio_comparacion(value, criterio) >= criterio_comparacion(self.__elements[index][0], criterio):
                index += 1
            self.__elements.insert(index, [value, ListaSimple()])

    def search(self, search_value, criterio=None):
        position = None
        first = 0
        last = self.size() - 1
        while (first <= last and position == None):
            middle = (first + last) // 2
            if search_value == criterio_comparacion(self.__elements[middle][0], criterio):
                position = middle
            elif search_value > criterio_comparacion(self.__elements[middle][0], criterio):
                first = middle + 1
            else:
                last = middle - 1
        return position

    def delete(self, value, criterio=None):
        return_value = None
        pos = self.search(value, criterio)
        if pos is not None:
            return_value = self.__elements.pop(pos)
        return return_value

    def size(self):
        return len(self.__elements)

    def barrido(self):
        for value in self.__elements:
            print(value[0])
            print('Sublista ----------------')
            value[1].barrido()

    def barrido_entrenadores(self):
        for value in self.__elements:
            print(value[0])
            print('Lista de Pokemons:')
            value[1].barrido()
            print()

    def barrido_cantidad_torneos_ganados(self, cantidad_victorias):
        for value in self.__elements:
            if value[0].ct_ganados > cantidad_victorias:
                print(value[0])

    def order_by(self, criterio=None, reverse=False):
        dic_atributos = self.__elements[0][0].__dict__
        if criterio in dic_atributos:
            def func_criterio(valor):
                return valor.__dict__[criterio]

            self.__elements.sort(key=func_criterio, reverse=reverse)
        else:
            print('no se puede ordenar por este criterio')

    def get_element_by_index(self, index):
        return_value = None
        if index >= 0 and index < self.size():
            return_value = self.__elements[index]
        return return_value


class Entrenador():

    def __init__(self, nombre, ct_ganados=0, cb_perdidas=0, cb_ganadas=0):
        self.nombre = nombre
        self.ct_ganados = ct_ganados
        self.cb_perdidas = cb_perdidas
        self.cb_ganadas = cb_ganadas

    def __str__(self):
        return f'{self.nombre} --> ctg:{self.ct_ganados}-cbg{self.cb_ganadas}-cbp{self.cb_perdidas}'
    
    def porcentaje_cb_ganadas(self):
        if self.cb_ganadas + self.cb_perdidas == 0:
            return 0.0
        return (self.cb_ganadas / (self.cb_ganadas + self.cb_perdidas)) * 100

    def tiene_porcentaje_alto(self, porcentaje_deseado=79):
        return self.porcentaje_cb_ganadas() >= porcentaje_deseado

class Pokemon():

    def __init__(self, nombre, tipo, nivel=1, subtipo=None):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f'{self.nombre}-{self.nivel}-{self.tipo}-{self.subtipo}'


e1 = Entrenador('Juan', ct_ganados=randint(1, 10), cb_ganadas=randint(1, 10), cb_perdidas=randint(1, 10))
e2 = Entrenador('Maria', ct_ganados=randint(1, 10), cb_ganadas=randint(1, 10), cb_perdidas=randint(1, 10))
e3 = Entrenador('Ana', ct_ganados=randint(1, 10), cb_ganadas=randint(1, 10), cb_perdidas=randint(1, 10))

entrenadores = [e1, e2, e3]

lista_entrenadores = Lista()

p1 = Pokemon('pikachu', 'electrico', randint(1, 20))
p2 = Pokemon('jolteon', 'electrico', randint(1, 20))
p3 = Pokemon('vaporeon', 'agua', randint(1, 20), "volador")
p4 = Pokemon('flareon', 'fuego', randint(1, 20), "planta")
p5 = Pokemon('leafeon', 'planta', randint(1, 20))

pokemons = [p1, p2, p3, p4, p5]

for entrenador in entrenadores:
    lista_entrenadores.insert(entrenador, 'nombre')

print()
print("Pokemons de entrenadores:")
print()

for pokemon in pokemons:
    numero_entrenador = randint(0, lista_entrenadores.size()-1)
    entrenador = lista_entrenadores.get_element_by_index(numero_entrenador)
    entrenador[1].insert(pokemon, 'nombre')


lista_entrenadores.barrido_entrenadores()
print()

print("Busqueda por nombre:")
print()

pos = lista_entrenadores.search('Juan', 'nombre')
if pos is not None:
    valor = lista_entrenadores.get_element_by_index(pos)
    entrenador, sublista = valor[0], valor[1]
    print(f'{entrenador.nombre} tiene {sublista.size()} pokemons')

print()
print("Barrido por torneos ganados:")

lista_entrenadores.barrido_cantidad_torneos_ganados(6)

print()
mayor_cantidad = lista_entrenadores.get_element_by_index(0)[0].ct_ganados
pos_mayor = 0

for pos in range(0, lista_entrenadores.size()):
    entrenador = lista_entrenadores.get_element_by_index(pos)[0]
    if entrenador.ct_ganados > mayor_cantidad:
        pos_mayor = pos
        mayor_cantidad = entrenador.ct_ganados

valor = lista_entrenadores.get_element_by_index(pos_mayor)
entrenador, sublista = valor[0], valor[1]

if sublista.size() > 0:
    pokemon_mayor = sublista.get_element_by_index(0)
    for pos in range(1, sublista.size()):
        pokemon = sublista.get_element_by_index(pos)
        if pokemon.nivel > pokemon_mayor.nivel:
            pokemon_mayor = pokemon

print(f'El pokemon de mayor nivel del entrenador {entrenador.nombre} es {pokemon_mayor.nombre} {pokemon_mayor.nivel} ')


pos = lista_entrenadores.search('Juan', 'nombre')
if pos is not None:
    valor = lista_entrenadores.get_element_by_index(pos)
    entrenador, sublista = valor[0], valor[1]
    sublista.order_by('nivel')
    print(f'{entrenador.nombre} tiene {sublista.size()} pokemons')

print()
print("Entrenadores con porcentaje de batallas ganadas >= a 79%")
print()

porcentaje = 0.0

for i in entrenadores:
    if i.cb_ganadas + i.cb_perdidas == 0:
        porcentaje = 0.0
    else:
        porcentaje= (i.cb_ganadas / (i.cb_ganadas + i.cb_perdidas))  * 100 
        if porcentaje >= 79:
            print(i.nombre,"batallas ganadas:", i.cb_ganadas,"batallas perdidas", i.cb_perdidas)
            print("Tiene un porcentaje de batallas ganadas de un: ", porcentaje, "%")

def P_tipo(lista_entrenadores):
    for i in range(0, lista_entrenadores.size()):
        
        valor = lista_entrenadores.get_element_by_index(i)
        for j in range(0, valor[1].size()):
            value = valor[1].get_element_by_index(j)
            if (value.tipo in 'agua' and value.subtipo in 'volador') or (value.tipo == 'fuego' and value.subtipo == 'planta')  :
                print(f'{valor[0].nombre} tiene su pokemon {value.nombre} tipo: {value.tipo} y subtipo: {value.subtipo}') 


def promediar(lista_entrenadores, x): 
    promedio = 0 
    cont = 0
    esto = lista_entrenadores.search(x, 'nombre')    
    
    if esto != None:
        value = lista_entrenadores.get_element_by_index(esto)
        for i in range(0, value[1].size()):
            valor = value[1].get_element_by_index(i)
                
            promedio = promedio + valor.nivel
            cont += 1    
              
        if cont > 0:
            final = promedio / cont  
            print(final)
        else:
            print('el entrenador no tiene pokemons')     

def P_especifico(lista_entrenadores, x):
    for i in range(0, lista_entrenadores.size()):
        
        value = lista_entrenadores.get_element_by_index(i)

        for j in range(0, value[1].size()):
            valor = value[1].get_element_by_index(j)
            if valor.nombre in x:
                print(value[0].nombre)

def P_repetidos(lista_entrenadores):
    entrenadores_por_pokemon = {}

    for i in range(lista_entrenadores.size()):
        entrenador = lista_entrenadores.get_element_by_index(i)
        for pokemon in range(entrenador[1].size()):
            nombre_pokemon = entrenador[1].get_element_by_index(pokemon).nombre
            if nombre_pokemon in entrenadores_por_pokemon:
                entrenadores_por_pokemon[nombre_pokemon].append(entrenador[0].nombre)
            else:
                entrenadores_por_pokemon[nombre_pokemon] = [entrenador[0].nombre]
                
    for nombre_pokemon, entrenador_list in entrenadores_por_pokemon.items():

        if len(entrenador_list) > 1:
            if len(entrenador_list) != len(set(entrenador_list)):
                print(f'{entrenador_list[0]} tiene mas de un {nombre_pokemon}')

def determinar_Pokemons(lista_entrenadores):
    for i in range(0, lista_entrenadores.size()):
        
        value = lista_entrenadores.get_element_by_index(i)

        for j in range(0, value[1].size()):
            valor = value[1].get_element_by_index(j)
            if valor.nombre in 'tyrantrum':
                print(f'{value[0].nombre} tiene a {valor.nombre}')
            if valor.nombre in 'terrakion':
                print(f'{value[0].nombre} tiene a {valor.nombre}')
            if valor.nombre in 'wingull':
                print(f'{value[0].nombre} tiene a {valor.nombre}')
            else:
                None

def Busqueda_E_P(lista_entrenadores, nombreentrenador, nombrepokemon):
    esto = lista_entrenadores.search(nombreentrenador, 'nombre')    
    if esto != None:
        value = lista_entrenadores.get_element_by_index(esto)
        entrenado, sublista = value[0], value[1]
        # print(f"{entrenado.nombre} tiene estos pokemones")
        # sublista.barrido()
        cont = 0
        for j in range(0, sublista.size()):
            valor = sublista.get_element_by_index(j)
            # print(valor.nombre)
            if valor.nombre in nombrepokemon:
                cont += 1
                print(nombreentrenador, " Tiene al pokemon ", nombrepokemon)
        if cont == 0:       
            print(f'no se encontro el pokemon {nombrepokemon}')


print("Entrenadores con Pokemons tipo fuego/planta o agua/volador")

print()

P_tipo(lista_entrenadores)

print()

print("Promedio de nivel de los Pokemons:")

print()

promediar(lista_entrenadores, "Juan")

print()

print("Entrenadores con pikachu: ")

print()

P_especifico(lista_entrenadores, "pikachu")

print()

print("Entrenadores con pokemones repetidos:")

print()

P_repetidos(lista_entrenadores)

print()

print("Entrenadores con: Tyrantrum, Terrakion, Wingull")

print()

determinar_Pokemons(lista_entrenadores)

print()

print("Entrenador Juan tiene a pikachu?")

print()

Busqueda_E_P(lista_entrenadores, "Juan", "pikachu")