personajes = [
    {"nombre": "Iron Man", "cantidad de películas": 7},
    {"nombre": "Captain America", "cantidad de películas": 5},
    {"nombre": "Thor", "cantidad de películas": 6},
    {"nombre": "Rocket Raccoon", "cantidad de películas": 3},
    {"nombre": "Black Widow", "cantidad de películas": 8},
    {"nombre": "Groot", "cantidad de películas": 4},
    {"nombre": "Hulk", "cantidad de películas": 9},
    {"nombre": "Loki", "cantidad de películas": 7},
    {"nombre": "Spiderman", "cantidad de películas": 12},
    {"nombre": "Doctor Strange", "cantidad de películas": 6},
]
def rocket(personajes):
    for i, personaje in enumerate(personajes, start=1):
        if personaje["nombre"] == "Rocket Raccoon":
            return i
    return None
print(rocket(personajes))
def groot(personajes):
    for j, personaje in enumerate(personajes, start=1):
        if personaje["nombre"] == "Groot":
            return j
    return None
print(groot(personajes))

def personajes_5_peliculas(personajes):
    personajes_5 = []
    for personaje in personajes:
        if personaje["cantidad de películas"] > 5:
            personajes_5.append((personaje["nombre"], personaje["cantidad de películas"]))
    return personajes_5
personajes_destacados = personajes_5_peliculas(personajes)
for personaje, cantidad_peliculas in personajes_destacados:
    print(f"{personaje} participó en {cantidad_peliculas} películas.")

def black_widow(personajes):
    for personaje in personajes:
        if personaje["nombre"] == "Black Widow":
            return personaje["cantidad de películas"]
    return 0
print(black_widow(personajes))

#d)
def personajes_letras(personajes, letras):
    personajes_inicial = [personaje["nombre"] for personaje in personajes if personaje["nombre"][0] in letras]
    return personajes_inicial
print(personajes_letras(personajes, ['C', 'D', 'G']))
