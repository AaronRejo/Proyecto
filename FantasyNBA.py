
# Bienvenida

print('Bienvenidos a Fantasy Basketball')
print('Selecciona tu equipo con un presupuesto de $80')


# Jugadores y precios

jugadores = ['Lebron James', 'Stephen Curry',
             'Nikola Jokic', 'Jason Tatum']

precios = [40, 35, 32, 25]

puntos = [28, 30, 27, 26]
rebotes = [8, 5, 12, 9]
asistencias = [7, 6, 10, 5]


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

print('Selecciona dos jugadores con un presupuesto de $80')

for i in range(len(jugadores)):
    print(i + 1, jugadores[i], '- $' + str(precios[i]))


# Selección de jugadores con ciclo

equipo = []
presupuesto = 80

while len(equipo) < 2:
    seleccion = int(input('Pon número de jugador (1-4): '))

    if seleccion < 1 or seleccion > 4:
        print('Opción inválida. Intenta otra vez.')

    elif seleccion - 1 in equipo:
        print('Ya seleccionaste ese jugador. Elige otro.')

    elif precios[seleccion - 1] > presupuesto:
        print('No tienes suficiente presupuesto.')

    else:
        equipo.append(seleccion - 1)
        presupuesto -= precios[seleccion - 1]
        print('Jugador agregado:', jugadores[seleccion - 1])
        print('Presupuesto restante:', presupuesto)


# Mostrar equipo y calcular puntos

print('\nTu equipo es:')

puntos_totales = 0

for jugador in equipo:
    print(jugadores[jugador])

    fantasy = calcular_fantasy(
        puntos[jugador],
        rebotes[jugador],
        asistencias[jugador]
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


