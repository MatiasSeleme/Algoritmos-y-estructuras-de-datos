avengers = [
    ('Star Lord', 'Peter Quill', 'Guardianes de la galaxia', 1976),
    ('Capitana Marvel', 'Carol Danvers', '', 2012),
    ('Iron Man', 'Tony Stark', 'Iron Man', 1963),
    ('Vlanck Widow', 'Natasha Romanoff', 'Avengers', 1964),
    ('Capitan America', 'Steve Rogers', 'Capitan America', 1941),
    ('Thor', '', 'Avengers', 1962),
    ('Hulk', '', 'Avengers', 1962),
    ('Hawkeye', 'Clint Barton', 'Avengers', 1964),
    ('Black Panther', 'T\'Challa', 'Avengers', 1966),
    ('Scarlet Witch', 'Wanda Maximoff', 'Avengers', 1964)
]
#a
found = False
character_name = ''

for hero in avengers:
    if hero[0] == 'Capitana Marvel':
        found = True
        character_name = hero[1]
        break

if found:
    print(f"El nombre de Capitana Marvel es: {character_name}")
else:
    print("Capitana Marvel no está en la lista.")
#h
additional_heroes = [
    ('Spider-Man', 'Peter Parker', '', 1962),
    ('Doctor Strange', 'Stephen Strange', '', 1963),
    ('Wolverine', 'Logan', '', 1974),
    ('Vision', '', '', 1968),
    ('Falcon', 'Sam Wilson', '', 1969),
    ('Ant-Man', 'Scott Lang', '', 1962),
    ('Winter Soldier', 'Bucky Barnes', '', 2005),
    ('Gamora', '', 'Guardianes de la galaxia', 1975),
    ('Groot', '', 'Guardianes de la galaxia', 1960),
    ('Rocket Raccoon', '', 'Guardianes de la galaxia', 1976),
    ('Mantis', '', 'Guardianes de la galaxia', 1973),
    ('Silver Surfer', '', 'Los cuatro fantásticos', 1966),
    ('Invisible Woman', 'Susan Storm', 'Los cuatro fantásticos', 1961),
    ('Mr. Fantastic', 'Reed Richards', 'Los cuatro fantásticos', 1961),
    ('Thing', 'Ben Grimm', 'Los cuatro fantásticos', 1961),
    ('Deadpool', 'Wade Wilson', '', 1991),
    ('Cyclops', 'Scott Summers', 'X-Men', 1963),
    ('Jean Grey', '', 'X-Men', 1963),
    ('Storm', 'Ororo Munroe', 'X-Men', 1975),
    ('Beast', 'Hank McCoy', 'X-Men', 1963)
]

avengers.extend(additional_heroes)
#b
from collections import deque

guardians_queue = deque()
count_guardians = 0

for hero in avengers:
    if hero[2] == 'Guardianes de la galaxia':
        guardians_queue.append(hero[0])
        count_guardians += 1

print(f"La cantidad de superhéroes de Guardianes de la galaxia son: {count_guardians}")
#c
group_heroes = []
for hero in avengers:
    if hero[2] == 'Los cuatro fantásticos' or hero[2] == 'Guardianes de la galaxia':
        group_heroes.append(hero[0])

        

group_heroes.sort(reverse=True)

print("Superhéroes de 'Los cuatro fantásticos' y 'Guardianes de la galaxia' en orden descendente:")
for hero in group_heroes:
    print(hero)
    
#e
for i, hero in enumerate(avengers):
    if hero[0] == 'Vlanck Widow':
        avengers[i] = ('Black Widow', hero[1], hero[2], hero[3])
        
#d
print("Los personajes que aparecieron posterior a 1960 son: ")
for hero in avengers:
    if hero[1] != '' and hero[3] > 1960:
        print(hero[0])


#f
aux_characters = ['Black Cat', 'Hulk', 'Rocket Racoonn', 'Loki']

for character in aux_characters:
    found = False
    for hero in avengers:
        if character.lower() == hero[0].lower():
            found = True
            break
    if not found:
        avengers.append((character, '', '', ''))

#g
for hero in avengers:
    if hero[0][0] in ['C', 'P', 'S']:
        print(hero[0])


