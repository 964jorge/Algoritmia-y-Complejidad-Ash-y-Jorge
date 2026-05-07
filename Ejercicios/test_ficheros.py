from Ejercicios.T2_ej2 import obtenerCoefFicheros, voraz_ficherosOrdenados


def test_obtenerCoefFicheros():
    #Probamos que se obtienen bien los coeficientes
    entrada = [(5,2),(3,5),(1,4)]
    resultado = obtenerCoefFicheros(entrada)
    esperados = [(2.5,5,(5,2)), (0.6,3,(3,5)), (0.25,1,(1,4))]
    assert resultado == esperados

def test_mergesort_paraEmpate():
    #Probamos que ante un empate se sigue la segunda condición
    entrada = [(2,4),(4,8),(1,2)]  # Todos l/p = 0.5
    resultado = voraz_ficherosOrdenados(entrada)
    assert resultado == [(1,2),(2,4),(4,8)]

def test_casoVacio():
    entrada= []
    resultado = voraz_ficherosOrdenados(entrada)
    assert resultado == []

def test_un_solo_fichero():
    entrada = [(10,5)]
    resultado = voraz_ficherosOrdenados(entrada)
    assert resultado == [(10,5)]

def test_todos_empatados():
    entrada = [(1,2),(3,6),(5,10),(2,4)]
    resultado = voraz_ficherosOrdenados(entrada)
    assert resultado == [(1,2),(2,4),(3,6),(5,10)]

def test_ficherosIguales():
    entrada = [(3,5),(3,5),(3,5)]
    resultado = voraz_ficherosOrdenados(entrada)
    assert resultado == [(3,5),(3,5),(3,5)]

def test_ficherosIguales_en_diferentesPosiciones():
    entrada = [(1,10),(3,5),(3,5),(5,2),(3,5),(3,5),(10,1),(3,5),(3,5),(3,5)]
    resultado = voraz_ficherosOrdenados(entrada)
    esperado = [(1,10), (3,5),(3,5),(3,5),(3,5),(3,5),(3,5),(3,5),(5,2),(10,1)]
    assert resultado == esperado

def test_listaLarga_Ficheros():
    entrada = [(2,9),(3,12),(1,5),(4,10),(5,25),(6,18),(2,4),(7,21),(1,2),(8,16),(3,6),(4,4)]
    resultado = voraz_ficherosOrdenados(entrada)
    assert resultado == [(1,5),(5,25),(2,9),(3,12),(6,18),(7,21),(4,10),(1,2),(2,4),(3,6),(8,16),(4,4)]



