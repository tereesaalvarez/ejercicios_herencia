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