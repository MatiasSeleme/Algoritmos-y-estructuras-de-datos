class Documento:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad

    def __str__(self):
        return f"{self.nombre} (Prioridad: {self.prioridad})"


class ColaPrioridad:

    def __init__(self):
        self.vector = []

    def add_element(self, value):
        self.vector.append(value)
        self.flotar(len(self.vector)-1)

    def remove_element(self):
        self.vector[0], self.vector[-1] = self.vector[-1], self.vector[0]
        value = self.vector.pop()
        self.hundir(0)
        return value

    def flotar(self, index):
        while index > 0 and self.vector[index][0] > self.vector[(index-1)//2][0]:
            padre = (index-1)//2
            self.vector[index], self.vector[padre] = self.vector[padre], self.vector[index]
            index = padre

    def hundir(self, index):
        hijo_izq = (index*2) + 1
        control = True
        while control and hijo_izq < len(self.vector):
            hijo_der = hijo_izq + 1
            mayor = hijo_izq
            if hijo_der < len(self.vector):
                if self.vector[hijo_der][0] > self.vector[hijo_izq][0]:
                    mayor = hijo_der

            if self.vector[index][0] < self.vector[mayor][0]:
                self.vector[index], self.vector[mayor] = self.vector[mayor], self.vector[index]
                index = mayor
                hijo_izq = (index*2) + 1
            else:
                control = False

    def size(self):
        return len(self.vector)

    def montculizar(self):
        for i in range(len(self.vector)):
            self.flotar(i)

    def hepasort(self):
        vector = []
        for i in range(len(self.vector)):
            vector.append(self.remove_element())
        return vector

    def arrive(self, documento):
        self.add_element([documento.prioridad, documento])

    def atention(self):
        return self.remove_element()[1]


cola = ColaPrioridad()

cola.arrive(Documento("Documento 1", 1))
cola.arrive(Documento("Documento 2", 1))
cola.arrive(Documento("Documento 3", 1))

print("Imprimir primer documento:")
print(cola.atention())
print()

cola.arrive(Documento("Documento 4", 2))
cola.arrive(Documento("Documento 5", 2))

cola.arrive(Documento("Documento 6", 3))

print("Imprimir dos primeros documentos:")
print(cola.atention())
print(cola.atention())
print()

cola.arrive(Documento("Documento 7", 1))
cola.arrive(Documento("Documento 8", 1))
cola.arrive(Documento("Documento 9", 3))

print("Imprimir todos los documentos:")
while cola.size() > 0:
    print(cola.atention())


cola = ColaPrioridad()

cola.arrive(Documento("Documento 1", 1))
cola.arrive(Documento("Documento 2", 1))
cola.arrive(Documento("Documento 3", 1))

print("Imprimir primer documento:")
print(cola.atention())
print()

cola.arrive(Documento("Documento 4", 2))
cola.arrive(Documento("Documento 5", 2))

cola.arrive(Documento("Documento 6", 3))

print("Imprimir dos primeros documentos:")
print(cola.atention())
print(cola.atention())
print()

cola.arrive(Documento("Documento 7", 1))
cola.arrive(Documento("Documento 8", 1))
cola.arrive(Documento("Documento 9", 3))

print("Imprimir todos los documentos:")
while cola.size() > 0:
    print(cola.atention())