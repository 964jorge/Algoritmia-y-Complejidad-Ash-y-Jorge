"""

Realiza un programa que pida un número entero positivo al usuario (N) y le diga
cuantos primos hay entre 1 y ese número N, y cuantos perfectos hay entre 1 y ese
número N. Realiza un análisis de eficiencia y de complejidad


Número perfecto: Número entero positivo que es igual a la suma de sus divisores
                 positivos excluyéndose a sí mismo.


"""

numeroInvalido = True
numero = 0

while numeroInvalido:

    try:

        numero = int(input("Elija un maximo: \n"))

        if numero > 1:

            numeroInvalido = False

        else:

            print("Numero invalido\n")


    except:

        print("Numero invalido\n")




def contarPrimos(numero) -> list[int]:

    lista = [1,2,3]

    return lista







