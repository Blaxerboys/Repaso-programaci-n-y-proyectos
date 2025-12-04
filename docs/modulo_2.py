class Partido:
    def __init__(self, numero, nombre_j1, nombre_j2, ganador, codigo):
        self.numero = numero
        self.nombre_j1 = nombre_j1
        self.nombre_j2 = nombre_j2
        self.ganador = ganador
        self.codigo = codigo
import random

def generar_partido():
    numero = random.randint(1,1000)
    nombre_j1 = random.choice(("Pepe", "Juan", "Del Potro"))
    nombre_j2 = random.choice(("Nadal","Mariano","Ernesto"))
    ganador = random.choice((nombre_j2, nombre_j1, "Nadie"))
    codigo = random.randint(0,9)
    return Partido(numero, nombre_j1, nombre_j2, ganador, codigo)

def __str__(self):
    cadena = "Número: {} - Nombre_j1: {} - Nombre_j2: {} - Ganador: {} - Código: {}"\
    .format(self.numero, self.nombre_j1, self.nombre_j2, self.ganador, self.codigo)
    return cadena

def test():
    cadena = generar_partido()
    mostrar = __str__(cadena)
    print(mostrar)

if __name__ == "__main__":
    test()
