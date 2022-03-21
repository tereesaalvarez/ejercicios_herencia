    
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