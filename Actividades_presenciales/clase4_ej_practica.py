import random

alumnos = [
    "Valentina De Los ángeles Albizú",
    "Pablo Andres Allende",
    "Luca Valentín Argumedo",
    "Pablo Avalos",
    "Lucas Avila",
    "Santino Barone",
    "Sofia Blangetti",
    "Nicolás Bohm",
    "Renzo Valentino Borello Canizo",
    "Juan Manuel Carrillo Taglio",
    "Facundo Gustavo Chacon Catalan",
    "Agustin Emiliano Contardi",
    "Jeronimo Coronel Alvarez",
    "Gabriel Emiliano Denis",
    "Facundo Gustavo Deseff",
    "Juan Martin García",
    "Enzo Giaquinta",
    "Sabrina Gimenez",
    "Joaquin Godoy",
    "Lucas Facundo Godoy",
    "Santino Alejo Godoy Galdeano",
    "Valentina Antonela Gordillo Moreno",
    "Lautaro Agustin Guardatti Esquivel",
    "Tiago Nahuel Guillot Duran",
    "Mateo Lautaro Liendo",
    "Juan Ignacio Martinez Quiroga",
    "Maximo Exequiel Monardez",
    "Tomas Agustin Mora Gonzalez",
    "Pablo Isaias Morinigo Lima",
    "Ares Martín Ocaña Martinez",
    "Thiago Santino Oviedo Saldaño",
    "Amanda Lucrecia Pagano",
    "Máximo Juan Cruz Quiroga",
    "Facundo Agustín Ramírez García",
    "Franco Agustin Rios Alzamora",
    "Leonel Enrique Rojas",
    "Matias Nicolas Ruiz Vargas",
    "Ramiro Ezequiel Salcedo",
    "Ismael Saleme Padolsky",
    "Ignacio Exequiel Sanchez",
    "Fabrizio Jonathan Simon Santos",
    "Cristian Gabriel Soto",
    "Giovanna Mercedes Suarez",
    "Ismael Mauricio Suarez",
    "Fernando Agustín Torrez",
    "Luca Nicolas Valdez",
    "Tiziano Ignacio Valentini",
    "Matias Nicolas Vargas",
    "Juan Ignacio Videla Continella",
    "Pablo Exequiel Avalos"
]

idx = len(alumnos)
n = random.sample(range(idx), (idx))
new_list = [alumnos[i] for i in n]
matriz = [[0 for _ in range(idx//4)] for _ in range(4)]
c = 0

for i in range(0, idx):
    for j in range(5):
        matriz[i][j] = new_list[0 + c]
        c += 1

print(matriz)