# Palabra secreta que el jugador debe adivinar
palabra = "hola"

# Lista vacía para almacenar las letras que el jugador ingresó
adivinadas = []

# Variable para almacenar el número de intentos (vidas) que el jugador tiene
vidas = 6

# Función para mostrar el tablero con las letras adivinadas y las vidas restantes
def mostrar_tablero(palabra, adivinadas, vidas):
    # Imprimir las letras de la palabra que han sido adivinadas. Si una letra no ha sido adivinada aún, se muestra un guión bajo (_)
    for letra in palabra:
        if letra in adivinadas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print("")
    
    # Imprimir el número de vidas restantes
    print("Vidas restantes:", vidas)

# Bucle principal del juego
while True:
    # Mostrar el tablero
    mostrar_tablero(palabra, adivinadas, vidas)
    
    # Pedir al jugador que ingrese una letra
    letra = input("Ingresa una letra: ")
    
    # Verificar si la letra está en la palabra secreta
    if letra in palabra:
        print("¡Bien! Adivinaste una letra.")
        adivinadas.append(letra)
    else:
        print("Lo siento, esa letra no está en la palabra.")
        vidas -= 1
    
    # Verificar si el jugador ha perdido todas sus vidas
    if vidas == 0:
        print("Perdiste. La palabra era", palabra)
        break
    
    # Verificar si el jugador ha adivinado todas las letras de la palabra secreta
    if all(letra in adivinadas for letra in palabra):
        print("¡Felicitaciones! Adivinaste la palabra.")
        break
