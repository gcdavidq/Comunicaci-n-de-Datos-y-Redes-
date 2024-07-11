'''
Ejercicio2: RESUMEN DEL MODELO OSI

Comprender el modelo OSI y su aplicacion en redes.
'''
class OSIModel:
    def __init__(self, data):
        self.data=data
    
    def capa_aplicacion(self):
        print("Capa de Aplicacion: Procesando datos", self.data)
        self.data="aplicacion_procesada("+ self.data +")"
        self.capa_presentacion()
    
    def capa_presentacion(self):
        print("Capa de Presentacion: Formateando data", self.data)
        self.data="presentacion_procesada("+ self.data +")"
        self.capa_session()
    
    def capa_session(self):
        print("Capa de Session: Manejando la sesion de la data", self.data)
        self.data="session_procesada("+self.data+")"
        self.capa_transporte()
    
    def capa_transporte(self):
        print("Capa Transporte: Segmentando data", self.data)
        self.data="Transporte_Procesado ("+ self.data +")"
        self.capa_red()
    

    def capa_red(self):
        print("Capa de red: Enrutando data", self.data)
        self.data="Redes_Procesado ("+self.data+")"
        self.capa_enlace_datos()
    
    def capa_enlace_datos(self):
        print("Capa de enlace de datos: Fragmentando data", self.data)
        self.data="Enlace De Datos_Procesado("+ self.data +")"
        self.capa_fisica()
    
    def capa_fisica(self):
        print("Capa Fisica: Transmitiendo data", self.data)
        self.data="Fisica_Procesada("+self.data+")"
        print("Transmision final de los datos:", self.data)

#USO
osi_model=OSIModel(data="Hello World")
osi_model.capa_aplicacion()