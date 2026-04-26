"""


Se dispone de un tablero M de tamaño FxC (donde F es la cantidad de filas y C la
cantidad de columnas) y se pone en una casilla inicial (x,y) un caballo de ajedrez.
El objetivo es encontrar, si es posible, la forma en la que el caballo debe moverse
para recorrer todo el tablero, de manera que cada casilla se utilice una única vez
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