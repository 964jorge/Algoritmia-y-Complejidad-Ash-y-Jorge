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


escenario = []

rio = int(random.random()*1000)

#Para esto nos ha ayudado ChatGPT porque en el que creamos nosotros se meseteaba a lo bestia, al final ha tocado meter suavizado y memoria
#hemos comprobado que no cree microvalles para no petar la idea del ejercicio. Ademas para respetar las mesetas las hemos añadido aleatoriamente
valor = 0
en_meseta = False
meseta_restante = 0

for i in range(1000):

    # 1. base de la U
    base = abs(i - rio)

    # 2. activar meseta de vez en cuando (evento global)
    if not en_meseta and random.random() < 0.02:
        en_meseta = True
        meseta_restante = random.randint(5, 20)
        valor_meseta = valor  # congelamos nivel actual

    # 3. si estamos en meseta
    if en_meseta:
        valor = valor_meseta
        meseta_restante -= 1

        if meseta_restante == 0:
            en_meseta = False

    else:
        # 4. dinámica con memoria (sin ruido)
        valor = (valor + base) // 2

    escenario.append(valor)





def medirConLaser(punto: int) -> int:

    return escenario[punto]



error = 10

extremoIzquierda = 0
extremoDerecha = 999

while abs(extremoDerecha - extremoIzquierda) > error:

    tercio1 = extremoIzquierda + (extremoDerecha - extremoIzquierda) // 3
    tercio2 = extremoDerecha - (extremoDerecha - extremoIzquierda) // 3

    if medirConLaser(tercio1) > medirConLaser(tercio2):

        extremoIzquierda = tercio1

    elif medirConLaser(tercio1) < medirConLaser(tercio2):

        extremoDerecha = tercio2

    else:

        extremoIzquierda = tercio1
        extremoDerecha = tercio2






# Esto esta para probar, es puro chatgpt. queda de hacerlo asi un poco mas personal pero me da un palo que no te imaginas
#estoy hasta la polla de Indiana Croft


estimado = (extremoIzquierda + extremoDerecha) // 2
real = rio

print("\n===== RESULTADOS =====")
print(f"Río real:        {real}")
print(f"Estimado:        {estimado}")
print(f"Error absoluto:  {abs(real - estimado)}")
print(f"Correcto (±{error}): {abs(real - estimado) <= error}")

print("\nZona final:")
print("Izquierda:", extremoIzquierda)
print("Derecha:   ", extremoDerecha)

print("\nValores alrededor del estimado:")
for i in range(max(0, estimado - 5), min(1000, estimado + 5)):
    print(i, escenario[i])


print("\n===== ESCENARIO (VISTA SIMPLE) =====\n")

max_val = max(escenario)

escala = max(1, max_val // 50)  # ajusta resolución vertical

for i in range(0, 1000, 10):  # salto horizontal para que sea legible

    valor = escenario[i]

    barras = "█" * (valor // escala)

    marcador = ""

    if i == rio:
        marcador += "  ← RÍO (mínimo)"

    # detectar meseta (comparación simple con anterior)
    if i > 0 and escenario[i] == escenario[i-1]:
        marcador += "  ─ meseta"

    print(f"{i:4} | {barras}{marcador}")









