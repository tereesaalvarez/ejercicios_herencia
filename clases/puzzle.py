#Importamos la libreria funciones
import funciones
#Definimos el main
if __name__ == "__main__":
    d = funciones.D(1, 2, 3)
    print(isinstance(d, funciones.A),isinstance(d, funciones.B),isinstance(d, funciones.C))
    print(d.a, d.b, d.c)    
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

