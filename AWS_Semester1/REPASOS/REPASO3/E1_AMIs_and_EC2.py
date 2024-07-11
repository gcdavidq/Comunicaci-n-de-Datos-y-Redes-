'''
Ejercicio 1: Simulación completa de Amazon EC2 y gestión de AMIs
'''

class AMI:
    def __init__(self):
        self.amis={}


    
    def crear_AMIs(self, nombre, so, aplicaciones, librerias):
        self.amis[nombre]={'SO':so, 
                                        'Aplicaciones':aplicaciones, 
                                        'Librerias': librerias
                                        }
        
        print(f"Creaste la AMI '{nombre}' con las siguientes caracteristicas de Software:\n SO: {so} \n Aplicaciones: {aplicaciones} \n Librerias: {librerias}")
    
    def seleccionar_AMI(self, nombre):
        if nombre in self.amis:
            AMI=self.amis[nombre]
            print(f"Seleccionaste la AMI '{nombre}' que contiene lo siguiente: \n SO: {AMI['SO']} \n Aplicaciones: {AMI['Aplicaciones']}, \n Librerias: {AMI['Librerias']}")
        
        else:
            print(f"No existe una AMI con el nombre {nombre}")

ami=AMI()

class EC2:

    def __init__(self):
        self.instancias={}

    def crear_instancias(self, ami, nombre_ami, nombre, cpu, memoria, almacenamiento):
        if nombre_ami in ami.amis:
            ami_seleccionada = ami.amis[nombre_ami]
            self.instancias[nombre]= {"AMI": ami_seleccionada, 
                                      'CPU': cpu, 
                                      'Memoria': memoria, 
                                      'Almacenamiento': almacenamiento,
                                      'Estado':'Pendiente' }
            print(f"Se creó la instancia {nombre}")
        else:
            print("No existe el AMI seleccionada. Primero crea una")
    
    def iniciar_instancia(self, nombre):
        if nombre in self.instancias:
            self.instancias[nombre]['Estado']='Iniciado'
            self.instancias[nombre]['Proceso']='Trabajando con EBS'
            print(f"Estado actual de la instancia {nombre}: \n Estado: {self.instancias[nombre]['Estado']} \n Proceso: {self.instancias[nombre]['Proceso']}")
        else:
            print(f"No existe la instancia {nombre}")
    
    def detener_instancia(self, nombre):
        if nombre in self.instancias:
            self.instancias[nombre]['Estado']='Detenido'
            self.instancias[nombre]['Proceso']='Se detuvo el volumen EBS'
            print(f"Se detuvo la instancia, ahora este es su estado:\n Nombre: {nombre} \n Estado:{self.instancias[nombre]['Estado']}")
        else:
            print(f"No existe la instancia {nombre}")
    
    def terminar_instancia(self, nombre):
        if nombre in self.instancias:
            print("Se está deteniendo la instancia")
            self.instancias[nombre]['Estado']='Terminado'
            self.instancias[nombre]['Proceso']={}
            print(f"Se eliminó la instancia {nombre}")
    
    def registro_instancias(self):
        print("SE IMPRIMIRÁ EL REGISTRO ACTUAL DE LAS INSTANCIAS")

        for nombre in self.instancias:
            print(f"Nombre de la instancia {nombre}:")
            print(f" AMI: {self.instancias[nombre]['AMI']}")
            print(f" Estado: {self.instancias[nombre]['Estado']}")         




ec2=EC2()

#crear una AMI
ami.crear_AMIs('AMI1', 'Linux', 'Fotos, Videos, Python', 'Librerias necesarias para ejecutar codigo')

#crear una instancia
ec2.crear_instancias(ami, 'AMI1', 'Instancia1', 8,10, 50)

#detener una instancia
ec2.detener_instancia('Instancia1')
ec2.registro_instancias()

