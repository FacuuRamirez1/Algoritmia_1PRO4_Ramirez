# 6) Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
#	55% del promedio de sus tres calificaciones parciales.
#	30% de la calificación del examen final.
#	15% de la calificación de un trabajo final.
print("Ejercicio 6 \n")

p1,p2,p3 = map(float, input("Ingrese las notas de los tres parciales: ").split())
exam_final = float(input("Ingrese la nota del examen final: "))
trab_final = float(input("Ingrese la nota del trabajo final:"))

prom_parciales = (p1 + p2 + p3) / 3
nota_final = (prom_parciales * 0.55) + (exam_final * 0.3) + (trab_final * 0.15)
print(f'La nota final es de: {round(nota_final, 2)}')
print("\n\n")


# 7) Conversión de divisas. Un programa que lea un monto en dólares y lo convierta a pesos colombianos, argentinos y euros usando tasas de cambio fijas definidas en el código.
print("Ejercicio 7 \n")

monto_usd = float(input("Ingrese el monto(USD) a convertir: "))
conver_arg = monto_usd * 1350
conver_colomb = monto_usd * 4029
conver_eur = monto_usd * 0.86
print(f'El monto de ${monto_usd} USD son equivalentes a: \n${round(conver_colomb, 3)} pesos colombianos \n${round(conver_arg, 3)} pesos argentinos \n€{round(conver_eur, 3)} euros')
print("\n\n")


# 8) Viaje en auto. Un auto consume 8 litros cada 100 km. El usuario ingresa la distancia en km y el precio de la gasolina por litro.
#   El programa debe calcular:
#   - cuántos litros se necesitan,
#   - cuánto costará el viaje,
#   - cuántas horas tardará si la velocidad promedio es de 90 km/h.
print("Ejercicio 8 \n")

d_km = float(input("Ingrese la distancia recorrida (en km): "))
pr_l = float(input("Ingrese el precio de la gasolina (por litros): "))

l_necesarios = (d_km * 8) / 100
costo_viaje = (l_necesarios * pr_l)
horas_viaje = d_km / 90

print("En base a los datos proporcionados:")
print(f'Se necesitan {l_necesarios}litros para realizar el viaje')
print(f'El viaje tiene un costo de ${costo_viaje}')
print(f'Con una velocidad constante de 90km/h, el viaje tardará {round(horas_viaje, 2)} horas en completarse')
print("\n\n")


# 9) Ejercicio monto fijo del 2% mensual
print("Ejercicio 9 \n")

monto_solicitado = float(input("Ingrese el monto del préstamo: "))
print("")
cant_meses = int(input("Ingrese la cantidad de meses a pagar: "))
print("")
INTERES_FIJO = 2 / 100

monto_total = monto_solicitado * (1 + (INTERES_FIJO))**cant_meses
cuota_mensual = (monto_solicitado * INTERES_FIJO) / (1 - (1 + INTERES_FIJO)**(-cant_meses))

print(f'El monto total a devolver es de ${round(monto_total, 3)}')
print(f'El valor de cada cuota mensual es de: ${round(cuota_mensual, 2)}')
print("\n\n")