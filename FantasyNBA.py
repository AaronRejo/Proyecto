# Bienvenida

print('Bienvenidos a Fantasy Basketball')
print('Selecciona tu equipo con un presupuesto de $80')


# Funciones Obtener jugadores

def obtener_jugador(numero):
    if numero == 1:
        return 'Lebron James'
    elif numero == 2:
        return 'Stephen Curry'
    elif numero == 3:
        return 'Nikola Jokic'
    elif numero == 4:
        return 'Jason Tatum'

# Funciones Obtener Precio

def obtener_precio(numero):
    if numero == 1:
        return 40
    elif numero == 2:
        return 35
    elif numero == 3:
        return 32
    elif numero == 4:
        return 25


# Funciones calculos

def calcular_presupuesto(precio1, precio2):
    return 80 - precio1 - precio2


def calcular_fantasy(puntos, rebotes, asistencias):
    return puntos + rebotes + asistencias


def comparar_equipos(puntos_equipo, otro_equipo):
    if puntos_equipo > otro_equipo:
        return 'GANASTE'
    else:
        return 'PERDISTE'


# Selección de jugadores

presupuesto = 80

print('Selecciona dos jugadores máximo')
print('1. Lebron James - $40')
print('2. Stephen Curry - $35')
print('3. Nikola Jokic - $32')
print('4. Jason Tatum - $25')

seleccion1 = int(input('Pon número de jugador: '))
seleccion2 = int(input('Pon número de jugador: '))


# Obtener jugadores y precios

nombre1 = obtener_jugador(seleccion1)
nombre2 = obtener_jugador(seleccion2)

precio1 = obtener_precio(seleccion1)
precio2 = obtener_precio(seleccion2)


# Mostrar equipo

print('Equipo:', nombre1, nombre2)


# Presupuesto

presupuesto_restante = calcular_presupuesto(precio1, precio2)

print('Presupuesto restante:', presupuesto_restante)


# Estadísticas

print('Estadísticas de los jugadores')

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


# Puntos Fantasy

fantasy1 = calcular_fantasy(puntos1, rebotes1, asistencias1)
fantasy2 = calcular_fantasy(puntos2, rebotes2, asistencias2)
fantasy3 = calcular_fantasy(puntos3, rebotes3, asistencias3)
fantasy4 = calcular_fantasy(puntos4, rebotes4, asistencias4)


# Equipo falso

equipo_falso = 86


# Puntos totales

if seleccion1 == 1 and seleccion2 == 2:
    puntos_totales = fantasy1 + fantasy2

elif seleccion1 == 1 and seleccion2 == 3:
    puntos_totales = fantasy1 + fantasy3

elif seleccion1 == 1 and seleccion2 == 4:
    puntos_totales = fantasy1 + fantasy4

elif seleccion1 == 2 and seleccion2 == 3:
    puntos_totales = fantasy2 + fantasy3

elif seleccion1 == 2 and seleccion2 == 4:
    puntos_totales = fantasy2 + fantasy4

elif seleccion1 == 3 and seleccion2 == 4:
    puntos_totales = fantasy3 + fantasy4

else:
    puntos_totales = 0


# Resultado

if puntos_totales > 0:
    print('Puntos Fantasy:', puntos_totales)
    print('Otro Equipo:', equipo_falso)

    resultado = comparar_equipos(puntos_totales, equipo_falso)
    print(resultado)

