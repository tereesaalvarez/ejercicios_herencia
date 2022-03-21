# Ejercicios_herencia_POO

Este trabajo ha sido realizado por Teresa Álvarez, Paula Naranjo y Miguel Ángel Guerra. Hemos realizado ejercicios de herencias, tanto simples como multiples, con sus respectivos diagramas UML.

Nuestra dirección de GitHub para este repositorio es la siguiente: https://github.com/tereesaalvarez/ejercicios_herencia.git

# Ejercicio 1: 
Herencia simple. Diagrama UML:

![Herencias_1](https://user-images.githubusercontent.com/100090620/159312235-d56fced3-02bd-46e7-944a-877e7dd1e653.PNG)



# Ejercicio 2:
Respuesta del ejercicio:

![Herencias_2](https://user-images.githubusercontent.com/100090620/159312560-d84049af-e678-4e0c-a0fe-959c94b8c80f.PNG)

El codigo es el siguiente:

```
#Empezamos a definir las clases y definimos los constructores para A, B y C
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
# Ejercicio 3:
```
#Importamos la libreria funciones
import funciones
#Definimos el main
if __name__ == "__main__":
    d = funciones.D(1, 2, 3)
    print(isinstance(d, funciones.A),isinstance(d, funciones.B),isinstance(d, funciones.C))
    print(d.a, d.b, d.c) 
    
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
        C.__init__(self, a, c)´´

![Herencias_3](https://user-images.githubusercontent.com/100090620/159312608-78295d34-df70-46a7-8033-39e5639dc534.PNG)

