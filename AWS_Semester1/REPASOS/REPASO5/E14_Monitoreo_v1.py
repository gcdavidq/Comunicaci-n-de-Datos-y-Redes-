import random
import time

class Instancias:
    def __init__(self):
        self.instancias = {}

    #creamos una instancia
    def crear_instancia(self, nombre, cpu, memoria, almacenamiento):
        self.instancias[nombre] = {
            'CPU': int(cpu),
            'memoria': int(memoria),
            'almacenamiento': int(almacenamiento),
            'uso_cpu': 0,
            'uso_memoria': 0,
            'uso_almacenamiento': 0,
            'salud': ''
        }
        print(f"Se creó la instancia '{nombre}'")

    #simulamos el uso de la instancia creada. 
    def simulacion_de_uso(self, nombre):
        if nombre not in self.instancias:
            print(f"La instancia '{nombre}' no existe")
            return
        
        instancia = self.instancias[nombre]
        instancia['uso_cpu'] = random.randint(1, instancia['CPU'])
        instancia['uso_memoria'] = random.randint(2, instancia['memoria'])
        instancia['uso_almacenamiento'] = random.randint(200, instancia['almacenamiento'])

        print(f"\nSimulación de uso para '{nombre}':")
        print(f"  Uso de CPU: {instancia['uso_cpu']} / {instancia['CPU']}")
        print(f"  Uso de memoria: {instancia['uso_memoria']} / {instancia['memoria']}")
        print(f"  Uso de almacenamiento: {instancia['uso_almacenamiento']} / {instancia['almacenamiento']}")

    #imprimimos el uso de la instancia.
    def mostrar_uso(self, nombre):
        if nombre in self.instancias:
            estado = self.instancias[nombre]
            print(f"\nEstado de '{nombre}': {estado}")
        else:
            print(f"No existe la instancia '{nombre}'")

#creamos la clase GestorRecuperacion en caso sea necesario.
class GestorRecuperacion:
    #empleamos esta funcion en caso la instancia tenga una salud baja.
    def salud_baja(self, instancias, nombre):
        print(f"\nSalud baja detectada en la instancia '{nombre}'")
        instancia = instancias.instancias[nombre]

        cpu, memoria, almacenamiento = instancia['CPU'], instancia['memoria'], instancia['almacenamiento']
        uso_cpu, uso_memoria, uso_almacenamiento = instancia['uso_cpu'], instancia['uso_memoria'], instancia['uso_almacenamiento']

        if uso_cpu >= cpu * 0.75 or uso_memoria >= memoria * 0.75:
            print("  -> El CPU o la memoria está sobreusada")
            nombre_nueva_instancia = nombre + '_1'
            instancias.crear_instancia(nombre_nueva_instancia, cpu, memoria, almacenamiento)
            
            print("  -> Balanceando carga entre instancias")
            time.sleep(3)
            instancia['uso_cpu'] /= 2
            instancia['uso_memoria'] /= 2
            instancia['uso_almacenamiento'] /= 2
            
            nueva_instancia = instancias.instancias[nombre_nueva_instancia]
            nueva_instancia['uso_cpu'] = instancia['uso_cpu']
            nueva_instancia['uso_memoria'] = instancia['uso_memoria']
            nueva_instancia['uso_almacenamiento'] = instancia['uso_almacenamiento']

            print(f"  Nueva carga de '{nombre}': {instancia}")
            print(f"  Nueva carga de '{nombre_nueva_instancia}': {nueva_instancia}")
        
        elif uso_almacenamiento >= almacenamiento * 0.75:
            print("  -> El almacenamiento está llegando a su límite")
            print("  -> Eliminando caché de procesos en segundo plano")
            time.sleep(3)
            memoria_cache = random.randint(1, uso_almacenamiento)
            instancia['uso_almacenamiento'] -= memoria_cache
            print(f"  -> Almacenamiento después de limpiar caché: {instancia['uso_almacenamiento']} / {almacenamiento}")

    #implementamos esta instancia en caso la clase tenga una salud media
    def salud_media(self, instancias, nombre):
        print(f"\nSalud regular detectada en la instancia '{nombre}'")
        instancia = instancias.instancias[nombre]
        
        print(f"  Uso actual de los recursos: {instancia}")
        print("  -> Reduciendo el uso de recursos innecesarios")
        time.sleep(4)
        instancia['uso_cpu'] *= 0.9
        instancia['uso_memoria'] *= 0.9
        instancia['uso_almacenamiento'] *= 0.9
        print(f"  Nuevo uso de los recursos: {instancia}")

gestor_recuperacion = GestorRecuperacion()


#clase que monitorea la salud del servidor. 
class SaludServidor:
    def estado_instancia(self, nombre, instancias):
        instancia = instancias.instancias[nombre]
        cpu, memoria, almacenamiento = instancia['CPU'], instancia['memoria'], instancia['almacenamiento']
        uso_cpu, uso_memoria, uso_almacenamiento = instancia['uso_cpu'], instancia['uso_memoria'], instancia['uso_almacenamiento']
        
        #condicional que comprueba una baja salud del servidor.
        if uso_cpu >= cpu * 0.75 or uso_memoria >= memoria * 0.75 or uso_almacenamiento >= almacenamiento * 0.75:
            instancia['salud'] = 'baja'
            print(f"\nEl estado actual del servidor '{nombre}' es bajo.")
            gestor_recuperacion.salud_baja(instancias, nombre)
        
        #condicion que comprueba una salud media del servidor.
        elif uso_cpu >= cpu * 0.5 or uso_memoria >= memoria * 0.5 or uso_almacenamiento >= almacenamiento * 0.5:
            instancia['salud'] = 'regular'
            print(f"\nEl estado actual del servidor '{nombre}' es regular.")
            gestor_recuperacion.salud_media(instancias, nombre)

        #condicion que comprueba la buena salud del servidor.1
        else:
            instancia['salud'] = 'buena'
            print(f"\nEl estado actual del servidor '{nombre}' es bueno.")

salud_servidor = SaludServidor()

instanciasEC2 = Instancias()
instanciasEC2.crear_instancia('EC2_VIDEOJUEGOS', 6, 16, 512)

#realizamos un bucle para simular la instancia creada 4 veces.
for _ in range(5):
    instanciasEC2.simulacion_de_uso('EC2_VIDEOJUEGOS')
    instanciasEC2.mostrar_uso('EC2_VIDEOJUEGOS')
    salud_servidor.estado_instancia('EC2_VIDEOJUEGOS', instanciasEC2)
    time.sleep(1)  # Simular intervalo de tiempo
