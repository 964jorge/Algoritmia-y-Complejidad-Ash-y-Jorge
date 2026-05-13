from Ejercicios.T5_ej4 import recorrido_caballo


def test_t1x1():
    assert recorrido_caballo(1, 1, (0, 0)) == [[0]]


def test_casilla_NoValida():
    assert recorrido_caballo(8, 8, (10, 10)) is None

def test_no_filas():
    assert recorrido_caballo(0, 8, (0, 0)) is None


def test_no_columnas():
    assert recorrido_caballo(8, 0, (0, 0)) is None


def test_filas_negativas():
    assert recorrido_caballo(-1, 8, (0, 0)) is None

def test_columnas_negativas():
    assert recorrido_caballo(8, -1, (0, 0)) is None

def test_tablero_8x8_tiene_solucion():
    tablero = recorrido_caballo(8, 8, (2, 3))
    assert tablero is not None

def test_empiezaEsquina():
    tablero = recorrido_caballo(8, 8, (7, 7))

    assert tablero is not None
    assert tablero[7][7] == 0

def test_empiezaCentro():
    tablero = recorrido_caballo(8, 8, (4, 4))

    assert tablero is not None
    assert tablero[4][4] == 0

def test_casillaInicial_fuera():
    tablero = recorrido_caballo(8, 8, (0, 8))

    assert tablero is None

def test_t1x2_NoPosibleMov():
    tablero = recorrido_caballo(1, 2, (0, 0))

    assert tablero is None
