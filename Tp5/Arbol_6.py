class Jedi:
    def __init__(self, nombre, especie, anio_nacimiento, color_sable, rango, maestros):
        self.nombre = nombre
        self.especie = especie
        self.anio_nacimiento = anio_nacimiento
        self.color_sable = color_sable
        self.rango = rango
        self.maestros = maestros

class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class RegistroJedi:
    def __init__(self):
        self.raiz_nombre = None
        self.raiz_rango = None
        self.raiz_especie = None

    def insertar_por_nombre(self, jedi):
        self.raiz_nombre = self._insertar_por_nombre(self.raiz_nombre, jedi)

    def insertar_por_rango(self, jedi):
        self.raiz_rango = self._insertar_por_rango(self.raiz_rango, jedi)

    def insertar_por_especie(self, jedi):
        self.raiz_especie = self._insertar_por_especie(self.raiz_especie, jedi)

    def _insertar_por_nombre(self, raiz, jedi):
        if raiz is None:
            return NodoArbol(jedi)
        if jedi.nombre < raiz.dato.nombre:
            raiz.izquierda = self._insertar_por_nombre(raiz.izquierda, jedi)
        else:
            raiz.derecha = self._insertar_por_nombre(raiz.derecha, jedi)
        return raiz

    def _insertar_por_rango(self, raiz, jedi):
        if raiz is None:
            return NodoArbol(jedi)
        if jedi.rango < raiz.dato.rango:
            raiz.izquierda = self._insertar_por_rango(raiz.izquierda, jedi)
        else:
            raiz.derecha = self._insertar_por_rango(raiz.derecha, jedi)
        return raiz

    def _insertar_por_especie(self, raiz, jedi):
        if raiz is None:
            return NodoArbol(jedi)
        if jedi.especie < raiz.dato.especie:
            raiz.izquierda = self._insertar_por_especie(raiz.izquierda, jedi)
        else:
            raiz.derecha = self._insertar_por_especie(raiz.derecha, jedi)
        return raiz

    def recorrido_inorden(self, raiz, atributo):
        if raiz is not None:
            self.recorrido_inorden(raiz.izquierda, atributo)
            if atributo == "nombre":
                print(f"Nombre: {raiz.dato.nombre}, Especie: {raiz.dato.especie}, Rango: {raiz.dato.rango}")
            elif atributo == "rango":
                print(f"Rango: {raiz.dato.rango}, Nombre: {raiz.dato.nombre}, Especie: {raiz.dato.especie}")
            self.recorrido_inorden(raiz.derecha, atributo)

    def recorrido_por_nivel(self, raiz, atributo):
        if raiz is None:
            return
        cola = []
        cola.append(raiz)
        while cola:
            actual = cola.pop(0)
            if atributo == "rango":
                print(f"Rango: {actual.dato.rango}, Nombre: {actual.dato.nombre}, Especie: {actual.dato.especie}")
            elif atributo == "especie":
                print(f"Especie: {actual.dato.especie}, Nombre: {actual.dato.nombre}, Rango: {actual.dato.rango}")
            if actual.izquierda:
                cola.append(actual.izquierda)
            if actual.derecha:
                cola.append(actual.derecha)

    def encontrar_jedi(self, nombre):
        return self._encontrar_jedi(self.raiz_nombre, nombre)

    def _encontrar_jedi(self, raiz, nombre):
        if raiz is None:
            return None
        if nombre == raiz.dato.nombre:
            return raiz.dato
        if nombre < raiz.dato.nombre:
            return self._encontrar_jedi(raiz.izquierda, nombre)
        else:
            return self._encontrar_jedi(raiz.derecha, nombre)

    def obtener_jedi_por_rango(self, rango):
        resultados = []
        self._obtener_jedi_por_rango(self.raiz_rango, rango, resultados)
        return resultados

    def _obtener_jedi_por_rango(self, raiz, rango, resultados):
        if raiz is None:
            return
        if rango == raiz.dato.rango:
            resultados.append(raiz.dato)
        if rango < raiz.dato.rango:
            self._obtener_jedi_por_rango(raiz.izquierda, rango, resultados)
        else:
            self._obtener_jedi_por_rango(raiz.derecha, rango, resultados)

    def obtener_jedi_por_color_sable(self, color):
        resultados = []
        self._obtener_jedi_por_color_sable(self.raiz_nombre, color, resultados)
        return resultados

    def _obtener_jedi_por_color_sable(self, raiz, color, resultados):
        if raiz is not None:
            self._obtener_jedi_por_color_sable(raiz.izquierda, color, resultados)
            if color in raiz.dato.color_sable:
                resultados.append(raiz.dato)
            self._obtener_jedi_por_color_sable(raiz.derecha, color, resultados)

    def obtener_jedi_con_maestros(self, maestros):
        resultados = []
        self._obtener_jedi_con_maestros(self.raiz_rango, maestros, resultados)
        return resultados

    def _obtener_jedi_con_maestros(self, raiz, maestros, resultados):
        if raiz is not None:
            self._obtener_jedi_con_maestros(raiz.izquierda, maestros, resultados)
            if any(maestro in raiz.dato.maestros for maestro in maestros):
                resultados.append(raiz.dato)
            self._obtener_jedi_con_maestros(raiz.derecha, maestros, resultados)

    def obtener_jedi_por_especie(self, especies):
        resultados = []
        self._obtener_jedi_por_especie(self.raiz_especie, especies, resultados)
        return resultados

    def _obtener_jedi_por_especie(self, raiz, especies, resultados):
        if raiz is not None:
            self._obtener_jedi_por_especie(raiz.izquierda, especies, resultados)
            if raiz.dato.especie in especies:
                resultados.append(raiz.dato)
            self._obtener_jedi_por_especie(raiz.derecha, especies, resultados)

    def obtener_jedi_por_nombre_comienza_con_a_o_contiene_guion(self):
        resultados = []
        self._obtener_jedi_por_nombre_comienza_con_a_o_contiene_guion(self.raiz_nombre, resultados)
        return resultados

    def _obtener_jedi_por_nombre_comienza_con_a_o_contiene_guion(self, raiz, resultados):
        if raiz is not None:
            self._obtener_jedi_por_nombre_comienza_con_a_o_contiene_guion(raiz.izquierda, resultados)
            if raiz.dato.nombre.startswith('A') or '-' in raiz.dato.nombre:
                resultados.append(raiz.dato)
            self._obtener_jedi_por_nombre_comienza_con_a_o_contiene_guion(raiz.derecha, resultados)


registro_jedi = RegistroJedi()

registro_jedi.insertar_por_nombre(Jedi("Yoda", "Desconocida", 896, "verde", "Maestro Jedi", []))
registro_jedi.insertar_por_nombre(Jedi("Luke Skywalker", "Humano", 19, "verde", "Caballero Jedi", ["Yoda"]))
registro_jedi.insertar_por_nombre(Jedi("Obi-Wan Kenobi", "Humano", 57, "azul", "Maestro Jedi", ["Yoda"]))
registro_jedi.insertar_por_nombre(Jedi("Mace Windu", "Humano", 72, "morado", "Maestro Jedi", ["Yoda"]))
registro_jedi.insertar_por_nombre(Jedi("Ahsoka Tano", "Togruta", 36, "verde", "Caballero Jedi", ["Anakin Skywalker"]))
registro_jedi.insertar_por_nombre(Jedi("Qui-Gon Jinn", "Humano", 60, "verde", "Maestro Jedi", ["Count Dooku"]))
registro_jedi.insertar_por_nombre(Jedi("Rey", "Humano", 19, "azul", "Caballero Jedi", ["Luke Skywalker"]))

print("Barrido por nombre:")
print()

registro_jedi.recorrido_inorden(registro_jedi.raiz_nombre, "nombre")
print()

print("Barrido por rango:")
registro_jedi.recorrido_inorden(registro_jedi.raiz_rango, "rango")
print()

print("Barrido por nivel:")
registro_jedi.recorrido_por_nivel(registro_jedi.raiz_rango, "rango")
print()

print("Barrido por especie:")
registro_jedi.recorrido_por_nivel(registro_jedi.raiz_especie, "especie")
print()

yoda_info = registro_jedi.encontrar_jedi("Yoda")
luke_skywalker_info = registro_jedi.encontrar_jedi("Luke Skywalker")
if yoda_info:
    print("Yoda:", yoda_info.__dict__)
if luke_skywalker_info:
    print("Luke Skywalker:", luke_skywalker_info.__dict__)
print()

jedi_maestros = registro_jedi.obtener_jedi_por_rango("Maestro Jedi")
print("Maestros Jedi:")
for jedi in jedi_maestros:
    print(jedi.__dict__)
print()

usuarios_sable_verde = registro_jedi.obtener_jedi_por_color_sable("verde")
print("Usan sables verdes:")
for jedi in usuarios_sable_verde:
    print(jedi.__dict__)
print()

jedi_con_maestros = registro_jedi.obtener_jedi_con_maestros(["Yoda"])
print("Jedi con Yoda como maestro:")
for jedi in jedi_con_maestros:
    print(jedi.__dict__)
print()

especies_especificas = registro_jedi.obtener_jedi_por_especie(["Togruta", "Cerean"])
print("Especie Togruta o Cerean:")
for jedi in especies_especificas:
    print(jedi.__dict__)
print()

jedi_especiales = registro_jedi.obtener_jedi_por_nombre_comienza_con_a_o_contiene_guion()
print("Nombres que empiezan con A o contienen un -:")
for jedi in jedi_especiales:
    print(jedi.__dict__)