from tkinter import Y


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