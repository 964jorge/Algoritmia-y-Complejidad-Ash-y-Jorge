"""

Realiza un programa que pida un número entero positivo al usuario (N) y le diga
cuantos primos hay entre 1 y ese número N, y cuantos perfectos hay entre 1 y ese
número N. Realiza un análisis de eficiencia y de complejidad


Número perfecto: Número entero positivo que es igual a la suma de sus divisores
                 positivos excluyéndose a sí mismo.


"""
from math import sqrt

numeroInvalido = True
numero = 0

while numeroInvalido:

    try:

        numero = int(input("Elija un maximo: "))

        if numero > 1:

            numeroInvalido = False

        else:

            print("\nNumero invalido\n")


    except:

        print("\nNumero invalido\n")



"""

Hemos valorado hacerlo con criba de erastotenes y primos de Mersenne pero despues de investigar y tomando este
extracto de wikipedia:

No se conoce la existencia de números perfectos impares. Sin embargo, existen algunos resultados parciales al 
respecto. Si existe un número perfecto impar debe ser mayor que 10300, debe tener al menos 8 factores primos 
distintos (y al menos 11 si no es divisible por 3). Uno de esos factores debe ser mayor que 107, dos de ellos
 deben ser mayores que 10 000 y tres factores deben ser mayores que 100.

https://es.wikipedia.org/wiki/N%C3%BAmero_perfecto

No podemos concluir que podamos hallar todos los perfectos asi. Aunque no se vayan a usar numero tan enormes
no podemos dar el algoritmo por exhaustivo por no estar demostrado que todos los casos sean resolubles con él.

Conociendo la criba de erastotenes y sabiendo que tendremos que calcular divisores hasta que la suma sea mayor
que el numero hemos decicido usar un algoritmo que los calcule para hacer los dos apartados a la vez y no tener
que ejecutar algo de N * log(log(N)) (la criba) y luego algo de N^2 (los perfectos). Para eso vamos a usar
 algo de complejidad N^2 directamente (Aunque la complejidad no cambie, ahorramos pasos innecesarios).

Lo estamos haciendo realmente sin guardar divisores en memoria, simplemente los sumamos a un tally
y si en algun momento se pasa del numero que analizamos simplemente se descarta ese nuemero como candidato a
ambos casos.


Notas importantes para nuestro enfoque:

Sabemos que un numero perfecto nunca sera 1 o primo por definicion de perfecto
Sabemos que la suma de los divisores no iguales al numero de un primo sera 1
El 1 no es un numero ni primo ni compuesto, por eso lo saltamos directamente.


"""

listaPerfectos = []
listaPrimos = []

def divisores(numero):

    numeroAnalizandose = 2

    while numeroAnalizandose < numero:

        sumaDivisores = 1

        for i in range(2, numeroAnalizandose):

            if numeroAnalizandose % i == 0:

                sumaDivisores += i


            if sumaDivisores > numeroAnalizandose:

                break

        if sumaDivisores == numeroAnalizandose:

            listaPerfectos.append(numeroAnalizandose)

        if sumaDivisores == 1:

            listaPrimos.append(numeroAnalizandose)

        numeroAnalizandose += 1




divisores(numero)

print("\nPrimos entre 1 y " + str(numero) + ": ")
print("\nCon metodo exahustivo de complejidad N^2")
print("En total son " + str(len(listaPrimos)) + " primos y " + str(len(listaPerfectos)) + " perfectos." + "\n")


"""

Despues de haber hecho un algoritmo teoricamente exhaustivo, vamos a presentar uno rápido. Con criba y Mersenne

"""

def resultadoConCriba(numeroHasta) -> list:

    listaResultados = []
    listaOperaciones = []

    for i in range(2, numeroHasta):

        listaOperaciones.append(True)


    i = 0
    while i < int(sqrt(numeroHasta)) -1:

        if listaOperaciones[i]:

            j = 2

            while j*(i+2) < numeroHasta:

                listaOperaciones[(j*(i+2))-2] = False

                j += 1


        i += 1


    for i in range(len(listaOperaciones)):

        if listaOperaciones[i]:

            listaResultados.append(i+2)



    return listaResultados



def perfectosConMeresnne(listaPrimosConCribado, numeroHasta) -> list:

    listaPerfectos = []

    n = 2
    while (2**(n-1))*(2**n -1) < numeroHasta:

        if 2**n-1 in listaPrimosConCribado:

            listaPerfectos.append((2**(n-1))*(2**n -1))

        n += 1

    return listaPerfectos


listaPrimos = resultadoConCriba(numero)
listaPerfectos = perfectosConMeresnne(listaPrimos, numero)
print("Con criba de Erastótenes + Mersenne de complejidad [por mirar]")
print("En total son " + str(len(listaPrimos)) + " primos y " + str(len(listaPerfectos)) + " perfectos." + "\n")