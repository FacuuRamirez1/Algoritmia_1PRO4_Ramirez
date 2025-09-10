# crear un programa para ingresar patente(validar)
# sumar cantidad n de números
# mostrar patente nueva

def main():
    print("")
    print("GENERADOR DE PATENTES")
    print("")
    print("Este programa calcula la N-ésima patente a partir de AAA000.")
    print("La primer patente (AAA000) corresponde al número 0.\n")

    numero = int(input("Ingrese el número de patente a calcular: "))
    print("")

    patente = ""
    contador = 0

    TOTAL_PATENTES = 26**3 * 10**3
    if numero >= TOTAL_PATENTES:
        print(f"El número es demasiado grande. El máximo posible es {TOTAL_PATENTES - 1}.")
        return


    for i in range(26):
        for j in range(26):
            for k in range(26):
                for x in range(10):
                    for y in range(10):
                        for z in range(10):
                            contador += 1
                            patente = chr(65 + i) + chr(65 + j) + chr(65 + k) + str(x) + str(y) + str(z)
                            if contador == numero + 1:
                                print("\nRESULTADO:")
                                print(f"Número solicitado: {numero}")
                                print(f"Patente final: {patente}")
                                return

if __name__ == "__main__":
    main()