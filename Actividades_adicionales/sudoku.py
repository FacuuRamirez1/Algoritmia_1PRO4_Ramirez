#1. Sudoku simplificado (4x4)
#
#Generar un tablero 4x4 con números del 1 al 4 (pueden estar repetidos).
#
#Escribir una función que valide si una fila tiene todos los números distintos.
#
#Escribir otra que valide una columna.
#
#(Extra) Validar que cada subcuadro 2x2 también cumpla la condición.
#👉 Aplican listas anidadas, bucles y slicing.
import random

# ========== Funciones ==========

def generar_tablero ():
    tablero = []
    tablero = [[random.randint(1,5) for _ in range(4)] for _ in range(4)]
    return tablero

def imprimir_tablero (tablero):
    print(" 0  1  2  3 ")
    print("------------")
    for i in range(4):
        for j in range(4):
            print(tablero[i][j], "|", end=" ")
        print()
    print("   -----------------")

def val_fila (tablero, fila):
    return len(set(tablero[fila])) == len(tablero[fila])

def val_col (tablero, col):
    columna = [tablero[f][col] for f in range(4)]
    return len(set(columna)) == len(columna)

def val_subcuadros (tablero, start_row, start_col):
    nums = []
    for i in range(start_row, start_row + 2):
        for j in range(start_col, start_col + 2):
            nums.append(tablero[i][j])
    return len(set(nums)) == len(nums)

def tablero_valido (tablero):
    for i in range(4):
        if not val_fila(tablero, i):
            return False
    for j in range(4):
        if not val_col(tablero, j):
            return False
    for r in [0, 2]:
        for c in [0, 2]:
            if not val_subcuadros(tablero, r, c):
                return False
    return True

# ========== Programa Principal ==========
tablero = generar_tablero()
print("Tablero inicial")
imprimir_tablero(tablero)

while not tablero_valido(tablero):
    try:
        fila = int(input("Ingrese la fila (0-3): "))
        col = int(input("Ingrese la columna (0-3): "))
        nuevo_valor = int(input("Ingrese valor entre 1 y 4: "))

        if 0 <= fila <= 3 and 0 <= col <= 3 and 1 <= nuevo_valor <= 4:
            tablero[fila][col] = nuevo_valor
            print("\nTablero actual:")
            imprimir_tablero(tablero)
        else:
            print("Coordenada o valor fuera de rango, intente nuevamente")
    
    except ValueError:
        print("Entrada inválida! Ingrese un número\n")

print("Felicidades! Tablero completado")
imprimir_tablero(tablero)