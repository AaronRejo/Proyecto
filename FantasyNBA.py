
# Bienvenida
print('Bienvenidos a Fantasy Basketball')
print('Selecciona tu equipo con un presupuesto de $80')

# Jugadores organizados en una matriz
# [Nombre, Precio, Puntos, Rebotes, Asistencias]

jugadores = [
    ['Lebron James', 40, 28, 8, 7],
    ['Stephen Curry', 35, 30, 5, 6],
    ['Nikola Jokic', 32, 27, 12, 10],
    ['Jason Tatum', 25, 26, 9, 5]
]

# Funciones
def calcular_fantasy(puntos, rebotes, asistencias):
    return puntos + rebotes + asistencias

def comparar_equipos(puntos_equipo, otro_equipo):
    if puntos_equipo > otro_equipo:
        return 'GANASTE'
    elif puntos_equipo == otro_equipo:
        return 'EMPATE'
    else:
        return 'PERDISTE'

# Mostrar jugadores
print('\nSelecciona dos jugadores con un presupuesto de $80')

for i in range(len(jugadores)):
    print(i + 1, jugadores[i][0], '- $' + str(jugadores[i][1]))

# Selección de jugadores
equipo = []
presupuesto = 80

while len(equipo) < 2:
    seleccion = int(input('Pon número de jugador (1-4): '))

    if seleccion < 1 or seleccion > 4:
        print('Opción inválida. Intenta otra vez.')

    elif seleccion - 1 in equipo:
        print('Ya seleccionaste ese jugador. Elige otro.')

    elif jugadores[seleccion - 1][1] > presupuesto:
        print('No tienes suficiente presupuesto.')

    else:
        equipo.append(seleccion - 1)
        presupuesto -= jugadores[seleccion - 1][1]
        print('Jugador agregado:', jugadores[seleccion - 1][0])
        print('Presupuesto restante:', presupuesto)

# Mostrar equipo y calcular puntos
print('\nTu equipo es:')

puntos_totales = 0

for indice in equipo:
    jugador = jugadores[indice]

    print(jugador[0])

    fantasy = calcular_fantasy(
        jugador[2],
        jugador[3],
        jugador[4]
    )

    print('Puntos Fantasy del jugador:', fantasy)
    puntos_totales += fantasy

# Resultado
equipo_falso = 86

print('\nPuntos totales de tu equipo:', puntos_totales)
print('Puntos del otro equipo:', equipo_falso)

resultado = comparar_equipos(puntos_totales, equipo_falso)
print('Resultado:', resultado)
print('Presupuesto final:', presupuesto)
