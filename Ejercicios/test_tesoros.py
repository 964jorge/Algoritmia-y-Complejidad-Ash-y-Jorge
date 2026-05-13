from Ejercicios.T4_ej4 import carga


def test_casoHabitual():
    objetos = [
        {"nombre": "pan", "valor": 5, "volumen": 2},
        {"nombre": "oro", "valor": 10, "volumen": 3},
        {"nombre": "agua", "valor": 4, "volumen": 1},
        {"nombre": "libro", "valor": 7, "volumen": 2}
    ]

    assert carga(objetos, 3, 3)[0] == 21

def test_sinObjetos():
    objetos = []
    assert carga(objetos, 5, 5)[0] == 0

def test_noCabenObjetos():
    objetos = [
        {"nombre": "estatua", "valor": 100, "volumen": 10},
        {"nombre": "vasija", "valor": 50, "volumen": 8}
    ]
    assert carga(objetos, 3, 3)[0] == 0

def test_cantidadObjetos_enAlforjas():
    objetos = [
        {"nombre": "pan", "valor": 5, "volumen": 2},
        {"nombre": "oro", "valor": 10, "volumen": 3},
        {"nombre": "agua", "valor": 4, "volumen": 1},
        {"nombre": "libro", "valor": 7, "volumen": 2}
    ]

    maximo_beneficio, alforja1, alforja2 = carga(objetos, 3, 3)

    assert maximo_beneficio == 21
    assert len(alforja1) == 2
    assert len(alforja2) == 1

def test_queLleva_cadaAlforja():
    objetos = [
        {"nombre": "pan", "valor": 5, "volumen": 2},
        {"nombre": "oro", "valor": 10, "volumen": 3},
        {"nombre": "agua", "valor": 4, "volumen": 1},
        {"nombre": "libro", "valor": 7, "volumen": 2}
    ]

    maximo_beneficio, alforja1, alforja2 = carga(objetos, 3, 3)

    assert maximo_beneficio == 21

    assert alforja1 == [{"nombre": "agua", "valor": 4, "volumen": 1},{"nombre": "libro", "valor": 7, "volumen": 2}]

    assert alforja2 == [{"nombre": "oro", "valor": 10, "volumen": 3}]