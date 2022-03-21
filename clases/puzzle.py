#Importamos la libreria funciones
import funciones
#Definimos el main
if __name__ == "__main__":
    d = funciones.D(1, 2, 3)
    print(isinstance(d, funciones.A),isinstance(d, funciones.B),isinstance(d, funciones.C))
    print(d.a, d.b, d.c)    
    
