#2. Cruce de matrices (tablero naval)
#
#Crear dos matrices 5x5:
#
#Una representa un “océano” con barcos colocados aleatoriamente (con 1 = barco y 0 = agua).
#
#Otra representa los disparos de un jugador.
#
#Cada vez que el jugador dispara, se marca con una “X” si fue acierto o “O” si fue fallo.
#
#El juego termina cuando todos los barcos son hundidos.
#👉 Similar al Bingo, pero con coordenadas y validaciones.
import random

# ===== Constantes =====
CANT_BARCOS = 5
TAMANO = 5

# ===== Funciones ======
def generar_tablero_barcos():
    tablero = [[0 for _ in range(TAMANO)] for _ in range(TAMANO)]
    barcos_colocados = 0
    while barcos_colocados < CANT_BARCOS:
        fila = random.randint(0, TAMANO - 1)
        col = random.randint(0, TAMANO - 1)
        if tablero[fila][col] == 0:
            tablero[fila][col] = 1
            barcos_colocados += 1
    return tablero

def generar_tablero_usuario():
    return [["-" for _ in range(TAMANO)] for _ in range(TAMANO)]

def imprimir_tablero(tablero, titulo="Tablero"):
    print(titulo)
    print("   " + "   ".join(map(str, range(TAMANO))))
    print("   " + "---" * TAMANO)
    for i, fila in enumerate(tablero):
        print(i, "|", " ".join(str(x) for x in fila))
    print()

def disparar(tablero_barco, tablero_usuario, fila, col):
    if tablero_barco[fila][col] == 1:
        tablero_usuario[fila][col] = "X"
        tablero_barco[fila][col] = -1
        print("¡Acierto!")
        return True
    else:
        tablero_usuario[fila][col] = "O"
        print("Agua")
        return False

def barcos_restantes (tablero_barco):
    return sum(cell == 1 for fila in tablero_barco for cell in fila)

# ===== Programa Principal ======

tablero_barco = generar_tablero_barcos()
tablero_usuario = generar_tablero_usuario()

imprimir_tablero(tablero_barco, "Tablero con barcos")
imprimir_tablero(tablero_usuario, "Tablero del jugador")

while barcos_restantes(tablero_barco) > 0:
    try:
        fila = int(input("Ingrese la fila (0-4): "))
        col = int(input("Ingrese la columna (0-4):"))

        if 0 <= fila <= TAMANO and 0 <= col <= TAMANO:
            disparar(tablero_barco, tablero_usuario, fila, col)
            imprimir_tablero(tablero_usuario, "Tablero del jugador")
        else:
            print("Coordenada fuera de rango!")

    except ValueError:
        print("Entrada inválida, ingrese un número:")

print("¡Ganaste! Has hundido todos los barcos")