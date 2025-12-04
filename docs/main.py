# Un club que acostumbra a organizar torneos de tenis necesita un programa que
# permita organizar los partidos de esos torneos. De cada partido se registra:
# el número de partido (un número entero de 1 en adelante), el nombre del jugador 1,
# el nombre del jugador 2, el ganador (una cadena, puede estar vacío),
# el código del torneo (un número entre 0 y 9 correspondiente al código del
# torneo al que pertenece el partido). Se desea almacenar la información referida
# a los n partidos en un arreglo de registros de tipo Partido (definir el tipo
# Partido y cargar n por teclado).
#
# Se pide desarrollar un programa en Python controlado por un menú de opciones y
# que posea como mínimo dos módulos, que permita gestionar las siguientes tareas:
#
# 1- Cargar el arreglo pedido con los datos de los n partidos. Valide que el
# número de partido sea mayor o igual a 1, y que el código de torneo sea mayor
# o igual a 0 y menor o igual a 9. Puede hacer la carga en forma manual,
# o puede generar los datos en forma automática (con valores aleatorios) o
# puede disponer de ambas técnicas si lo desea. Pero al menos una debe programar.
#
# 2- Mostrar todos los datos de las partidos que no se han jugado aún
# (es decir donde el campo ganador esté vacío), a razón de un registro por
# línea ordenados por número de partido de menor a mayor. Mostrar solo el
# número de partido, el nombre del jugador 1, el nombre del jugador 2 y el código de torneo.
#
# 3- Determinar y mostrar la cantidad de partidos no jugados (el ganador sigue vacío)
# por cada uno de los códigos de torneo. En total, 10 contadores.
# Mostrar todos los valores cuyo resultado sea mayor a 0.
#
# 4- Determinar y mostrar el código de torneo con mayor cantidad de partidos sin jugar.
# (Reutilizar lo realizado en el punto 3). En el caso de existir más de un torneo con
# la misma cantidad de partidos pendientes, mostrar solo el primero encontrado.
#
# 5- Determinar si existe un partido para el número p siendo p un valor que se carga
# por teclado. Si existe mostrar sus datos. Si no existe, informar con un mensaje.
# Si existe más de un partido con el mismo número solo mostrar el primero.
import random

from modulo_2 import generar_partido, __str__


def principal():
    print("Partido Número: 1\n"
          "Partidos no jugados (Datos): 2\n"
          "Partidos no jugados (Cantidad): 3\n"
          "Partido no juado(Código): 4\n"
          "Buscar un partido por su codigo: 5\n"
          "salir: 0")
    respuesta = int(input("Respuesta: "))
    while respuesta != 0:
        if respuesta == 1:
            opcion = int(input("Cantidad de partidos manual(1) o automatica(0): "))
            if opcion == 1:
                nro_partida = int(input("Ingrese la cantidad de partidos que se van a jugar: "))
                while nro_partida >= 0 and nro_partida <= 9:
                    nro_partida = int(input("Ingrese un número valido"))
            elif opcion == 0:
                nro_partido = random.randint(0, 9)
                partido = [0] * nro_partido
            for i in range(nro_partido):
                partido[i] = generar_partido()
            opcion = int(input("Mostrar los partidos = 1: "))
            if opcion == 1:
                cadena = __str__(partido[i])
                print(cadena)
        elif respuesta == 2:
            for i in range(nro_partido):
                for j in range(nro_partido):
                    if partido[i].numero >= partido[j].numero:
                        partido[i], partido[j] = partido[j], partido[i]
            for i in range(nro_partido):
                if partido[i].ganador == "Nadie":
                    cadena = __str__(partido[i])
                    print(cadena)
        elif respuesta == 3:
            cant_part_no_jugados = [0] * 10
            for i in range(nro_partido):
                if partido[i].ganador == "Nadie":
                    cant_part_no_jugados[partido[i].codigo] += 1
            for i in range(10):
                if cant_part_no_jugados[i] > 0:
                    print("los partidos con Código:", i, "tienen", cant_part_no_jugados[i])
        elif respuesta == 4:
            mayor = cant_part_no_jugados[0]
            cant_viejo = 0
            for i in range(10):
                if cant_part_no_jugados[i] > cant_viejo:
                    mayor = cant_part_no_jugados[i]
                cant_viejo = cant_part_no_jugados[i]
            print("El Código del partido con más veces sin jugar es:", mayor)
        elif respuesta == 5:
            p = int(input("Ingrese el Códiogo del partido: "))
            for i in range(nro_partido):
                if p == partido[i].codigo:
                    cadena = __str__(partido[i])
                    print(cadena)
                    break
        else:
            print("No es una opcion valida")

        print("Partido Número: 1\n"
              "Partidos no jugados (Datos): 2\n"
              "Partidos no jugados (Cantidad): 3\n"
              "Partido no juado(Código): 4\n"
              "Buscar un partido por su codigo: 5\n"
              "salir: 0")
        respuesta = int(input("Respuesta: "))


if __name__ == "__main__":
    principal()
