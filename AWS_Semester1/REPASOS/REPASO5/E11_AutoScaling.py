'''
Ejercicio 11: Implementacion de elasticidad con Auto Scaling Groups y politicas personalizadas
Desarrollar un sistema de Auto Scaling Group completo con políticas de escalado
personalizadas y simulación de carga.

'''
import random
import time

# Clase que define la configuración de las instancias de servidor
class ServerTemplate:
    def __init__(self, cpu_capacity, memory_capacity):
        self.cpu_capacity = cpu_capacity
        self.memory_capacity = memory_capacity

    def create_server(self):
        return Server(self.cpu_capacity, self.memory_capacity)

# Clase que representa un servidor
class Server:
    def __init__(self, cpu_capacity, memory_capacity):
        self.cpu_capacity = cpu_capacity
        self.memory_capacity = memory_capacity
        self.cpu_usage = 0  # Uso de CPU actual
        self.memory_usage = 0  # Uso de memoria actual
        self.network_latency = 0  # Latencia de red actual

    def handle_request(self, cpu_load, memory_load, network_latency):
        self.cpu_usage += cpu_load
        self.memory_usage += memory_load
        self.network_latency += network_latency

    def reset_usage(self):
        self.cpu_usage = 0
        self.memory_usage = 0
        self.network_latency = 0

    def __str__(self):
        return (f"CPU Usage: {self.cpu_usage}/{self.cpu_capacity}, "
                f"Memory Usage: {self.memory_usage}/{self.memory_capacity}, "
                f"Network Latency: {self.network_latency}")

# Clase que gestiona el grupo de servidores
class AutoScalingGroup:
    def __init__(self, template, min_size, max_size, scaling_policy):
        self.template = template
        self.min_size = min_size
        self.max_size = max_size
        self.scaling_policy = scaling_policy
        self.servers = [self.template.create_server() for _ in range(min_size)]
        self.log = []

    def scale_out(self):
        if len(self.servers) < self.max_size:
            self.servers.append(self.template.create_server())
            self.log.append("Escalado hacia afuera: Añadido un servidor")
            print("Escalado hacia afuera: Añadido un servidor")

    def scale_in(self):
        if len(self.servers) > self.min_size:
            self.servers.pop()
            self.log.append("Escalado hacia adentro: Eliminado un servidor")
            print("Escalado hacia adentro: Eliminado un servidor")

    def adjust_capacity(self, metrics):
        if self.scaling_policy(metrics):
            self.scale_out()
        else:
            self.scale_in()

    def simulate_load(self, cpu_load, memory_load, network_latency):
        for server in self.servers:
            server.handle_request(cpu_load, memory_load, network_latency)
        self.log.append(f"Simulación de carga: CPU {cpu_load}, Memoria {memory_load}, Latencia {network_latency}")
        print(f"Simulación de carga: CPU {cpu_load}, Memoria {memory_load}, Latencia {network_latency}")

    def reset_servers(self):
        for server in self.servers:
            server.reset_usage()

    def log_status(self):
        for i, server in enumerate(self.servers, start=1):
            self.log.append(f"Estado del servidor {i}: {server}")
            print(f"Estado del servidor {i}: {server}")

    def print_log(self):
        for entry in self.log:
            print(entry)

# Políticas de escalado personalizadas
def custom_scaling_policy(metrics):
    cpu_avg = sum(metrics['cpu']) / len(metrics['cpu'])
    memory_avg = sum(metrics['memory']) / len(metrics['memory'])
    network_avg = sum(metrics['network']) / len(metrics['network'])
    
    # Condiciones para escalar hacia afuera
    if cpu_avg > 70 or memory_avg > 70 or network_avg > 100:
        return True
    # Condiciones para escalar hacia adentro
    elif cpu_avg < 50 and memory_avg < 50 and network_avg < 50:
        return False
    # Mantener la capacidad actual
    return None

# Simulador de carga
def simulador_de_carga(asg):
    for _ in range(10):  # 10 iteraciones de simulación
        cpu_load = random.randint(0, 100)
        memory_load = random.randint(0, 100)
        network_latency = random.randint(0, 200)
        
        asg.simulate_load(cpu_load, memory_load, network_latency)

        metrics = {
            'cpu': [server.cpu_usage for server in asg.servers],
            'memory': [server.memory_usage for server in asg.servers],
            'network': [server.network_latency for server in asg.servers]
        }

        asg.adjust_capacity(metrics)
        asg.log_status()
        asg.reset_servers()
        time.sleep(1)  # Pausa para simular el paso del tiempo

# Configuración del entorno
template = ServerTemplate(cpu_capacity=100, memory_capacity=100)
asg = AutoScalingGroup(template=template, min_size=2, max_size=5, scaling_policy=custom_scaling_policy)

# Ejecutar la simulación
simulador_de_carga(asg)
asg.print_log()

