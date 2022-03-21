# Ejercicios_herencia_POO

Este trabajo ha sido realizado por Teresa Álvarez, Paula Naranjo y Miguel Ángel Guerra. Hemos realizado ejercicios de herencias, tanto simples como multiples, con sus respectivos diagramas UML.

Nuestra dirección de GitHub para este repositorio es la siguiente: https://github.com/tereesaalvarez/ejercicios_herencia.git

# Ejercicio 1: 
Herencia simple. Diagrama UML:

![Herencias_1](https://user-images.githubusercontent.com/100090620/159312235-d56fced3-02bd-46e7-944a-877e7dd1e653.PNG)

    class Punto2D:
        def __init__(self, x, y):
            self.x= x
            self.y= y
        
        def translacion(self, a, b):
            self.x = self.x + a
            self.y = self.y + b
        

    class Punto3D(Punto2D):
        def __init__(self, x, y, z):
            Punto2D.__init__(self, x, y)
            self.z = z

        def translacion2(self, a, b, c):
            self.x = self.x + a
            self.y = self.y + b
            self.z = self.z + c 
        


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
        a
        b
        bb
        bb
        c
        cc
        c

```


# Ejercicio 3:


![Herencias_3](https://user-images.githubusercontent.com/100090620/159312608-78295d34-df70-46a7-8033-39e5639dc534.PNG)

El codigo es el siguiente:

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


# Ejercicio 4

El codigo es el siguiente:

        class casa:
            def __init__(self,ventana_n, ventana_s, ventana_e, ventana_o):
                self.ventana_n = ventana_n
                self.ventana_s = ventana_s
                self.ventana_e = ventana_e
                self.ventana_o = ventana_o

            def superficie_acristalada(self):
                suma = int(self.ventana_n) + int(self.ventana_s) + int(self.ventana_e) + int(self.ventana_o)
                return suma 

        def proteccion():
            print("¿Quieres proteccion en la ventana? si o no?")
            respuesta = input()
            if respuesta == "si":
                print("¿Cual es?")
                opciones = ["persianas", "estor", "cortinas", "mosquitera"]
                print(opciones)
                cuales = input()
                if cuales not in opciones:
                    print("Error, no es una opcion valida")
                    proteccion()
                else:
                    print("Opcion valida")
            else:
                raise Exception("No se ha excogido ninguna proteccion")
