"""

Ejercicio: Realiza un programa que pida un número entero positivo al usuario (N) y le diga
cuantos primos hay entre 1 y ese número N, y cuantos perfectos hay entre 1 y ese
número N. Realiza un análisis de eficiencia y de complejidad. 
Hemos asumido que N está incluido en el intervalo.

"""

"""
Comentario y explicación: 

Hemos valorado hacerlo con criba de erastotenes y primos de Mersenne pero despues de investigar y tomando este
extracto de wikipedia:

"No se conoce la existencia de números perfectos impares. Sin embargo, existen algunos resultados parciales al 
respecto. Si existe un número perfecto impar debe ser mayor que 10300, debe tener al menos 8 factores primos 
distintos (y al menos 11 si no es divisible por 3). Uno de esos factores debe ser mayor que 107, dos de ellos
 deben ser mayores que 10 000 y tres factores deben ser mayores que 100"

https://es.wikipedia.org/wiki/N%C3%BAmero_perfecto

No podemos concluir que podamos hallar todos los perfectos asi. Aunque no se vayan a usar numero tan enormes
no podemos dar el algoritmo por exhaustivo por no estar demostrado que todos los casos sean resolubles con él.

Conociendo la criba de erastotenes y sabiendo que tendremos que calcular divisores hasta que la suma sea mayor
que el numero hemos decicido usar un algoritmo que los calcule para hacer los dos apartados a la vez y no tener
que ejecutar algo de N * log(log(N)) (la criba) y luego algo de N^2 (los perfectos). Para eso vamos a usar
algo de complejidad N^2 directamente (Aunque la complejidad no cambie, ahorramos pasos innecesarios).

Lo estamos haciendo realmente sin guardar divisores en memoria, simplemente los sumamos a un tally
y si en algun momento se pasa del numero que analizamos simplemente se descarta ese número como candidato a
ambos casos.


Notas importantes para nuestro enfoque:

Sabemos que un numero perfecto nunca será 1 o primo por definicion de perfecto
Sabemos que la suma de los divisores no iguales al número de un primo será 1
El 1 no es un número ni primo ni compuesto, por eso lo saltamos directamente.

"""

from math import sqrt

def primoYPerfecto(numero):

    """El for externo se ejecuta n veces, el interno n veces en el peor caso, 
    dentro tenemos operaciones elementales por lo que será de orden O(n^2) """
    
    listaPerfectos =[] #Para guardar los perfectos encontrados
    listaPrimos=[]#Para guardar los primos encontrados

    for numeroAnalizandose in range(2,numero + 1): #Para los números entre 2 y n

        sumaDivisores = 1 #Todos tienen un divisor 

        for i in range(2,numeroAnalizandose): #Nos fijamos en los que van del 2 hasta el que estamos viendo que es menor que n

            if numeroAnalizandose % i ==0: #Calculamos la suma de sus divisiores
                sumaDivisores+=i
            
            if sumaDivisores>numeroAnalizandose:
                break
        
        if sumaDivisores == numeroAnalizandose:
            listaPerfectos.append(numeroAnalizandose)

        if sumaDivisores ==1:
            listaPrimos.append(numeroAnalizandose)

    return len(listaPrimos), len(listaPerfectos)


"""

Despues de haber hecho un algoritmo teoricamente exhaustivo, vamos a presentar uno rápido. Con criba y Mersenne.

"""

def resultadoConCriba(numeroHasta) -> list:
    """Orden: O(n log log n) porque inicializar la lista tiene una complejidad 0(n), 
    recorrer la lista hasta la ríz cuadrada de n tiene O(raiz de n) y obtenemos (n log log n) de la 
    suma de los costes de eliminar múltiplos de todos los número primos"""

    if numeroHasta<2:
        return[]

    listaResultados = []
    listaOperaciones = []

    for i in range(2, numeroHasta + 1):

        listaOperaciones.append(True)


    i = 0
    while i < int(sqrt(numeroHasta)):

        if listaOperaciones[i]:

            j = 2

            while j*(i+2) <= numeroHasta:

                listaOperaciones[(j*(i+2))-2] = False

                j += 1


        i += 1


    for i in range(len(listaOperaciones)):

        if listaOperaciones[i]:

            listaResultados.append(i+2)



    return listaResultados



def perfectosConMeresnne(listaPrimosConCribado, numeroHasta) -> list:
    """Tiene orden: O(n log n) porque la complejidad de iterar es O(log n) 
    por el crecimiento exponencial de 2^n y comprobar si un número es 
    primo es O(n)"""
    listaPerfectos = []

    n = 2
    while (2**(n-1))*(2**n -1) <= numeroHasta:

        if 2**n-1 in listaPrimosConCribado:

            listaPerfectos.append((2**(n-1))*(2**n -1))

        n += 1

    return listaPerfectos

def calculoRapido(numero): #Utilizando criba y Meresnne
    listaPrimos = resultadoConCriba(numero)
    listaPerfectos = perfectosConMeresnne(listaPrimos, numero)
    return len(listaPrimos), len(listaPerfectos)


#Solicitar al usuario un número y comprobar que es válido
if __name__=="__main__":
    numeroInvalido = True

    while numeroInvalido:

        try:

            numero = int(input("Elija un maximo: "))

            if numero > 0:

                numeroInvalido = False

            else:

                print("\nNumero invalido\n")


        except:

            print("\nNumero invalido\n")



    if numero <= 2:

        print("Hasta el " + str(numero)+ " no hay ni primos ni perfectos\n")
        exit(0)
    
    primos1, perfectos1 = primoYPerfecto(numero)
    print("Resultados con el primer método")
    print("Primos:", primos1)
    print("Perfectos:", perfectos1)

    print("Resultados con el segundo método")
    primos2,perfectos2 = calculoRapido(numero)
    print("Primos:", primos2)
    print("Perfectos:", perfectos2)
    




