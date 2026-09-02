#Introducción

print('Bienvenidos a Fantasy Basketball')
print('Seleccióna tu equipo con un presupeusto de $80')

#Selección de Jugadores

presupuesto = 80

print('Sleccióna dos jugadores maximo')
print('1. Lebron James - $40')
print('2. Stephen Curry - $35')
print('3. Nikola Jokic - $32')
print('4. Jason Tatum - $25')

jugador1 = 'Lebron James'
jugador2 = 'Stephen Curry'
jugador3 = 'Nikola Jokic'
jugador4 = 'Jason Tatum'

seleccion1 = int(input('pon numero de jugador: '))
seleccion2 = int(input('pon numero de jugador: '))

if seleccion1 == 1 and seleccion2 == 2:
    print('presupuesto: ', presupuesto - 75)
    print('Equipo: ', jugador1, ' ', jugador2)

if seleccion1 == 1 and seleccion2 == 3:
    print('Equipo: ', jugador1, ' ', jugador3)
    print('presupuesto: ', presupuesto - 72)

if seleccion1 == 1 and seleccion2 == 4:
    print('presupuesto: ', presupuesto - 15)
    print('Equipo: ', jugador1, ' ', jugador4)

if seleccion1 == 2 and seleccion2 == 3:
    print('presupuesto: ', presupuesto - 67)
    print('Equipo: ', jugador2, ' ', jugador3)

if seleccion1 == 2 and seleccion2 == 4:
    print('presupuesto: ', presupuesto - 60)
    print('Equipo: ', jugador2, ' ', jugador4)

if seleccion1 == 3 and seleccion2 == 4:
    print('presupuesto: ', presupuesto - 57)
    print('Equipo: ', jugador3, ' ', jugador4)


# Estadísticas de los jugadores

print('\nEstadísticas de los jugadores')

# Lebron James
puntos1 = 28
rebotes1 = 8
asistencias1 = 7

# Stephen Curry
puntos2 = 30
rebotes2 = 5
asistencias2 = 6

# Nikola Jokic
puntos3 = 27
rebotes3 = 12
asistencias3 = 10

# Jason Tatum
puntos4 = 26
rebotes4 = 9
asistencias4 = 5

#Equipo Falso test

equipo_falso = 86

# Puntos Fantasy

fantasy1 = puntos1 + rebotes1 + asistencias1
fantasy2 = puntos2 + rebotes2 + asistencias2
fantasy3 = puntos3 + rebotes3 + asistencias3
fantasy4 = puntos4 + rebotes4 + asistencias4


# Puntos totales del equipo

print('\nPuntos Fantasy:')

if seleccion1 == 1 and seleccion2 == 2:
    print('Puntos totales del equipo:', fantasy1 + fantasy2)
    print('Otro Equipo: ', equipo_falso)
    if fantasy1 + fantasy2 > equipo_falso:
        print('GANASTE')
    else:
        print('PERDISTE')
    

if seleccion1 == 1 and seleccion2 == 3:
    print('Puntos totales del equipo:', fantasy1 + fantasy3)
    print('Otro Equipo: ', equipo_falso)
    if fantasy1 + fantasy3 > equipo_falso:
        print('GANASTE')
    else:
        print('PERDISTE')

if seleccion1 == 1 and seleccion2 == 4:
    print('Puntos totales del equipo:', fantasy1 + fantasy4)
    print('Otro Equipo: ', equipo_falso)
    if fantasy1 + fantasy4 > equipo_falso:
        print('GANASTE')
    else:
        print('PERDISTE')

if seleccion1 == 2 and seleccion2 == 3:
    print('Puntos totales del equipo:', fantasy2 + fantasy3)
    print('Otro Equipo: ', equipo_falso)
    if fantasy2 + fantasy3 > equipo_falso:
        print('GANASTE')

if seleccion1 == 2 and seleccion2 == 4:
    print('Puntos totales del equipo:', fantasy2 + fantasy4)
    print('Otro Equipo: ', equipo_falso)
    if fantasy2 + fantasy4 > equipo_falso:
        print('GANASTE')
    else:
        print('PERDISTE')

if seleccion1 == 3 and seleccion2 == 4:
    print('Puntos totales del equipo:', fantasy3 + fantasy4)
    print('Otro Equipo: ', equipo_falso)
    if fantasy3 + fantasy4 > equipo_falso:
        print('GANASTE')
    else:
        print('PERDISTE')
    
