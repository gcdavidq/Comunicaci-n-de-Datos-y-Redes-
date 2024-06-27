# Importamos librerías
import time
import random as rd


def ejercicio14():
  marco = '*'*80
  enunciado = '''
  Ejercicio 14: \n  Desarrollar un sistema que monitoree la salud de los servidores y realice
  recuperaciones automáticas en caso de fallos.\n'''
  print(marco + enunciado + marco)

ejercicio14()
print('#'*80)


class Servidor():
  '''Esta clase permite crear instancias y
     simular el uso de estas. 
  '''

  def __init__(self):
    self.instancias = {} 

  # Función que me permite crear una instancia  
  def crear_instancia(self, nombre_instancia, cpu, memoria, almacenamiento, red):
    self.instancias[nombre_instancia] = {'CPU':cpu,
                                         'memoria': memoria,
                                         'almacenamiento': almacenamiento,
                                         'red':red,
                                         'uso_cpu':0,
                                         'uso_memoria':0,
                                         'uso_almacenamiento':0,
                                         'uso_red':0}
    print("Creando instancia ...")
    # time.sleep(3)
    print(f"- Se creo la instancia {nombre_instancia}:")

  
  # Función que permite simular el uso de una instancia
  def simulacion_de_uso(self, nombre_instancia, uso_ejemplo, cpu_uso, memoria_uso, almacenamiento_uso):
    if nombre_instancia not in self.instancias:
      print(f"La instancia {nombre_instancia} no existe!")
        
    uso_cpu = rd.randint(uso_ejemplo, cpu_uso)
    uso_memoria = rd.randint(4, memoria_uso)
    uso_almacenamiento = rd.randint(4, almacenamiento_uso)
    uso_red = rd.uniform(1, 2)
    
    self.instancias[nombre_instancia]['uso_cpu'] = (uso_cpu*100)/self.instancias[nombre_instancia]['CPU']
    self.instancias[nombre_instancia]['uso_memoria'] = (uso_memoria*100)/self.instancias[nombre_instancia]['memoria']
    self.instancias[nombre_instancia]['uso_almacenamiento'] = (uso_almacenamiento*100)/self.instancias[nombre_instancia]['almacenamiento']
    self.instancias[nombre_instancia]['uso_red'] = uso_red


class HealthMonitor:
  '''Esta clase permite mostrar el registro del estado de
     las instancias.
  '''
  def __init__(self):
    self.registro = {'Nombre':[],
                     'CPU': [],
                     'Memoria': [],
                     'Almacenamiento': [],
                     'Red':[]}
    
  # Función que permite mostrar el estado de las instancias
  def mostrar_registro(self, servidores):
    if len(servidores.instancias) == 0:
      print(f"No hay información de servidores!")

    for i, instancia in enumerate(servidores.instancias):
      estado_cpu = servidores.instancias[instancia]['uso_cpu']
      estado_memoria = servidores.instancias[instancia]['uso_memoria']
      estado_almacenamiento = servidores.instancias[instancia]['uso_almacenamiento']
      estado_red = servidores.instancias[instancia]['uso_red']
      
      if instancia in self.registro['Nombre']: # En caso la instancia ya esté registrada
                                               # solamente se actualiza el uso de la CPU
        indice = self.registro['Nombre'].index(instancia)
        self.registro['CPU'][indice] = estado_cpu
          
      else:
        self.registro['Nombre'].append(instancia)
        self.registro['CPU'].append(estado_cpu)
        self.registro['Memoria'].append(estado_memoria)
        self.registro['Almacenamiento'].append(estado_almacenamiento)
        self.registro['Red'].append(estado_red)

      print(f'{instancia}')
      print(f"  Uso de CPU: {estado_cpu} %.")
      print(f"  Uso de memoria: {estado_memoria} %.")
      print(f"  Uso de almacenamiento: {estado_almacenamiento} %.")
      print(f"  Uso de red lantencia: {estado_red:.2f} ms.")


class RecoveryManager:
  '''Esta clase permite detectar fallos en caso el uso de los recursos
     de las instancias sobrepasan el límite en base al reporte de la
     clase HealthMonitor. 
  '''
  def __init__(self, reporte, instanciasServidor):
    self.reporte = reporte
    self.instanciasServidor = instanciasServidor
  
  # Función que permite mostrar el reporte general
  def reporte_mensaje(self):
    nombres_instancias = self.reporte.registro['Nombre']
    cantidad_instancias = len(nombres_instancias)
    promedio_CPU = sum(self.reporte.registro['CPU'])/cantidad_instancias
    promedio_latencia = sum(self.reporte.registro['Red'])/cantidad_instancias
    
    print("\n------------------ REPORTE DE MONITOREO ------------------")
    print(f"Servidores disponibles: \n{nombres_instancias}.")
    print(f"El uso promedio de las CPU's es de: {promedio_CPU:.2f} %.")
    print(f"El tiempo promedio de latencia es de: {promedio_latencia} ms.")

    return nombres_instancias, cantidad_instancias, promedio_CPU, promedio_latencia

  # Función que permite detectar fallos en nuestras instancias 
  def deteccion_fallos(self):
    nombres_instancias, cantidad_instancias, promedio_CPU, promedio_latencia = self.reporte_mensaje()
    print('#'*80)

    
    if promedio_CPU >= 80.0: # En caso el uso del recurso promedio de la CPU sea mayor al 80%
      nombre = f'Server_N{cantidad_instancias +1}'
      self.instanciasServidor.crear_instancia(nombre, 8, 256, 1000, 1)
      self.instanciasServidor.simulacion_de_uso(nombre,4, 6, 150, 990)

      numero_instancias = len(self.instanciasServidor.instancias)
      nuevo_portentaje_estado_cpu = (promedio_CPU*(numero_instancias -1))/ numero_instancias

      for nomb in self.instanciasServidor.instancias:
        self.instanciasServidor.instancias[nomb]['uso_cpu'] = nuevo_portentaje_estado_cpu

      self.reporte.mostrar_registro(instanciasServidor)
      self.reporte_mensaje()
    


# Creamos los servidores
print("CREAR INSTANCIAS:")
# 1
instanciasServidor = Servidor()
instanciasServidor.crear_instancia('Server_N1', 8, 256, 1000, 1)# Nombre, núcleos, memoria, almacenamiento, latencia.
instanciasServidor.simulacion_de_uso('Server_N1',7,  8, 150, 990)# Nombre, (uso_lim_inferior, uso_lim_superior),
                                                                   # memoria_uso, almacenamiento_uso.
# 2
instanciasServidor.crear_instancia('Server_N2', 8, 256, 1000, 1)
instanciasServidor.simulacion_de_uso('Server_N2',7, 8, 150, 990)

# 3
instanciasServidor.crear_instancia('Server_N3', 8, 256, 1000, 1)
instanciasServidor.simulacion_de_uso('Server_N3',7, 8, 150, 990)
print('#'*80)


# Mostramos el estado de las intancias
print("ESTADOS DE LAS INSTANCIAS:")
monitor = HealthMonitor()
monitor.mostrar_registro(instanciasServidor)
print('#'*80)


# Gestionamos las instancias
gestor = RecoveryManager(monitor, instanciasServidor)
gestor.deteccion_fallos()
