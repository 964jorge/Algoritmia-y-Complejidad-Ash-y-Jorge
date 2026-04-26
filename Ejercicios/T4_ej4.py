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

objetos = [(2, 40), (5, 20), (4, 40), (3, 20), (2, 40), (5, 20), (4, 40), (3, 20) ]

capacidadAlforja = 8

resultadosParciales = []

k = 0
while k < capacidadAlforja + 1 :

    filaMatriz = [0]*(capacidadAlforja + 1)
    resultadosParciales.append(filaMatriz)
    k += 1




def maximizador(trasto = 0, capacidadRestante = capacidadAlforja) -> list:


    while trasto < len(objetos):

        i = capacidadRestante

        while i >= 0:

            j = capacidadRestante

            while j >= 0:

                if objetos[trasto][0] <= i:

                    resultadosParciales[i][j] = max(
                        resultadosParciales[i - objetos[trasto][0]][j] + objetos[trasto][1],
                        resultadosParciales[i][j])

                if objetos[trasto][0] <= j:

                    resultadosParciales[i][j] = max(
                        resultadosParciales[i][j - objetos[trasto][0]] + objetos[trasto][1],
                        resultadosParciales[i][j])

                j -= 1

            i -= 1

        trasto += 1

    return resultadosParciales



dp = maximizador()

i = 0
while i <= capacidadAlforja:
    print(f"{i}: {dp[i]}")
    i += 1

print ("\n\nMaximo dinero: " + str(dp[capacidadAlforja][capacidadAlforja]))




