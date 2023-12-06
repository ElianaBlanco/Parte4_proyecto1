import os

# Esta función limpia la pantalla de la consola dependiendo del sistema operativo
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Esta función muestra el mapa en la consola
def mostrar_mapa(mapa):
    for fila in mapa:
        print("".join(fila))

# Esta función convierte la cadena del laberinto en una lista de listas de caracteres (matriz)
def convertir_a_matriz(laberinto):
    return [list(fila) for fila in laberinto.split('\n')]

# Esta es la función principal que maneja el bucle del juego
def main_loop(mapa, inicio, final):
    px, py = inicio  # Establece las coordenadas iniciales del jugador

    while (px, py) != final:  # Continúa hasta que el jugador llegue al final
        limpiar_pantalla()  # Limpia la pantalla
        mapa[py][px] = 'P'  # Marca la posición del jugador en el mapa

        mostrar_mapa(mapa)  # Muestra el mapa en la consola

        movimiento = input("Ingresa la dirección (w/a/s/d): ")  # Lee la dirección del teclado

        nueva_px, nueva_py = px, py  # Establece las nuevas coordenadas del jugador

        # Actualiza las coordenadas según la dirección ingresada por el usuario
        if movimiento == 'w':
            nueva_py -= 1
        elif movimiento == 's':
            nueva_py += 1
        elif movimiento == 'a':
            nueva_px -= 1
        elif movimiento == 'd':
            nueva_px += 1

        # Verifica si la nueva posición es válida (no se sale del mapa y no es una pared)
        if (
            0 <= nueva_px < len(mapa[0]) and
            0 <= nueva_py < len(mapa) and
            mapa[nueva_py][nueva_px] != '#'
        ):
            mapa[py][px] = '.'  # Restaura la posición anterior a un punto
            px, py = nueva_px, nueva_py  # Actualiza las coordenadas del jugador
        else:
            print("Movimiento inválido")  # Muestra un mensaje si el movimiento es inválido


if __name__ == "__main__":
    # Ejemplo de un laberinto (representado como una cadena)
    laberinto = """
    ##################
    #P...............#
    #.................#
    #.................#
    #.................#
    #.................#
    #.................#
    #.................#
    #.................#
    #.................#
    #.................#
    #.................#
    #.................#
    #.................#
    #.................#
    #.................#
    #.................#
    ##################
    """

    # Convertir la cadena del laberinto a una matriz de caracteres
    mapa = convertir_a_matriz(laberinto)

    # Coordenadas de inicio y final
    inicio = (1, 1)  # Cambiar según la configuración del laberinto
    final = (len(mapa[0]) - 2, len(mapa) - 2)  # Cambiar según la configuración del laberinto

    # Ejecutar el bucle principal del juego
    main_loop(mapa, inicio, final)
