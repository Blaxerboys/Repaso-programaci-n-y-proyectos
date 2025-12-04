import random


def truco():
    cont = 1
    x = ""
    puntaje_final = 0
    while x != "T":
        x = input("Ingrese su opcion: ")
        if x == "T":
            cont += 1
            puntaje_final = cont + 1


def envido():
    pass


op = ""
while op != 0:
    print("Truco: T\n"
          "Envido: E\n"
          "Salir: S")
    op = input("Infrese su opción")
    if op == "T":
        truco()
    elif op == "E":
        envido()
