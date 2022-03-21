from clases.herencia_simple import *

# Ejercicio 1: Herencia Simple

if __name__ == '__main__':
    punto1 = Punto2D(1,4)
    punto1.translacion(3,2)
    print("Las coordenadas del putno nuevo son ({}, {})".format(punto1.x, punto1.y))

    punto2 = Punto3D(5,3,7)
    punto2.translacion(2,2,3)
    print("Las coordenadas del punto nuevo son ({},{})".format(punto2.x, punto2.y, punto2.z))
    