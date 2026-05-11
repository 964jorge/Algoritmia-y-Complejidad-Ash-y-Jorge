from Ejercicios.T3_ej6 import crearEscenario, medirConLaser, encontrarValle


def test_escenario_tamano():
    esc = crearEscenario(5, 10)
    assert len(esc) == 10

def test_escenario_rio():
    esc = crearEscenario(10, 100)
    rio=esc[10]
    assert rio ==0

def test_medir_laser():
    esc = [10, 20, 30]
    assert medirConLaser(1, esc) == 20

def test_encontrar_valle_sencillo():
    esc = [5, 3, 1, 0, 1, 3, 5]
    ind,val = encontrarValle(esc, 3)
    ind_real = 2
    assert abs(ind-ind_real)<=3

def test_valle():
    esc = crearEscenario(5, 50)
    idx, val = encontrarValle(esc, 5)
    assert val == min(esc)

def test_valle_veces():
    for _ in range(5):
        esc = crearEscenario(5, 50)
        idx, val = encontrarValle(esc, 5)
        assert val == min(esc)

def test_laser_veces():
    esc = crearEscenario(5, 20)
    for i in range(len(esc)):
        assert medirConLaser(i, esc) == esc[i]