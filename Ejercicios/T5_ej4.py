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


"""En el peor caso, desde cada casilla pueden probarse hasta 8 movimientos. Por tanto, la complejidad
es O(8^N), es decir, O(8^(filas*columnas)).

La heurística de Warnsdorff ordena los movimientos posibles desde una casilla 
según el número de opciones futuras. Como 8 es el número de movimientos posibles,
calcular el coeficiente de cada movimiento y ordenarlos tiene coste O(a log a). 
En el caso del caballo, a está acotado por 8, por lo que este coste se considera 
constante, O(1), y no modifica la complejidad global del algoritmo.

"""


def crear_tablero(filas, columnas):
    """
    Crea un tablero de tamaño filas x columnas lleno de -1
    (para indicar que no están ocupadas). La creación del tablero tiene coste
    O(FxC), ya que se inicializan todas las casillas. """

    tablero = []

    for _ in range(filas):
        fila = []

        for _ in range(columnas):
            fila.append(-1)

        tablero.append(fila)

    return tablero


def es_valida(fila, columna, tablero, filas, columnas):
    """
    Comprueba si una posición está dentro del tablero y si
    no ha sido visitada.Realiza únicamente comprobaciones constantes,
    por lo que cuesta O(1).
    """

    return (
            0 <= fila < filas
            and 0 <= columna < columnas
            and tablero[fila][columna] == -1
    )


def movimientos_posibles(posicion, tablero, filas, columnas):
    """
    Devuelve los movimientos válidos del caballo desde una posición. Tiene complejidad O(1),
    ya que el caballo tiene como máximo 8 movimientos.

    """

    fila = posicion[0]
    columna = posicion[1]

    # 8 posibilidades
    posibles = [
        (fila + 2, columna + 1),
        (fila + 2, columna - 1),
        (fila - 2, columna + 1),
        (fila - 2, columna - 1),
        (fila + 1, columna + 2),
        (fila + 1, columna - 2),
        (fila - 1, columna + 2),
        (fila - 1, columna - 2)
    ]

    movimientos = []

    for fila_nueva, columna_nueva in posibles:
        if es_valida(fila_nueva, columna_nueva, tablero, filas, columnas):
            movimientos.append((fila_nueva, columna_nueva))

    return movimientos

def ordenar_warnsdorff(movimientos, tablero, filas, columnas):
    """
    Ordena los movimientos usando la idea de Warnsdorff.
    (primero las casillas desde las que habría menos movimientos futuros).

    """

    lista_coef= []

    for movimiento in movimientos:
        cantidad_mov_futuros = len(
            movimientos_posibles(movimiento, tablero, filas, columnas)
        )

        lista_coef.append((cantidad_mov_futuros, movimiento))

    # Ordena por el primer valor de la tupla automáticamente
    lista_coef.sort()

    movimientos_ordenados = []

    for coeficiente, movimiento in lista_coef:
        movimientos_ordenados.append(movimiento)

    return movimientos_ordenados

def backtracking_caballo(posicion, marcador, tablero, filas, columnas):
    """
    Función recursiva de backtracking
    """

    fila = posicion[0]
    columna = posicion[1]

    # Marcamos la casilla actual con el número de paso
    tablero[fila][columna] = marcador

    # Si el marcador es la última casilla, hemos terminado.
    if marcador == filas * columnas - 1:
        return True

    # Generamos los hijos válidos. Calculamos las casillas a las que el caballo puede ir desde la pos actual
    hijos = movimientos_posibles(posicion, tablero, filas, columnas)

    # Ordenamos los hijos con la heurística de Warnsdorff
    hijos = ordenar_warnsdorff(hijos, tablero, filas, columnas)

    # Para cada movimiento posible del caballo
    for hijo in hijos:
        #Recursión
        if backtracking_caballo(hijo, marcador + 1, tablero, filas, columnas):
            return True

    # Si no consigue compleat el tablero, hacemos backtracking:
    # desmarcamos la casilla actual.
    tablero[fila][columna] = -1

    return False


def recorrido_caballo(filas, columnas, casilla_inicial):
    """
    Función principal.Devolvemos:
     tablero con el recorrido si hay solución
     None si no hay solución
    """

    fila_inicial = casilla_inicial[0]
    columna_inicial = casilla_inicial[1]

    # Comprobamos que la casilla inicial esté dentro del tablero
    if not (0 <= fila_inicial < filas and 0 <= columna_inicial < columnas):
        return None

    tablero = crear_tablero(filas, columnas)

    hay_solucion = backtracking_caballo(
        casilla_inicial,
        0,
        tablero,
        filas,
        columnas
    )

    if hay_solucion:
        return tablero

    return None



#
#Pequeña prueba:

tablero = recorrido_caballo(8, 8, (2, 3))

if tablero is None:
    print("No hay solución")
else:
    for fila in tablero:
        print(fila)
