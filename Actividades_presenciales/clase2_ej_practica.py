# Ejercicio 1 - Sistema de becas estudiantiles
print("Ejercicio 1 \n")
nombre_completo = input("Ingrese su nombre y apellido: ")
edad = int(input("Ingrese su edad: "))
promedio_g = float(input("Ingrese su promedio general: "))
ing_fam = float(input("¿Cuáles son sus ingresos familiares mensuales? "))
res_beca = ""

if promedio_g >= 0 and promedio_g < 6:
    res_beca = "Beca rechazada"
elif promedio_g >= 6 and promedio_g < 10:
    if ing_fam < 300000:
        res_beca = "Beca completa"
    elif ing_fam >= 300000 and ing_fam < 600000:
        res_beca = "Media beca"
    elif ing_fam > 600:
        res_beca = "Becha rechazada"
else: print("Ingrese un promedio válido")

print(f'✔ {nombre_completo}, {edad} años')
print(f'Promedio: {round(promedio_g, 1)}')
print(f'Ingresos: ${ing_fam}')
print(f'Resultado: {res_beca}')
print("\n\n")

# Ejercicio 2 - Gestión de turnos hospitalarios

print("Ejercicio 2 \n")
nom_completo = input("Ingrese su nombre completo: ")
dni = (input("Ingrese su DNI: "))
edad_user = int(input("Ingrese su edad: "))
obra_social = input("¿Tiene obra social? (si/no): ").lower()
prioridad = input("Ingrese el nivel de urgencia (emergencia, urgente o control): ").lower()
prioridad_m = ["emergencia","urgente","control"]
dni_v = 0

def validar_dni (dni):
    dni_v = dni if (len(dni) == 8)  else "DNi inválido"
    if dni_v == dni: return dni_v

res_p = ""
turno_asig = ""

if (prioridad == prioridad_m[0]):
    turno_asig = "Guardia"
    res_p = prioridad_m[0]
elif (prioridad == prioridad_m[1]):
    res_p = prioridad_m[1]
    if obra_social == "si":
        turno_asig = "Turno en menos de 24hs"
    else: turno_asig = "Turno en 48hs"
elif(prioridad == prioridad_m[2]):
    res_p = prioridad_m[2]
    if edad > 65: 
        turno_asig = "Turno preferencial en 72hs"
    else: turno_asig = "Turno normal en 7 días"

print(f'✔ Paciente: {nom_completo}')
print(f'DNI: {validar_dni(dni)}')
print(f'Edad: {edad_user}')
print(f'Prioridad: {res_p}')
print(f'Turno asignado: {turno_asig}')
print("\n\n")

# Ejercicio 3 — Evaluación de crédito bancario
print("Ejercicio 3 \n")

nombre_apellido = input("Ingrese su nombre y apellido: ")
cuit = (input("Ingrese su cuit/cuil (formato xx-xxxxxxxx-x): ").strip().split("-"))
ing_mensuales = float(input("Ingrese sus ingresos mensuales: "))
ant_laboral = int(input("Ingrese su antigüedad laboral (en años): "))
hist_crediticio = input("Ingrese su historial crediticio (bueno / regular / malo): ").lower()
opc_hist = ["bueno", "regular", "malo"]

# Validar CUIT
def validar_cuit (cuit):
    principio_valido = ["20", "23", "24", "27"]
    if len(cuit) != 3:
        return "CUIT inválido (formato incorrecto)"
    if cuit[0] not in principio_valido:
        return "CUIT inválido (primeros dígitos incorrectos)"
    if len(cuit[1]) != 8 or not cuit[1].isdigit():
        return "CUIT inválido (parte del medio incorrecta)"
    if len(cuit[2]) != 1 or not cuit[2].isdigit():
        return "CUIT inválido (último dígito incorrecto)"
    return f"{cuit[0]}-{cuit[1]}-{cuit[2]}"

# def conseguir préstamo
def calif_cliente (ingresos, antiguedad, historial):
    if historial not in opc_hist:
        return "Historial inválido"
    if ingresos < 200000 or hist_crediticio == "malo":
        return "rechazado"
    if ingresos >= 200000 and antiguedad >= 2:
        if historial == "bueno":
            return "$3.000.000"
        elif historial == "regular":
            return "$1.000.000"
        else:
            return "$500.000"
    else:
        return "$500.000"

print(f'✔ Cliente: {nombre_apellido}')
print(f'CUIT: {validar_cuit(cuit)}')
print(f'Ingresos: ${ing_mensuales}')
print(f'Antigüedad: {ant_laboral} años')
print(f'Historial: {hist_crediticio}')
print(f'Monto aprobado: {calif_cliente(ing_mensuales, ant_laboral, hist_crediticio)}')
print("\n\n")


# --------------------- Actividades extras ---------------------

#  Ejercicio 1 — Clasificación de impuestos

print("Ejercicio 1 \n")
nombre_comp = input("Ingrese su nombre completo: ")
ed = int(input("Ingrese su edad: "))
ingresos_an = float(input("Ingese sus ingresos anuales: "))
print("")
impuestos = 0

if ingresos_an < 500000:
    impuestos = 0
elif ingresos_an >= 500000 and ingresos_an < 2000000:
    impuestos = ingresos_an * 0.10
elif ingresos_an >= 2000000 and ingresos_an < 5000000:
    impuestos = ingresos_an * 0.20
elif ingresos_an >= 5000000:
    impuestos = ingresos_an * 0.35

if ed > 65:
    impuestos = impuestos - (impuestos * 0.5)

print(f'Cliente: {nombre_comp}')
print(f'Ingresos: {ingresos_an}')
print(f'Edad del cliente: {ed} años')
print("No paga impuestos") if (impuestos == 0) else print(f'Impuesto final: ${round(impuestos, 2)}') 
print("\n\n")

# Ejercicio 2 - Sistema de calificaciones con promoción
print("Ejercicio 2 \n")
nombre_alum = input("Ingrese su nombre completo: ")
legajo = int(input("Ingrese su número de legajo: "))
notas = input("Ingrese las tres notas separadas por un espacio: ").strip().split()
n1, n2, n3 = [int(n) for n in notas]
print("")
promedio = (n1 + n2 + n3) / 3

# Colores
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"

print(f'Nombre: {nombre_alum}')
print(f'Legajo: {legajo}')
if (n1 < 4 or n2 < 4 or n3 < 4):
    print(f'Estado:{RED} Desaprobado{RESET}')
else:
    if promedio < 6:
        print(f'Estado: {RED}Desaprobado{RESET}')
    elif promedio >= 6 and promedio < 8:
        print(f'Estado: {YELLOW}Aprobado con final{RESET}')
    elif promedio >= 8:
        print(f'Estado: {GREEN}Promocionado{RESET}')

print("\n\n")

# Ejercicio 3 - Simulador de cajero automático
print("Ejercicio 3 \n")
saldo_in = 100000
intentos = 3

print("Escriba 'cancelar' para cancelar la operación en cualquier momento.")

nomb_usuario = input("Ingrese su nombre de usuario: ")
if nomb_usuario.lower() == "cancelar":
    print("Operación cancelada.")
else:
    while intentos > 0:
        pin = input("Ingrese su PIN (4 dígitos): ")
        if pin.lower() == "cancelar":
            print("Operación cancelada.")
            break
        if len(pin) != 4 or not pin.isdigit():
            print("PIN inválido. Ingréselo nuevamente.")
            intentos -= 1
            if intentos == 0:
                print("Número de intentos excedidos.")
                break
        else:
            while True:
                print(f'El saldo es de ${saldo_in}')
                retiro = input("¿Cuánto desea retirar? ")
                if retiro.lower() == "cancelar":
                    print("Operación cancelada.")
                    break
                if not retiro.isdigit():
                    print("Monto inválido.")
                    continue
                retiro = int(retiro)
                if retiro % 1000 != 0:
                    print("Error al retirar dinero, monto debe ser múltiplo de 1000.")
                elif retiro > saldo_in:
                    print("Fondos insuficientes.")
                else:
                    comision = 0
                    if retiro > 20000:
                        comision = retiro * 0.02
                    saldo_in -= (retiro + comision)
                    print(f'Retiro exitoso!\nDinero retirado: ${retiro}\nComisión: ${round(comision,2)}\nSaldo actual: ${round(saldo_in,2)}')
                    break
            break

print("\n\n")

# Ejercicio 4 - Categoría de conductores
print("Ejercicio 4 \n")
nomb_conductor = input("Ingrese su nombre completo: ")
edad_conductor = int(input("Ingrese su edad: "))
años_exp = int(input("Ingrese sus años de experiencia: "))

if edad_conductor < 18:
    print("Usted no puede conducir (menor de edad).")
elif (edad_conductor >= 18 and edad_conductor < 21) and años_exp < 1:
    print("Usted es un conductor de nivel principiante.")
elif (edad_conductor >= 21 and edad_conductor < 30) and (años_exp > 1 and años_exp < 5):
    print("Usted es un conductor de nivel intermedio.")
elif (edad_conductor >= 30 and años_exp > 10):
    print("Usted es un conductor de nivel profesional.")
else:
    print("Usted es un conductor de nivel estandar.")

print("\n\n")

# Ejercicio 5 - Simulador de carrito de compras
print("Ejercicio 5 \n")

nomb_cliente = input("Ingrese su nombre completo: ")
while True:
    cant_productos = int(input("¿Cuántos productos desea comprar? "))
    if cant_productos <= 0:
        print("La cantidad debe ser mayor a 0.")
    else:
        break

while True:
    monto_total = float(input("Ingrese el monto total de la compra: "))
    if monto_total <= 0:
        print("Ingrese un monto válido (positivo).")
    else:
        break

medio_pago = input("Ingrese el medio de pago (efectivo, debito, credito, mercado pago): ").lower()
descuento = 0
recargo = 0

if medio_pago == "efectivo":
    descuento = monto_total * 0.15
elif medio_pago == "debito":
    descuento = monto_total * 0.10
elif medio_pago == "credito":
    recargo = monto_total * 0.05
elif medio_pago == "mercado pago":
    if monto_total > 10000:
        descuento = monto_total * 0.20

monto_final = monto_total - descuento + recargo
desc_extra = 0
if cant_productos > 10:
    desc_extra = monto_final * 0.05
    monto_final -= desc_extra


print(f'Cliente: {nomb_cliente}')
print(f'Cantidad de productos: {cant_productos}')
print(f'Medio de pago: {medio_pago}')
if recargo != 0 and cant_productos > 10:
    pass
elif recargo != 0:
    print(f'Recargo aplicado: ${round(recargo, 2)}')
elif descuento != 0 and cant_productos > 10:
    print(f'Descuento aplicado: ${round(descuento, 2)} + ${round(desc_extra, 2)} (extra por cantidad)')
elif descuento != 0:
    print(f'Descuento aplicado: ${round(descuento, 2)}')
print(f'Monto final a pagar: ${round(monto_final, 2)}')