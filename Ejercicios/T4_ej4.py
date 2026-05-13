"""


Alí Babá ha conseguido entrar en la cueva de los ciento un mil ladrones, y ha llevado
consigo su camello junto con dos grandes alforjas; el problema es que se
encuentra con tanto tesoro que no sabe ni qué llevarse. Los tesoros son joyas
talladas, obras de arte, cerámica… es decir, son objetos únicos que no pueden
partirse ya que entonces su valor se reduciría a cero.
Afortunadamente los ladrones tienen tod muy bien organizado y se encuentra con
una lista de todos los tesoros que hay en la cueva, donde se refleja el peso de cada
pieza y su valor en el mercado de Damasco. Por su parte, Alí sabe la capacidad de
peso que tiene cada una de las alforjas.
Diseñar un algoritmo de Programación Dinámica que, teniendo como datos los
pesos y valor de las piezas, y la capacidad de las dos alforjas, permita obtener el
máximo beneficio que podrá sacar Alí Babá de la cueva de las maravillas.


"""


"""Utilizamos programación dinámica mediante una matriz tridimensional de tamaño (n+1) x (C1+1) x (C2+1). 
En cada posición almacenamos el máximo beneficio que puede obtenerse usando los primeros i objetos, con capacidad c1 
en la primera alforja y capacidad c2 en la segunda. Para rellenar la matriz se recorren todos los objetos y 
para cada uno, todas las combinaciones posibles de capacidades de ambas alforjas para no incluir el objeto, incluirlo 
en la primera alforja o en la segunda. Su complejidad es de O(n x C1 x C2) Una vez calculada la matriz, el máximo 
beneficio se encuentra en M[n][C1][C2]. Por lo que si nuestra matriz devolvierá solo ese valor, ya tendríamos calculada 
la complejidad.

Como decidimos devolver también el contenido de cada alforja,tenemos en cuenta el coste de construir la
solución recorriendo la matriz hacia atrás para determinar qué objetos fueron incluidos en cada alforja. 
Esto tiene coste O(n), por lo que no cambia la complejidad total.

Por tanto, la complejidad es: O(n x C1 x C2)"""


def carga(objetos, capacidad1, capacidad2):


    num_objetos = len(objetos) #Cuenta cuantos objetos hay

    #Matriz 3D llena de ceros
    matriz_beneficios = [[[0 for _ in range(capacidad2 +1)] for _ in range(capacidad1 +1)] for _ in range(num_objetos+1)]

    for indice_objeto in range(1,num_objetos+1):#Recorremos los objetos
        objeto = objetos[indice_objeto-1]
        volumen = objeto['volumen']
        valor = objeto['valor']

        for col1 in range(capacidad1 + 1): #Para probar todas las capacidades de la alforja 1
            for col2 in range(capacidad2 + 1): #Para probar todas las capacidades de la alforja 2

                mejor = matriz_beneficios[indice_objeto-1][col1][col2] #De momento el mejor valor es el que tenía antes
                if volumen <= col1: #¿Cabe el objeto actual en la alforja 1?
                    mejor = max(mejor, valor + matriz_beneficios[indice_objeto-1][col1-volumen][col2])

                if volumen <= col2:
                    mejor = max(
                        mejor,
                        valor + matriz_beneficios[indice_objeto-1][col1][col2-volumen]
                    )
                #Obtenemos la matriz de beneficios
                matriz_beneficios[indice_objeto][col1][col2] = mejor

    #Obtenemos el máximo beneficio:
    maximo_beneficio = matriz_beneficios[num_objetos][capacidad1][capacidad2]

    #Vemos que tiene cada alforja: Lo añadimos para completar la función
    alforja1 = []
    alforja2 = []

    while num_objetos > 0:
        #Recorremos los objetos desde el final hasta el principio
        objeto= objetos[num_objetos-1]
        volumen = objeto['volumen']
        valor = objeto['valor']

        valor_actual = matriz_beneficios[num_objetos][capacidad1][capacidad2]

        #Si el objeto actual no fue usado:
        if valor_actual == matriz_beneficios[num_objetos-1][capacidad1][capacidad2]:
            num_objetos -= 1

        #Si el objeto actual fue metido en la alforja 1
        elif volumen <= capacidad1 and valor_actual == valor + matriz_beneficios[num_objetos-1][capacidad1-volumen][capacidad2]:
            alforja1.append(objeto)
            capacidad1 -= volumen
            num_objetos -=1

        elif volumen<= capacidad2 and valor_actual == valor +matriz_beneficios[num_objetos-1][capacidad1][capacidad2-volumen]:
            alforja2.append(objeto)
            capacidad2 -= volumen
            num_objetos -= 1

    alforja1.reverse()
    alforja2.reverse()

    return maximo_beneficio, alforja1, alforja2



#Pequeña prueba:
objetos = [
    {"nombre": "pan", "valor": 5, "volumen": 2},
    {"nombre": "oro", "valor": 10, "volumen": 3},
    {"nombre": "agua", "valor": 4, "volumen": 1},
    {"nombre": "libro", "valor": 7, "volumen": 2}
]

capacidad1 = 3
capacidad2 = 3

maximo_beneficio, alforja1, alforja2 = carga(objetos, capacidad1, capacidad2)

print("Máximo beneficio:", maximo_beneficio)

print("Alforja 1:")
for objeto in alforja1:
    print(objeto)

print("Alforja 2:")
for objeto in alforja2:
    print(objeto)
