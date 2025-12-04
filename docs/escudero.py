from funciones import punto1, punto2, punto3, punto4, punto5, punto6, punto7, generador


def principal():
    primero = False
    tercero = False
    quinto = False
    reg = [generador()]

    op = int(input("Generar Tours: 1 \n"
                   "Mostrar Tours: 2 \n"
                   "Generar archivo: 3 \n"
                   "Mostrar archivo: 4 \n"
                   "Buscar un Tour: 5 \n"
                   "Cantidad de Tours: 6 \n"
                   "Procesamiento de texto: 7 \n"
                   "Salir: 0 \n"
                   "Ingrese su opciòn: "))

    while op != 0:
        if op == 1:
            y = int(input("Cantidad de arreglos: "))
            for i in range(y):
                reg = punto1(reg)
            primero = True
        elif op == 2 and primero:
            punto2(reg)
        elif op == 3 and primero:
            m1 = punto3(reg)
            tercero = True
        elif op == 4 and tercero:
            punto4(m1)
        elif op == 5 and primero:
            x = punto5(reg)
            quinto = True
        elif op == 6 and primero:
            punto6(reg)
        elif op == 7 and quinto:
            punto7(x)
        op = int(input("Generar Tours: 1 \n"
                       "Mostrar Tours: 2 \n"
                       "Generar archivo: 3 \n"
                       "Mostrar archivo: 4 \n"
                       "Buscar un Tour: 5 \n"
                       "Cantidad de Tours: 6 \n"
                       "Procesamiento de texto: 7 \n"
                       "Salir: 0 \n"
                       "Ingrese su opciòn: "))


if __name__ == "__main__":
    principal()
