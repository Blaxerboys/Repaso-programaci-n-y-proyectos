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
    iden = random.randint()
    titulo = random.choice(())
    descrip = random.choice(())
    importe = random.randrange()
    cantidad = random.randint()
    return Tour(iden, titulo, descrip, importe, cantidad)


def punto1(reg):
    izq, der = 0, len(reg) - 1
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
    return reg


def mostrar(reg):
    for i in reg:
        print("Identificador:", {reg[i].iden}, "Titulo:", {reg[i].titulo}, "Descripción:", {reg[i].descrip}, "Importe:",
              "Importe:", {reg[i].importe}, "Cantidad:", {reg[i].cantidad})


def punto3(reg):
    p = int(input("Ingrese un valor de maximos pasajeros: "))
    m1 = "programa"
    archivo = open(m1, "wb")
    for i in reg:
        if i.cantidad < p:
            pickle.dump(i, archivo)
    archivo.close()
    return m1


def punto4(m1):
    i = []
    archivo = open(m1, "rb")
    x = os.path.getsize(m1)
    while archivo.tell() < x:
        i += [pickle.load(archivo)]
    mostrar(i)
    print("La cantidad de registros es de: ", len(i))
    archivo.close()


def punto5(reg):
    x = int(input("Identificador: "))
    izq, der = 0, len(reg) - 1
    while izq <= der:
        cen = (izq + der) // 2
        if x == reg[cen].iden:
            i = [reg[cen]]
            mostrar(i)
            j = reg[cen].descrip
            return j
        elif x < reg[cen].iden:
            der = cen - 1
        else:
            izq = cen + 1
    print("No hay registro.")


def punto6(reg):
    i = [0] * 26
    for j in reg:
        i[j.cantidad - 5] += 1

    for k in range(i):
        if i[k] != 0:
            print("La cantidad maxima:", k + 5, "es de :", i[k])


def punto7(j):
    inicio = False
    condicion = False
    cont_vocales = 0
    for i in j:
        if i != "a" and i != "e" and i != "i" and i != "o" and i != "u" and i != " " and \
             i != ".":
            condicion = True
        if jvieja == " ":
            inicio = True
        elif (i == "a" or i == "e" or i == "i" or i == "o" or i == "u") and inicio:
            cont_vocales += 1

