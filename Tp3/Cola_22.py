class Cola:

    def __init__(self):
        self.__elementos = []

    def arrive(self, value):
        self.__elementos.append(value)

    def atention(self):
        if self.size() > 0:
            return self.__elementos.pop(0)

    def size(self):
        return len(self.__elementos)

    def on_front(self):
        if self.size() > 0:
            return self.__elementos[0]

    def move_to_end(self):
        if self.size() > 0:
            aux = self.atention()
            self.arrive(aux)
            return aux

    def buscar_por_nombre(self, nombre):
        for elemento in self.__elementos:
            if elemento[0] == nombre:
                return elemento
        return None

    def superheroes_femeninos(self):
        return [elemento for elemento in self.__elementos if elemento[2] == 'F']

    def personajes_masculinos(self):
        return [elemento for elemento in self.__elementos if elemento[2] == 'M']

    def superheroe_de_personaje(self, nombre_personaje):
        for elemento in self.__elementos:
            if elemento[0] == nombre_personaje:
                return elemento[1]
        return None

    def datos_por_inicial(self, inicial):
        return [elemento for elemento in self.__elementos if elemento[0].startswith(inicial)]

    def buscar_carol_danvers(self):
        for elemento in self.__elementos:
            if elemento[0] == 'Carol Danvers':
                return elemento[1]
        return None

cola_personajes = Cola()
cola_personajes.arrive(('Tony Stark', 'Iron Man', 'M'))
cola_personajes.arrive(('Steve Rogers', 'Capitán América', 'M'))
cola_personajes.arrive(('Natasha Romanoff', 'Black Widow', 'F'))
cola_personajes.arrive(('Scott Lang', 'Ant-Man', 'M'))
cola_personajes.arrive(('Carol Danvers', 'Capitana Marvel', 'F'))
cola_personajes.arrive(('Sam Wilson', 'Falcon', 'M'))
cola_personajes.arrive(('Scarlet Witch', 'Wanda Maximoff', 'F'))

nombre_capitana_marvel = cola_personajes.superheroe_de_personaje('Capitana Marvel')
print(f"a. Nombre del personaje de la superhéroe Capitana Marvel: {nombre_capitana_marvel}")

superheroes_femeninos = cola_personajes.superheroes_femeninos()
print("b. Nombres de los superhéroes femeninos:")
for elemento in superheroes_femeninos:
    print(elemento[1])

personajes_masculinos = cola_personajes.personajes_masculinos()
print("c. Nombres de los personajes masculinos:")
for elemento in personajes_masculinos:
    print(elemento[0])

superheroe_scott_lang = cola_personajes.superheroe_de_personaje('Scott Lang')
print(f"d. Nombre del superhéroe del personaje Scott Lang: {superheroe_scott_lang}")

personajes_con_s = cola_personajes.datos_por_inicial('S')
print("e. Datos de los superhéroes o personajes cuyos nombres comienzan con la letra S:")
for elemento in personajes_con_s:
    print(elemento)

nombre_superheroe_carol_danvers = cola_personajes.buscar_carol_danvers()
if nombre_superheroe_carol_danvers:
    print(f"f. Carol Danvers se encuentra en la cola y su nombre de superhéroe es: {nombre_superheroe_carol_danvers}")
else:
    print("f. Carol Danvers no se encuentra en la cola.")