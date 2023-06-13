bitacora = [
    {"planeta": "Tatooine", "captura": "Jabba el Hutt", "recompensa": 1000},
    {"planeta": "Coruscant", "captura": "Greedo", "recompensa": 500},
    {"planeta": "Bespin", "captura": "Lando Calrissian", "recompensa": 800},
    {"planeta": "Endor", "captura": "Wicket W. Warrick", "recompensa": 300},
    {"planeta": "Hoth", "captura": "Han Solo", "recompensa": 2000},
]

# a
planetas_visitados = [mision["planeta"] for mision in bitacora]
print("Planetas visitados en orden:")
print('\n'.join(planetas_visitados))

# b
total_creditos = sum(mision["recompensa"] for mision in bitacora)
print("Total de créditos galácticos recaudados:", total_creditos)

# c
han_solo_mision = next((i + 1 for i, mision in enumerate(bitacora) if mision["captura"] == "Han Solo"), None)
planeta_captura = next((mision["planeta"] for mision in bitacora if mision["captura"] == "Han Solo"), None)

print("Número de la misión en la que capturó a Han Solo:", han_solo_mision)
print("Planeta de la captura de Han Solo:", planeta_captura)
