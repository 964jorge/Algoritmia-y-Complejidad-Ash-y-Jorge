"""


Tras su paso por la Sala de las Baldosas y conseguir la Cuna de la Vida, ahora
Indiana Croft se enfrenta a un nuevo desafío antes de poder salir del Templo
Maldito. Se encuentra en un puente bajo el que se observa una profunda oscuridad.
Afortunadamente, este lugar también aparece en el diario. El puente cruza el
llamado Valle de Sombras, que empieza con una pendiente de bajada (la pendiente
no es necesariamente constante) para después de llegar al punto más bajo
empezar a subir hasta el otro extremo del puente (de nuevo, no necesariamente
con pendiente contante). Justo en la parte inferior del valle hay un río, pero el diario
no especifica su ubicación con respecto al puente (por ejemplo, no se sabe si el río
está a 53 metros desde el comienzo del puente) ni la distancia en altura (es decir,
no se sabe si el río está 228 metros por debajo, por ejemplo). En las pendientes hay
afiladísimas rocas.
Si Indiana Croft tuviese tiempo, podría encontrar sin problema el punto por donde
descolgarse del puente para llegar exactamente al río, ya que tiene un puntero laser
para medir alturas que le dice cuántos metros hay desde el puente hasta el suelo
en un punto determinado. El problema es que los sacerdotes del templo han
averiguado que les han robado la Cuna de la Vida, están persiguiendo a Indiana
Croft y le alcanzarán enseguida. El aventurero debe encontrar rápidamente la
posición del río para descolgarse y huir seguro.
Diseñar el algoritmo que debería usar Indiana Croft para buscar el punto mínimo
del valle en las condiciones indicadas. El algoritmo debe ser eficiente: al menos en
el mejor caso debe tener un orden logarítmico. Se puede considerar el tiempo que
tarda Indiana Croft en desplazarse a lo largo del puente es nulo y que la estimación
del punto del río por donde descolgarse puede tener un error de aproximación de ε
metros (ε es una constante dada).


"""


import random
import sys


def crearEscenario(rio: int, tamanno: int) -> list:

    #Creado para poder probar nuestra función principal

    if rio >= tamanno:

        sys.exit(-1)

    escenario = []
    valor = 0
    en_meseta = False
    meseta_restante = 0

    for i in range(tamanno):

        # Para garantizar el decrecimiento y crecimiento
        base = abs(i - rio)

        # Añadimos mesetas usando probabilidad
        if not en_meseta and random.random() < 0.02:
            en_meseta = True
            meseta_restante = random.randint(5, 20)
            valor_meseta = valor  # congelamos nivel actual

        # si estamos en meseta
        if en_meseta:
            valor = valor_meseta
            meseta_restante -= 1

            if meseta_restante == 0:
                en_meseta = False

        else:

            valor = (valor + base) // 2

        escenario.append(valor)

    escenario[rio] = 0

    return escenario


def medirConLaser(punto: int, escenario: list) -> int:
    """Supone un coste de O(1), solo de acceso"""
    return escenario[punto]


def encontrarValle(escenario: list, error: int) -> tuple:
    """Usamos una búsqueda ternaria para reducir cada vez más el intervalo donde buscamos el mínimo
    (Consideramos el río como nuestro 0). Obtenemos una complejidad de O(log n). En cada paso tenemos
    operaciones constantes como las operaciones con el láser y la búsqueda en el tramo reducido para
    encontrar el mínimo que continuan manteniendo el O(log n) """

    extremoDerecha = len(escenario) -1
    extremoIzquierda = 0


    while abs(extremoDerecha - extremoIzquierda) > error:

        tercio1 = extremoIzquierda + (extremoDerecha - extremoIzquierda) // 3
        tercio2 = extremoDerecha - (extremoDerecha - extremoIzquierda) // 3

        d1 = medirConLaser(tercio1, escenario)
        d2 = medirConLaser(tercio2, escenario)

        if d1 > d2:

            extremoIzquierda = tercio1

        elif d1 < d2:

            extremoDerecha = tercio2

        else:

            extremoIzquierda = tercio1
            extremoDerecha = tercio2

        min = extremoIzquierda
        for i in range(extremoIzquierda,extremoDerecha +1):
            if escenario[i]<escenario[min]:
                min = i

    return min, escenario[min]

#Pequeña prueba con print:
error=3
escenario = crearEscenario(9, 100)
devolucion = encontrarValle(escenario, error)
resultado = devolucion
print(f"{resultado} con margen de error {error}")


