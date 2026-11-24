#Bienvenida

print('Bienvenidos a Fantasy Basketball')

print('Selecciona tu equipo con un presupuesto de $80')


#Introducción

nombre_equipo = input('Escribe el nombre de tu equipo: ')

nombre_equipo = nombre_equipo.strip()

while len(nombre_equipo) == 0:

    print('El nombre no puede estar vacio')

    nombre_equipo = input('Escribe el nombre de tu equipo: ')

    nombre_equipo = nombre_equipo.strip()

nombre_equipo = nombre_equipo.capitalize()

print('Nombre de tu equipo:', nombre_equipo.upper())

nombre_codigo = nombre_equipo.replace(' ', '_')

print('Identificador del equipo:', nombre_codigo)


#Jugadores

#Leer información de los jugadores desde archivo

jugadores = []

archivo = open('jugadores.txt', 'r')

for linea in archivo:

    datos = linea.strip().split(',')

    jugador = [datos[0], int(datos[1]), int(datos[2]),
               int(datos[3]), int(datos[4])]

    jugadores.append(jugador)

archivo.close()


#Funciones

def calcular_fantasy(puntos, rebotes, asistencias):

    return puntos + rebotes + asistencias


def comparar_equipos(puntos_equipo, otro_equipo):

    if puntos_equipo > otro_equipo:

        return 'GANASTE'

    elif puntos_equipo == otro_equipo:

        return 'EMPATE'

    else:

        return 'PERDISTE'


#Mostrar jugadores

print('Selecciona dos jugadores con un presupuesto de $80')

for i in range(len(jugadores)):

    print(i + 1, jugadores[i][0], '- $' + str(jugadores[i][1]))


#Selección de jugadores

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

print('Equipo:', nombre_equipo.upper())

puntos_totales = 0

for indice in equipo:

    jugador = jugadores[indice]

    print(jugador[0])

    fantasy = calcular_fantasy(jugador[2], jugador[3], jugador[4])

    print('Puntos Fantasy del jugador:', fantasy)

    puntos_totales += fantasy


#Resultado

equipo_falso = 86

print('Puntos totales de tu equipo:', puntos_totales)

print('Puntos del otro equipo:', equipo_falso)

resultado = comparar_equipos(puntos_totales, equipo_falso)

print('Resultado:', resultado)

print('Presupuesto final:', presupuesto)


#Guardar datos

archivo = open('resultados_fantasy.txt', 'a')

archivo.write('Equipo: ' + nombre_equipo + '\n')

archivo.write('Jugadores:\n')

for indice in equipo:

    archivo.write(jugadores[indice][0] + '\n')

archivo.write('Puntos totales: ' + str(puntos_totales) + '\n')

archivo.write('Resultado: ' + resultado + '\n')

archivo.write('Presupuesto final: ' + str(presupuesto) + '\n')

archivo.write('-------------------------\n')

archivo.close()
