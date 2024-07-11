'''
Ejercicio 8: Simulacion de in sistema de escalabildiad vertical y horizontal completo

Desarrollar un sistema completo que soporte tanto la escalabilidad vertical como
horizontal, simulando un entorno de servidor con balanceo de carga y ajuste automático de
capacidad.
'''
import random

# Clase que representa un servidor
class Server:
    def __init__(self, nombre, cpu_capacity, memory_capacity):
        """
        Inicializa un servidor con atributos específicos de capacidad.
        
        :param nombre: Nombre del servidor.
        :param cpu_capacity: Capacidad de CPU del servidor.
        :param memory_capacity: Capacidad de memoria del servidor.
        """
        self.nombre = nombre  # Nombre del servidor.
        self.cpu_capacity = cpu_capacity  # Capacidad de CPU.
        self.memory_capacity = memory_capacity  # Capacidad de memoria.
        self.current_cpu_load = 0  # Carga actual de CPU.
        self.current_memory_load = 0  # Carga actual de memoria.

    def scale_up(self, additional_cpu, additional_memory):
        """
        Aumenta la capacidad del servidor (escalabilidad vertical).
        
        :param additional_cpu: Capacidad adicional de CPU a añadir.
        :param additional_memory: Capacidad adicional de memoria a añadir.
        """
        self.cpu_capacity += additional_cpu
        self.memory_capacity += additional_memory
        print(f"{self.nombre}: Capacidad escalada (CPU: +{additional_cpu}, Memoria: +{additional_memory})")

    def handle_request(self, cpu_demand, memory_demand):
        """
        Maneja una solicitud, incrementando la carga actual según la demanda.
        
        :param cpu_demand: Demanda de CPU de la solicitud.
        :param memory_demand: Demanda de memoria de la solicitud.
        :return: True si la solicitud es manejada, False si no puede ser manejada.
        """
        if self.current_cpu_load + cpu_demand <= self.cpu_capacity and self.current_memory_load + memory_demand <= self.memory_capacity:
            self.current_cpu_load += cpu_demand
            self.current_memory_load += memory_demand
            print(f"{self.nombre}: Solicitud manejada (CPU: {cpu_demand}, Memoria: {memory_demand})")
            return True
        else:
            print(f"{self.nombre}: Solicitud rechazada por falta de recursos")
            return False

    def release_resources(self, cpu_demand, memory_demand):
        """
        Libera los recursos utilizados por una solicitud.
        
        :param cpu_demand: Demanda de CPU de la solicitud.
        :param memory_demand: Demanda de memoria de la solicitud.
        """
        self.current_cpu_load -= cpu_demand
        self.current_memory_load -= memory_demand
        print(f"{self.nombre}: Recursos liberados (CPU: {cpu_demand}, Memoria: {memory_demand})")

# Clase que administra un clúster de servidores
class ServerCluster:
    def __init__(self):
        """
        Inicializa un clúster de servidores vacío.
        """
        self.servidores = []  # Lista de servidores en el clúster.

    def agregar_servidor(self, servidor):
        """
        Agrega un servidor al clúster.
        
        :param servidor: Instancia del servidor a añadir.
        """
        self.servidores.append(servidor)
        print(f"Servidor {servidor.nombre} añadido al clúster")

    def remover_servidor(self):
        """
        Remueve el último servidor del clúster.
        """
        if self.servidores:
            servidor_removido = self.servidores.pop()
            print(f"Servidor {servidor_removido.nombre} removido del clúster")
        else:
            print("No hay servidores para remover")

    def distribuir_solicitudes(self, solicitudes):
        """
        Distribuye las solicitudes entre los servidores disponibles.
        
        :param solicitudes: Lista de solicitudes a distribuir.
        """
        for solicitud in solicitudes:
            cpu_demand, memory_demand = solicitud
            handled = False
            for servidor in self.servidores:
                if servidor.handle_request(cpu_demand, memory_demand):
                    handled = True
                    break
            if not handled:
                print("La solicitud no pudo ser manejada por ningún servidor")

    def liberar_recursos(self, solicitudes):
        """
        Libera los recursos utilizados por una lista de solicitudes.
        
        :param solicitudes: Lista de solicitudes a liberar.
        """
        for solicitud in solicitudes:
            cpu_demand, memory_demand = solicitud
            for servidor in self.servidores:
                if servidor.current_cpu_load >= cpu_demand and servidor.current_memory_load >= memory_demand:
                    servidor.release_resources(cpu_demand, memory_demand)
                    break

# Clase que ajusta automáticamente la capacidad del clúster
class AutoScaler:
    def __init__(self, cluster, cpu_threshold, memory_threshold):
        """
        Inicializa el autoescalador con el clúster y umbrales específicos.
        
        :param cluster: Instancia del clúster de servidores.
        :param cpu_threshold: Umbral de CPU para activar el escalado.
        :param memory_threshold: Umbral de memoria para activar el escalado.
        """
        self.cluster = cluster  # Clúster de servidores.
        self.cpu_threshold = cpu_threshold  # Umbral de CPU.
        self.memory_threshold = memory_threshold  # Umbral de memoria.

    def ajustar_capacidad(self):
        """
        Ajusta la capacidad del clúster según los umbrales de CPU y memoria.
        """
        total_cpu_load = sum(servidor.current_cpu_load for servidor in self.cluster.servidores)
        total_memory_load = sum(servidor.current_memory_load for servidor in self.cluster.servidores)
        total_cpu_capacity = sum(servidor.cpu_capacity for servidor in self.cluster.servidores)
        total_memory_capacity = sum(servidor.memory_capacity for servidor in self.cluster.servidores)

        if total_cpu_load / total_cpu_capacity > self.cpu_threshold or total_memory_load / total_memory_capacity > self.memory_threshold:
            # Escalar horizontalmente añadiendo un nuevo servidor
            nuevo_servidor = Server(f"Servidor {len(self.cluster.servidores) + 1}", 100, 200)
            self.cluster.agregar_servidor(nuevo_servidor)
            print("Escalado horizontal: Se añadió un nuevo servidor")
        elif total_cpu_load / total_cpu_capacity < self.cpu_threshold / 2 and total_memory_load / total_memory_capacity < self.memory_threshold / 2:
            # Escalar horizontalmente removiendo un servidor
            self.cluster.remover_servidor()
            print("Escalado horizontal: Se removió un servidor")

        # Escalado vertical: incrementar capacidad de los servidores actuales
        for servidor in self.cluster.servidores:
            if servidor.current_cpu_load / servidor.cpu_capacity > self.cpu_threshold:
                servidor.scale_up(10, 20)  # Aumentar capacidad de CPU y memoria
            if servidor.current_memory_load / servidor.memory_capacity > self.memory_threshold:
                servidor.scale_up(10, 20)  # Aumentar capacidad de CPU y memoria

# Simulación de la llegada de solicitudes y ajuste dinámico de capacidad
def simular_trabajo():
    """
    Simula la llegada de solicitudes y el ajuste dinámico de la capacidad del clúster.
    """
    # Inicializa el clúster y el autoescalador
    cluster = ServerCluster()
    autoescalador = AutoScaler(cluster, cpu_threshold=0.7, memory_threshold=0.7)

    # Agrega servidores iniciales al clúster
    cluster.agregar_servidor(Server("Servidor 1", 100, 200))
    cluster.agregar_servidor(Server("Servidor 2", 100, 200))

    for _ in range(10):  # Simular 10 ciclos de trabajo
        solicitudes = [(random.randint(10, 50), random.randint(20, 60)) for _ in range(5)]  # Genera solicitudes aleatorias
        print("\n--- Ciclo de trabajo ---")
        cluster.distribuir_solicitudes(solicitudes)  # Distribuye las solicitudes entre los servidores
        autoescalador.ajustar_capacidad()  # Ajusta la capacidad del clúster
        cluster.liberar_recursos(solicitudes)  # Libera los recursos después de manejar las solicitudes

# Ejecuta la simulación
simular_trabajo()
