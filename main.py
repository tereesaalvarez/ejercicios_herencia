from clases.herencia_simple import *
from clases.herencia_real import *

# Ejercicio 1: Herencia Simple

if __name__ == '__main__':
    punto1 = Punto2D(1,4)
    punto1.translacion(3,2)
    print("Las coordenadas del putno nuevo son ({}, {})".format(punto1.x, punto1.y))

    punto2 = Punto3D(5,3,7)
    punto2.translacion(2,2,3)
    print("Las coordenadas del punto nuevo son ({},{})".format(punto2.x, punto2.y, punto2.z))



# Ejercicio 4: Herencia real

if __name__ == '__main__':
    print("Introduce la medida de la superficia de las ventanas")
    v_n = input("Ventana de la pared norte: ")
    v_s = input("Ventana de la pared sur: ")
    v_e = input("Ventana de la pared este: ")
    v_o = input("Ventana de la pared oeste: ")

    suma = casa.superficie_acristalada()
    print("La superficio total de las ventanas: ")