from T1_ej7 import primoYPerfecto
from T1_ej7 import calculoRapido


def test_casoMin_primerMet():
    assert primoYPerfecto(1) == (0,0)

def test_casoMin_segMet():
    assert calculoRapido(1) == (0,0)

def test_casoHabitual_primerMet():
    assert primoYPerfecto(2) == (1,0)

def test_casoHabitual_segMet():
    assert calculoRapido(2) == (1,0)

def test_primerPerfecto6_primerMet(): #Sabiendo que el primer número perfecto es el 6
    assert primoYPerfecto(6) == (3,1)

def test_primerPerfecto6_SegMet():#Sabiendo que el primer número perfecto es el 6
    assert calculoRapido(6) == (3,1)

def test_casoGeneral_primerMet():
    assert primoYPerfecto(10) == (4,1)

def test_casoGeneral_segMet():
    assert calculoRapido(10) == (4,1)

def test_primerMet():
    assert primoYPerfecto(100) == (25,2)

def test_SegMet():
    assert calculoRapido(100) == (25,2)

def test_comparacion():
    assert calculoRapido(1500) == primoYPerfecto(1500)
