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

        numero = int(input("Elija un maximo: "))

        if numero > 1:

            numeroInvalido = False

        else:

            print("\nNumero invalido\n")


    except:

        print("\nNumero invalido\n")


"""

VERSION MENOS EFICIENTE SIN CRIBA DE ERASTOTENES


def divisores(numero) -> list[int]:

    divisores = []

    for i in range(2, numero):

        if numero % i == 0:

            divisores.append(i)
            break

    return divisores





def contarPrimos(numero) -> list[int]:

    lista = []

    #resulta que el 1 no es primo ni compuesto asi que no le contamos
    for i in range(2, numero+1):

        listaDivisores = divisores(i)

        if len(listaDivisores) == 0:

            lista.append(i)
            print(i)



    return lista


print("Divisores de " + str(numero) + "\n")

listaPrimos = contarPrimos(numero)

print("\n\n En total son " + str(len(listaPrimos)) + "\n")

"""


