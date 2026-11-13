###
# EXERCICIS (funcions)
###


#Pruebas internas:
#en esta función se especifica el nombre del parametro y el tipo de parametro separado por dos puntos c/u.
def funcion_prueba(nombre: str, apellido: str, edad: int):
    print(f"Hola, mi nombre: {nombre}, apellido: {apellido}, edad:{edad}")

funcion_prueba("Arianna", "Leccese", 22)


def funcion_muestra_parametro_y_valor(**kwargs):
    for parametro, valor in kwargs.items():
        print(f"{parametro}: {valor}")

funcion_muestra_parametro_y_valor(nombre = "ari", edad=2, apellido="lec")


# Exercici 1: Funció de salutació
# Crea una funció saludar_a(nom, salutacio="Hola") que imprimeixi la salutació seguida del nom.
# Prova-la amb i sense el segon argument.
print("\n\n____________________exercici 1")
def saludar_a(nom: str, salutacio="hola"):
    print(f"{salutacio}: {nom}")
    print(f"Hola {nom}")

saludar_a("ari")

# Exercici 2: Parell o senar
# Crea una funció es_parell(numero) que retorni True si el número és parell i False si no ho és.

print("\n\n____________________exercici 2")
def es_parell(numero):
    if numero %2 == 0:
        print(True)
    else:
        print(False)

es_parell(3)

# Exercici 3: Mitjana d'una llista
# Crea una funció mitjana(numeros) que rebi una llista de números i en retorni la mitjana.
# Fes servir un bucle for.
print("\n\n____________________exercici 3")
def mitjana(numeros):
    suma =0
    for i in numeros:
        suma += i      
    print(suma / len(numeros)) 
    #return  suma / len(numeros) 

mitjana([2,4,5])

# Exercici 4: Suma amb *args
# Crea una funció sumar_tot(*args) que retorni la suma de tots els números rebuts.
# Prova-la amb 2, 5 i 10 arguments.
print("\n\n____________________exercici 4")
def sumar_tot(*args):
    suma =0
    for i in args:
        suma += i
    print(suma)

sumar_tot(2,3)
sumar_tot(5,8,9,7,1)
sumar_tot(5,8,9,7,1,9,6,8,7,1)

# Exercici 5: Taula de multiplicar
# Crea una funció taula_multiplicar(numero, limit=10) que imprimeixi la taula de multiplicar
# del número fins al límit indicat, fent servir range().


# Exercici 6: Informació amb **kwargs
# Crea una funció mostrar_perfil(**kwargs) que imprimeixi cada parella clau: valor.
# Crida-la amb les dades d'un estudiant (nom, edat, grau).

# Exercici 7: Reconvertir exercicis anteriors
# Torna a l'exercici del factorial (while) i del màxim d'una llista (for)
# i converteix-los en funcions que retornin el resultat.
