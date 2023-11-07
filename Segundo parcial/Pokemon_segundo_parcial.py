class Pokemon:
    def __init__(self, nombre, numero, tipo):
        self.nombre = nombre
        self.numero = numero
        self.tipo = tipo

class PokemonTree:
    class Node:
        def __init__(self, pokemon):
            self.pokemon = pokemon
            self.left = None
            self.right = None

    def __init__(self, index):
        self.root = None
        self.index = index

    def insertar_pokemon(self, pokemon):
        new_node = self.Node(pokemon)
        if self.index == 'nombre':
            key = pokemon.nombre
        elif self.index == 'numero':
            key = pokemon.numero
        elif self.index == 'tipo':
            key = pokemon.tipo

        if not self.root:
            self.root = new_node
        else:
            current = self.root
            while True:
                if self.index == 'nombre' and key.lower() < current.pokemon.nombre.lower():
                    if current.left is None:
                        current.left = new_node
                        break
                    current = current.left
                elif self.index == 'nombre' and key.lower() > current.pokemon.nombre.lower():
                    if current.right is None:
                        current.right = new_node
                        break
                    current = current.right
                elif self.index == 'numero' and key < current.pokemon.numero:
                    if current.left is None:
                        current.left = new_node
                        break
                    current = current.left
                elif self.index == 'numero' and key > current.pokemon.numero:
                    if current.right is None:
                        current.right = new_node
                        break
                    current = current.right
                elif self.index == 'tipo' and key < current.pokemon.tipo:
                    if current.left is None:
                        current.left = new_node
                        break
                    current = current.left
                elif self.index == 'tipo' and key > current.pokemon.tipo:
                    if current.right is None:
                        current.right = new_node
                        break
                    current = current.right

    def buscar_por_nombre(self, name):
        name = name.lower()
        current = self.root
        while current:
            if name == current.pokemon.nombre.lower() or current.pokemon.nombre.lower().startswith(name):
                return current.pokemon
            elif name < current.pokemon.nombre.lower():
                current = current.left
            else:
                current = current.right
        return None

    def obtener_tipo(self, type):
        result = []
        type = type.lower()
        self._obtener_tipo(self.root, type, result)
        return result

    def _obtener_tipo(self, node, type, result):
        if node:
            if node.pokemon.tipo.lower() == type:
                result.append(node.pokemon.nombre)
            self._obtener_tipo(node.left, type, result)
            self._obtener_tipo(node.right, type, result)

    def barrido_en_orden(self):
        result = []
        self._barrido_en_orden(self.root, result)
        return result

    def _barrido_en_orden(self, node, result):
        if node:
            self._barrido_en_orden(node.left, result)
            result.append(node.pokemon.nombre)
            self._barrido_en_orden(node.right, result)

tree_name = PokemonTree('nombre')
tree_number = PokemonTree('numero')
tree_type = PokemonTree('tipo')

pokemon_data = [
    {"nombre": "Bulbasaur", "numero": 1, "tipo": "planta"},
    {"nombre": "Pikachu", "numero": 25, "tipo": "eléctrico"},
    {"nombre": "Charmander", "numero": 4, "tipo": "fuego"},
    {"nombre": "Squirtle", "numero": 7, "tipo": "agua"},
]
for pokemon_info in pokemon_data:
    pokemon = Pokemon(pokemon_info['nombre'], pokemon_info['numero'], pokemon_info['tipo'])
    tree_name.insertar_pokemon(pokemon)
    tree_number.insertar_pokemon(pokemon)
    tree_type.insertar_pokemon(pokemon)


print(tree_name.buscar_por_nombre('Bul')) 
print(tree_type.obtener_tipo('planta'))
print(tree_number.barrido_en_orden())