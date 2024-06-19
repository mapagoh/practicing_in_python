import random 


def adivina_el_número(x):

    print("================================")
    print("    ¡Bienvenido(a) al juego!    ")
    print("================================")
    print("Tu meta es adivinar el número generado por la computadora.")

    número_aleatorio = random.randint(1, x) 

    predicción = 0

    while predicción != número_aleatorio:
        predicción = int(input(f"Adivina un número entre 1 y {x}: ")) 

        if predicción < número_aleatorio:
            print("Intenta otra vez. Este número es muy pequeño.")
        elif predicción > número_aleatorio:
            print("intenta otra vez. Este número es muy grande.")
    
    print(f"¡Felicitaciones! Adivinaste el número {número_aleatorio} correctamente.")


adivina_el_número(10)

