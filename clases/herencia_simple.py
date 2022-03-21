from tkinter import Y


class Punto2D:
    def __init__(self, x, y):
        self.y= y
        self.x= x
    def translacion(self, a, b):
        self.y = self.y + b
        self.x = self.x + a

class Punto3D(Punto2D):
    def __init__(self, x, y, z):
        Punto2D.__init__(self, x, y)
        self.z = z