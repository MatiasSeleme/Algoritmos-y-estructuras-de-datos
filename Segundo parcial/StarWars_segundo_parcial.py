class Grafo:
    def __init__(self, dirigido=False):
        self.__elements = []
        self.dirigido = dirigido


    def arbol_expansion_minima(self):
        def encontrar(conjunto, i):
            if conjunto[i] == i:
                return i
            return encontrar(conjunto, conjunto[i])
        
        def unir(conjunto, rango, x, y):
            x_raiz = encontrar(conjunto, x)
            y_raiz = encontrar(conjunto, y)

            if rango[x_raiz] < rango[y_raiz]:
                conjunto[x_raiz] = y_raiz
            elif rango[x_raiz] > rango[y_raiz]:
                conjunto[y_raiz] = x_raiz
            else:
                conjunto[y_raiz] = x_raiz
                rango[x_raiz] += 1


        arbol_exp_minimo = []


        aristas_ordenadas = sorted(self.get_all_edges(), key=lambda x: x[2])

        conjunto = []
        rango = []
        for i in range(self.size()):
            conjunto.append(i)
            rango.append(0)

        index_aristas = 0
        index_resultado = 0

        while index_resultado < self.size() - 1:
            u, v, peso = aristas_ordenadas[index_aristas]
            index_aristas += 1
            conjunto_u = encontrar(conjunto, u)
            conjunto_v = encontrar(conjunto, v)

            if conjunto_u != conjunto_v:
                index_resultado += 1
                arbol_exp_minimo.append([u, v, peso])
                unir(conjunto, rango, conjunto_u, conjunto_v)

        return arbol_exp_minimo

    def contiene_yoda(self):
        arbol_exp_minimo = self.arbol_expansion_minima()
        for arista in arbol_exp_minimo:
            if "Yoda" in arista:
                return True
        return False

    def maximo_episodios_compartidos(self):
        max_episodios = 0
        for vertice in self.__elements:
            for arista in vertice[1].get_elements():
                if arista.peso > max_episodios:
                    max_episodios = arista.peso
        return max_episodios