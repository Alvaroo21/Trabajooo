import random

def imprimir_tablero(tablero):
    print("\nTablero:")
    for fila in tablero:
        print(" | ".join(fila))
        print("---------")

def hay_ganador(tablero, jugador):
    for i in range(3):
        if all(tablero[i][j] == jugador for j in range(3)) or all(tablero[j][i] == jugador for j in range(3)):
            return True
    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2-i] == jugador for i in range(3)):
        return True
    return False

def tablero_lleno(tablero):
    for fila in tablero:
        for casilla in fila:
            if casilla == ' ':
                return False
    return True

def turno_cpu(tablero, jugador):
    print(f"\nTurno de {jugador} (CPU):")
    while True:
        fila = random.randint(0, 2)
        columna = random.randint(0, 2)
        if tablero[fila][columna] == ' ':
            tablero[fila][columna] = jugador
            break
    imprimir_tablero(tablero)

def jugar_gato():
    print("Bienvenido al Juego Gato!\n")

    while True:
        tablero = [[' ' for _ in range(3)] for _ in range(3)]
        imprimir_tablero(tablero)

        jugador1 = 'X'
        jugador2 = 'O'

        print("\nSeleccione una opción:")
        print("1. Nueva partida (Player 1 VS COM)")
        print("2. Versus (P1 VS P2)")
        print("3. Salir")

        opcion = input("Ingrese el número de opción: ")

        if opcion == '1':
            print("\n¡Nueva partida (Player 1 VS COM)!")
            while True:
                print(f"\nTurno de {jugador1} (Jugador 1):")
                fila = int(input("Ingrese el número de fila (0-2): "))
                columna = int(input("Ingrese el número de columna (0-2): "))
                if tablero[fila][columna] == ' ':
                    tablero[fila][columna] = jugador1
                    imprimir_tablero(tablero)
                    if hay_ganador(tablero, jugador1):
                        print(f"\n¡El jugador 1 ({jugador1}) ha ganado!")
                        break
                    if tablero_lleno(tablero):
                        print("\n¡Empate!")
                        break
                    turno_cpu(tablero, jugador2)
                    if hay_ganador(tablero, jugador2):
                        print("\n¡La CPU ha ganado!")
                        break
                    if tablero_lleno(tablero):
                        print("\n¡Empate!")
                        break
                else:
                    print("\n¡Casilla ocupada! Intente de nuevo.")
        
        elif opcion == '2':
            print("\n¡Versus (P1 VS P2)!")
            while True:
                print(f"\nTurno de {jugador1} (Jugador 1):")
                fila = int(input("Ingrese el número de fila (0-2): "))
                columna = int(input("Ingrese el número de columna (0-2): "))
                if tablero[fila][columna] == ' ':
                    tablero[fila][columna] = jugador1
                    imprimir_tablero(tablero)
                    if hay_ganador(tablero, jugador1):
                        print(f"\n¡El jugador 1 ({jugador1}) ha ganado!")
                        break
                    if tablero_lleno(tablero):
                        print("\n¡Empate!")
                        break
                    print(f"\nTurno de {jugador2} (Jugador 2):")
                    fila = int(input("Ingrese el número de fila (0-2): "))
                    columna = int(input("Ingrese el número de columna (0-2): "))
                    if tablero[fila][columna] == ' ':
                        tablero[fila][columna] = jugador2
                        imprimir_tablero(tablero)
                        if hay_ganador(tablero, jugador2):
                            print(f"\n¡El jugador 2 ({jugador2}) ha ganado!")
                            break
                        if tablero_lleno(tablero):
                            print("\n¡Empate!")
                            break
                    else:
                        print("\n¡Casilla ocupada! Intente de nuevo.")
                else:
                    print("\n¡Casilla ocupada! Intente de nuevo.")

        elif opcion == '3':
            print("\n¡Gracias por jugar! ¡Hasta luego!")
            break
        
        else:
            print("\nOpción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    jugar_gato()