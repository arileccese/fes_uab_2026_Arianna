###
# EXERCICIS (diccionaris)
###

# Exercici 1: Crear un diccionari
# Crea un diccionari anomenat estudiant amb les claus "nom", "edat" i "assignatures"
# (aquesta última, una llista amb tres assignatures). Imprimeix-lo.

print("\n_____________ex1")
estudiante = {
    "nombre": "arianna",
    "edad": 22,
    "asignaturas":["asig1", "asig2", "asig3"]
}
print(estudiante)

print("\n_____________ex2")
# Exercici 2: Accedir i modificar
# Imprimeix la segona assignatura de l'estudiant i canvia'n l'edat a un valor nou.
print(estudiante["asignaturas"][1])
estudiante["asignaturas"][1] = "asignatura modificada"
print(estudiante["asignaturas"][1])


# Exercici 3: Afegir i eliminar
# Afegeix la clau "grau" a l'estudiant i elimina després la clau "edat" amb del.

print("\n_____________ex3")
estudiante["grau"] = "Ing. Telecos"
del estudiante["edad"]
print(estudiante)


# Exercici 4: Comprovar claus
# Comprova amb in si existeixen les claus "nom" i "email" i imprimeix el resultat.
print("\n_____________ex4")
print("nombre" in estudiante)
print("email" in estudiante)



# Exercici 5: Recórrer un diccionari
# Recorre el diccionari amb un bucle for i items() i imprimeix cada parella com "clau: valor".

# Exercici 6: Comptar paraules
# Donada la llista de paraules:
# paraules = ["sol", "lluna", "sol", "estrella", "lluna", "sol"]
# Crea un diccionari que indiqui quantes vegades apareix cada paraula.
