from tkinter import N
from clases.herencia_simple import *
from clases.herencia_real import *
from clases.herencia_diamante import *

# Ejercicio 1: Herencia Simple

if __name__ == '__main__':
    punto1 = Punto2D(1,4)
    punto1.translacion(3,2)
    print("Las coordenadas del putno nuevo son ({}, {})".format(punto1.x, punto1.y))

    punto2 = Punto3D(5,3,7)
    punto2.translacion(2,2,3)
    print("Las coordenadas del punto nuevo son ({},{})".format(punto2.x, punto2.y, punto2.z))


# Ejercicio 2: Puzzle

class Base: 
    def __init__(self): 
        self.a = "a" 
        self.b = "b" 
        self.c = "c" 
    def A(self): 
        print(self.a) 
 
    def B(self): 
        print(self.b) 
 
    def C(self): 
        print(self.c) 

#Una vez definida la clase Base, definimos la clase que deriva de dicha base igual que la anterior, haciendo uso de las herencias
class Derivada(Base): 
    def __init__(self): 
        self.a = "aa" 
        super().__init__() 
        self.c = "cc" 
    def A(self): 
        print(self.a) 
    def B(self): 
        self.b = "bb" 
        super().B() 
        print(self.b) 
#El resultado es el siguiente:
'''
a
b
bb
bb
c
cc
c
'''


# Ejercicio 3: Herencia diamante 
class A:
    def __init__(self, a):
        self.a = a

class B(A):
    def __init__(self, a, b):
        A.__init__(self, a)
        self.b = b
        
class C(A):
    def __init__(self, a, c):
        A.__init__(self, a)
        self.c = c

class D(B, C):
    def __init__(self, a, b, c):
        B.__init__(self, a, b)
        C.__init__(self, a, c)




# Ejercicio 4: Herencia real

if __name__ == '__main__':
    print("Introduce la medida de la superficia de las ventanas")
    v_n = input("Ventana de la pared norte: ")
    v_s = input("Ventana de la pared sur: ")
    v_e = input("Ventana de la pared este: ")
    v_o = input("Ventana de la pared oeste: ")

    suma = casa.superficie_acristalada()
    print("La superficio total de las ventanas: " + str(suma))

    print("Introduce la medida de la superficie de las paredes cortina")
    c_n = input("Cortina norte: ")
    c_s = input("Cortina sur: ")
    c_e = input("Cortina este: ")
    c_o = input("Cortina oeste: ")

    paredes_cortina = casa.superficie_acristalada(c_n, c_s, c_e, c_o)
    suma= paredes_cortina.superficie_acristalada()
    print("Esta es la superficie total de las paredes cortina: " +str(suma))