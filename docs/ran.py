import random
import os.path
import pickle


class Tour:
    def __init__(self, iden, titulo, descrip, importe, cantidad):
        self.iden = iden
        self.titulo = titulo
        self.descrip = descrip
        self.importe = importe
        self.cantidad = cantidad


def generador():
    iden = random.randint(1, 100)
    titulo = random.choice(())
    descrip = random.choice(())
    importe = random.random() * 10
    cantidad = random.randint()
    return Tour(iden, titulo, descrip, importe, cantidad)


def punto1(reg):
    izq, der = 0, len(reg)
    pos = der
    tour = generador()
    while izq <= der:
        cen = (izq + der) // 2
        if tour.iden == reg[cen].iden:
            pos = cen
            break
        elif tour.iden < reg[cen].iden:
            der = cen - 1
        else:
            izq = cen + 1
    if izq > der:
        pos = izq
    reg[pos:pos] = [tour]


def punto2(reg):
    for i in reg:
        print("Identificador:", {reg[i].iden}, "Titulo:", {reg[i].titulo}, "Descripción:", {reg[i].descrip}, "Importe:",
              {reg[i].importe}, "Cantidad:", {reg[i].cantidad})


def punto3(reg):
    x = int(input("Ingrese la cantidad maxima de pasajeros: "))
    m1 = "archivo"
    archivo = open(m1, "wb")
    for i in reg:
        if x > reg[i].cantidad:
            pickle.dump(reg[i], archivo)
    archivo.close()
    return m1


def punto4(m1):
    i = []
    x = os.path.getsize(m1)
    archivo = open(m1, "rb")
    while archivo.tell() < x:
        i += [pickle.load(archivo)]
    punto2(i)
    print("La cantidad de archivos es:", len(i))
    archivo.close()


def punto5(reg):
    x = int(input("Identificador: "))
    izq, der = 0, len(reg)
    while izq <= der:
        cen = (izq + der) // 2
        if x == reg[cen].iden:
            punto2([reg[cen]])
            return reg[cen].descrip
        elif x < reg[cen].iden:
            der = cen - 1
        else:
            izq = cen + 1
    print("No existe.")


def punto6(reg):
    i = [0] * 26
    for j in reg:
        i[j.cantidad - 5] += 1
    for k in range(i):
        if i[k] != 0:
            print("la cantidad de viajes para un maximo de:", k + 5, "es de:", i[k])


def punto7(x):
    inicio = False
    bandera = False
    vocales = 0
    contador = 0
    principio = True
    for i in x:
        if i != "a" and i != "e" and i != "i" and i != "o" and i != "u" and principio:
            inicio = True
        if not (i != "a" and i != "e" and i != "i" and i != "o" and i != "u") and inicio:
            vocales += 1
        if vocales == 2 and (i == " " or i == "."):
            contador += 1
        if i == " ":
            vocales = 0
            inicio = False
        else:
            if ivieja == " ":
                if i != "a" and i != "e" and i != "i" and i != "o" and i != "u":
                    inicio = True

            elif not(i != "a" and i != "e" and i != "i" and i != "o" and i != "u") and inicio:
                vocales += 1
            if vocales == 2 and (i == " " or i == "."):
                contador += 1
            if i == " ":
                vocales = 0
                inicio = False
