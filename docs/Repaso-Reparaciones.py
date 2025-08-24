# clase nombre_de_la_clase:
class Oferentes:
    def __init__(self, nombre, dias, importe): #def __init__(self,1,2)
        self.nombre = nombre                   #__init__ y self son keywords.
        self.dias = dias                       #nombre, dias = características.
        self.importe = importe                 #self.1 = comportamiento.

cantidad_de_ofertas = int(input("Cuantas ofertas desea cargar: "))
parametro_dias = int(input("Cuantos dias usamos de parametro: "))
lista_de_ofertas = []                          #[] seldas de memoria.
importe_i = 0                                  #int, str, float.
importe_viejo = 99999999999999999999999999     #Se crean variables que seran
rapidito = 0                                   #ocupadas más adelante.

def generar_ofertas():                         #funcion nombre(parametros de entrada):
    nombre = input("Nombre de la empresa: ")   #definis variables y luego las
    dias = int(input("Días de trabajo: "))     #pasas a la clase con
    importe = int(input("Importe: "))          #nombre_de_clase(características).
    return Oferentes(nombre, dias, importe)    #return devuelbe a la variable que la llamó.


for i in range(cantidad_de_ofertas):           #bucle itera i por cada uno de
    print(f"\nOferta #{i + 1}")                #los valores de range.
    #Creo los objetos oferas                    llama a la función(parámetros).
    oferta = generar_ofertas()                 #.append agrega el objeto en
    #Cargo los objetos en una lista             seldas de memoria distintas
    lista_de_ofertas.append(oferta)
    #Junto todos los importes en inportes_i
    importe_i = lista_de_ofertas[i].importe + importe_i
    #Comparo todos los importes
    importe_actual = lista_de_ofertas[i].importe
    if importe_actual < importe_viejo:
        importe_viejo = importe_actual
        #Consigo el nombre con la iteación i
        nombre_barato = lista_de_ofertas[i].nombre
    #Calculo el porcentaje
    if lista_de_ofertas[i].dias <= parametro_dias:
        rapidito = rapidito + 1

#Genero cálculos
importe_promedio = importe_i // cantidad_de_ofertas
porcentaje = 100 * rapidito // cantidad_de_ofertas

#Prints (f me deja meter variables sin necesidad de las comas)
print(f"El promedio de importes es: {importe_promedio}")
print(f"¡Oferton! {nombre_barato}, te cobra ${importe_viejo}")
print(f"la cantidad de ofertas que se encuentran por debajo de {parametro_dias} días es de {porcentaje}%")
