
peliculas = [
    {"título": "Maze Runner: correr o morir", "estudio": "20th Century Studios", "año de estreno": 2014},
    {"título": "Guardianes de la galaxia", "estudio": "Marvel", "año de estreno": 2014},
    {"título": "Creed II", "estudio": "Warner Bros", "año de estreno": 2018},
    {"título": "Doctor Strange", "estudio": "Marvel", "año de estreno": 2016},
    {"título": "Batman vs Superman: el origen de la justicia", "estudio": "DC", "año de estreno": 2016},
    {"título": "Capitan America: civil war", "estudio": "Marvel", "año de estreno": 2016}
]

def peliculas_2014(peliculas):
    peliculas_2014 = [p["título"] for p in peliculas if p["año de estreno"] == 2014]
    return peliculas_2014
print(peliculas_2014(peliculas))

def peliculas_2018(peliculas):
    cantidad_peliculas_2018 = sum(1 for p in peliculas if p["año de estreno"] == 2018)
    return cantidad_peliculas_2018
print(peliculas_2018(peliculas))

def peliculas_marvel_2016(peliculas):
    peliculas_marvel_2016 = [p["título"] for p in peliculas if p["estudio"] == "Marvel" and p["año de estreno"] == 2016]
    return peliculas_marvel_2016
print(peliculas_marvel_2016(peliculas))
