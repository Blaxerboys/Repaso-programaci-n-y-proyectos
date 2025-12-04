import random
import pickle
import os.path


class Tour:

    def __init__(self, iden, titulo, descrip, importe, cantidad):
        self.iden = iden
        self.titulo = titulo
        self.descrip = descrip
        self.importe = importe
        self.cantidad = cantidad


def generador():
    iden = random.randint(1, 100)
    titulo = random.choice(("Tras las montañas", "Sierras de Córdoba"))
    descrip = random.choice(("El tour incluye visita guiada a Carlos Paz y La Falda.", "El Tour son 5 días."))
    importe = random.random()  # float
    cantidad = random.randint(5, 30)
    return Tour(iden, titulo, descrip, importe, cantidad)


def punto1(reg):
    tour = generador()
    der = len(reg) - 1
    izq = 0
    pos = der
    while izq <= der:
        cen = (izq + der) // 2
        if tour.iden == reg[cen].iden:
            pos = cen
            break
        elif tour.iden > reg[cen].iden:
            izq = cen + 1  # xd
        else:
            der = cen - 1
    if izq > der:
        pos = izq

    reg[pos:pos] = [tour]

    return reg


def punto2(reg):
    for i in reg:
        print("Identificador:", i.iden, "Titulo:", {i.titulo}, "Descripción:", i.descrip,
              "Importe:", {i.importe}, "Cantidad:", {i.cantidad})


def punto3(reg):
    p = int(input("Ingrese el valor maximo del Tour: "))
    m1 = "tour"
    archivo = open(m1, "wb")
    for i in reg:
        if i.importe < p:
            pickle.dump(i, archivo)
    archivo.close()
    return m1


def punto4(m1):
    reg = []
    archivo = open(m1, "rb")
    x = os.path.getsize(m1)  # xd
    while archivo.tell() < x:
        reg += [pickle.load(archivo)]
    punto2(reg)
    print("La cantidad de arreglos es de:", len(reg))
    archivo.close()


def punto5(reg):
    cod = int(input("Ingrese el cod que busca: "))
    # for i in range(reg):
    #     if i.iden == cod:
    #         punto2([i])
    #         x = i.descrip
    #         print(x)
    #         break
    #     else:
    #         print("No existe.")
    izq, der = 0, len(reg) - 1
    while izq <= der:
        cen = (izq + der) // 2
        if reg[cen].iden == cod:
            x = reg[cen].descrip
            print(x), punto2([reg[cen]])
            return x
        elif reg[cen].iden < cod:
            izq = cen + 1
        else:
            der = cen - 1
    print("No existe.")


def punto6(reg):
    # cont = [] * 26
    # for i in reg:
    #     cont[i.cantidad] = i
    # for j in cont:
    #     if j.cantidad != 0:
    #         punto2([j])
    cont = [0] * 26
    for i in reg:
        cont[i.cantidad - 5] += 1
    for i in cont:
        if i != 0:
            print(i)


def punto7(x):
    cont_palabras = 1
    condicional = 0
    inicio = False
    cont_vocales = 0
    xvieja = ""
    primera_palabra = False
    for i in x:
        if not primera_palabra:
            if i != "a" and i != "e" and i != "i" and i != "o" and i != "u" and i != " " and \
                    i != ".":
                inicio = True
            elif (i == "a" or i == "e" or i == "i" or i == "o" or i == "u") and inicio:
                cont_vocales += 1
            if cont_vocales >= 2 and (i == " " or i == "."):
                condicional += 1
            if i == " " or i == ".":
                cont_vocales = 0
                inicio = False
                primera_palabra = True
            xvieja = i
        else:
            if xvieja == " ":
                cont_palabras += 1
                if i != "a" and i != "e" and i != "i" and i != "o" and i != "u" and i != " " and \
                        i != ".":
                    inicio = True
            elif (i == "a" or i == "e" or i == "i" or i == "o" or i == "u") and inicio:
                cont_vocales += 1
            if cont_vocales >= 2 and (i == " " or i == "."):
                condicional += 1
            if i == " " or i == ".":
                cont_vocales = 0
                inicio = False
            xvieja = i
    print(condicional, cont_palabras)
