"""


Se dispone de un tablero M de tamaño FxC (donde F es la cantidad de filas y C la
cantidad de columnas) y se pone en una casilla inicial (x,y) un caballo de ajedrez.
El objetivo es encontrar, si es posible, la forma en la que el caballo debe moverse
para recorrer tod el tablero, de manera que cada casilla se utilice una única vez
en el recorrido. El tablero 8x8 siempre tiene solución independientemente de
dónde comience el caballo. El caballo puede terminar en cualquier posición del
tablero.
El caballo de ajedrez tiene ocho posibles movimientos (suponiendo que no se sale
del tablero).
Un movimiento entre las casillas Mij y Mpq es válido solamente si se cumple alguna
de las siguientes condiciones:
• |p − i| = 1 y |q − j| = 2
• |p − i| = 2 y |q − j| = 1
Es decir, una coordenada cambia dos unidades y la otra una única unidad


"""
tablero = []

altoTablero = 5
anchoTablero = 5

alto = altoTablero
while alto > 0:

    fila = []
    ancho = anchoTablero

    while ancho > 0:

        fila.append(-1)
        ancho -= 1

    tablero.append(fila)

    alto -= 1

casillaInicial = (2, 3)


movimientos = [casillaInicial]


def movimientosPosibles(posicion) -> list:

    movimientos = []

    posibles = [(posicion[0]+2, posicion[1]+1),
                (posicion[0]+2, posicion[1]-1),
                (posicion[0]-2, posicion[1]+1),
                (posicion[0]-2, posicion[1]-1),
                (posicion[0]+1, posicion[1]+2),
                (posicion[0]+1, posicion[1]-2),
                (posicion[0]-1, posicion[1]+2),
                (posicion[0]-1, posicion[1]-2)]

    for posibilidad in posibles:

        if 0 <= posibilidad[0] < altoTablero and 0 <= posibilidad[1] < anchoTablero:

            movimientos.append(posibilidad)


    return movimientos



def wandorff(movimientos) -> list:

    listaConCoef = []
    ordenSinCoef = []

    for movimiento in movimientos:

        listaConCoef.append((len(movimientosPosibles(movimiento)), movimiento))

    listaConCoef = sorted(listaConCoef)

    for elem in listaConCoef:

        ordenSinCoef.append(elem[1])

    return ordenSinCoef




def backTrakingDelCaballo(posicionCaballo = casillaInicial, marcador = 0) -> bool:

    if tablero[posicionCaballo[0]][posicionCaballo[1]] != -1:
        return False

    tablero[posicionCaballo[0]][posicionCaballo[1]] = marcador

    if marcador == altoTablero*anchoTablero -1:

        print("exito")
        return True

    print("marcador = ", marcador, "posicion = ", posicionCaballo)

    for fila in tablero:
        print("[", end=" ")
        for valor in fila:
            if valor == -1:
                print(" . ", end="")
            else:
                print(f"{valor:2}", end=" ")
        print("]")

    for hijo in wandorff(movimientosPosibles(posicionCaballo)):

        if tablero[hijo[0]][hijo[1]] == -1:

            resultado = backTrakingDelCaballo(hijo, marcador+1)

            if resultado:

                return True


    tablero[posicionCaballo[0]][posicionCaballo[1]] = -1
    return False



backTrakingDelCaballo()

print("\n")
for fila in tablero:
    print("[", end=" ")
    for valor in fila:
        if valor == -1:
            print(" . ", end="")
        else:
            print(f"{valor:2}", end=" ")
    print("]")