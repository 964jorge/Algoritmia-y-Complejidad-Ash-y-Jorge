"""

Se tiene que almacenar un conjunto de N ficheros en una cinta magnética (soporte
de almacenamiento de recorrido secuencial), donde cada fichero tiene una
longitud conocida L1, L2, ..., Ln. Para simplificar el problema, puede suponerse que
la velocidad de lectura es constante, así como la densidad de información en la
cinta.

Se conoce de antemano la tasa de utilización de cada fichero almacenado, es
decir, se sabe la cantidad de peticiones Pi correspondiente al fichero i que se van
a realizar. Por tanto, el total de peticiones al soporte será:

P = sumatorio desde i = 0 hasta i = n de Pi

Tras la petición de un fichero, al ser encontrado, la cinta se rebobina
automáticamente hasta el principio.

El objetivo es decidir el orden en que los ficheros deben ser almacenados para que
se minimice el tiempo medio de carga, creando un algoritmo voraz correcto.



"""

#cada tupla guarda la longitud y el uso
ficheros = [(5, 2), (3, 5), (1, 4), (7, 2), (1, 1), (2, 4), (4, 2), (4, 4)]
#ficheros = [(2, 10), (5, 20), (1, 4), (4, 8), (3, 9), (6, 18), (1, 1), (7, 14), (2, 3), (4, 12)]
#ficheros = [(2, 9), (3, 12), (1, 5), (4, 10), (5, 25), (6, 18), (2, 4), (7, 21), (1, 2), (8, 16), (3, 6), (4, 4), (5, 10), (9, 18), (2, 1)]

#guardará la relación longitud/uso, el tamaño en una tupla y la propia tupla para luego recuperarla
coeficientesFicheros =[]

#el resultado del algoritmo
ficherosOrdenados = []

i = 0
while i < len(ficheros):

    #para cada fichero calculamos el coeficiente y lo guardamos en la lista de los coef
    coeficientesFicheros.append((ficheros[i][0]/ficheros[i][1], ficheros[i][0], ficheros[i]))
    i += 1



#para hacer las cosas eficientes, vamos a ordenar por el cociente y ante igualdad por el que tenga menor longitud
def ordenarMergeSort(cosaSiendoOrdenada) -> list:

    if len(cosaSiendoOrdenada) <= 1:

        return cosaSiendoOrdenada

    else:

        medio = len(cosaSiendoOrdenada)//2

        principio = ordenarMergeSort(cosaSiendoOrdenada[:medio])
        final = ordenarMergeSort(cosaSiendoOrdenada[medio:])

        p = 0
        f = 0
        ordenado = []

        while p < len(principio) and f < len(final):


            if principio[p][0] > final[f][0]:

                ordenado.append(final[f])
                f += 1

            elif principio[p][0] < final[f][0]:

                ordenado.append(principio[p])
                p += 1

            else:

                if principio[p][1] >= final[f][1]:

                    ordenado.append(final[f])
                    f += 1

                else:

                    ordenado.append(principio[p])
                    p += 1


        while p < len(principio):

            ordenado.append(principio[p])
            p += 1


        while f < len(final):

            ordenado.append(final[f])
            f += 1

        return ordenado



i = 0
ficherosOrdenados = ordenarMergeSort(coeficientesFicheros)
resultado = []
while i < len(ficherosOrdenados):

    #vamos a quitar la información extra para imprimirlo bonito, recorremos y dejamos solo la tupla
    resultado.append(ficherosOrdenados[i][2])
    i += 1

print(resultado)
#este de abajo es por si queremos ver que se ha segido el orden del coeficiente + minima longitud
print("\n\n" + str(ficherosOrdenados))