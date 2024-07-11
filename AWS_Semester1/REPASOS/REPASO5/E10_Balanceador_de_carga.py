'''
Ejercicio10: Simulacion de balanceadores de carga con politicas de distribucion avanzadas

tar un sistema de balanceo de carga avanzado que soporte múltiples tipos de
balanceadores (ALB, NLB, CLB) y políticas de distribución personalizadas.
'''
import random
import hashlib

# Clase base LoadBalancer
class LoadBalancer:
    def __init__(self):
        self.servers = []  # Lista de servidores gestionados por el balanceador
        self.policy = None  # Política de distribución de carga
        self.request_count = 0  # Contador de solicitudes

    def add_server(self, server):
        self.servers.append(server)  # Añade un servidor a la lista
        print(f"Servidor añadido: {server}")

    def remove_server(self, server):
        self.servers.remove(server)  # Elimina un servidor de la lista
        print(f"Servidor eliminado: {server}")

    def set_policy(self, policy):
        self.policy = policy  # Configura la política de distribución de carga
        print(f"Política configurada: {self.policy.__name__}")

    def distribute_request(self, request):
        if self.policy:
            server = self.policy(self.servers, request)  # Aplica la política de distribución
            self.request_count += 1
            print(f"Solicitud {self.request_count} distribuida a: {server}")
            server.handle_request(request)
        else:
            print("No hay política configurada")

# Clases derivadas
class ApplicationLoadBalancer(LoadBalancer):
    pass  # Puede tener funcionalidades específicas

class NetworkLoadBalancer(LoadBalancer):
    pass  # Puede tener funcionalidades específicas

class ClassicLoadBalancer(LoadBalancer):
    pass  # Puede tener funcionalidades específicas

# Políticas de distribución de carga
def round_robin(servers, request):
    server = servers[round_robin.index % len(servers)]
    round_robin.index += 1
    return server
round_robin.index = 0

def least_connections(servers, request):
    return min(servers, key=lambda server: server.connection_count)

def ip_hash(servers, request):
    ip_hash_value = int(hashlib.md5(request['ip'].encode()).hexdigest(), 16)
    server_index = ip_hash_value % len(servers)
    return servers[server_index]

# Clase Server
class Server:
    def __init__(self, name):
        self.name = name
        self.connection_count = 0

    def handle_request(self, request):
        self.connection_count += 1  # Incrementa el contador de conexiones
        print(f"Servidor {self.name} manejando solicitud de {request['ip']}")

    def __str__(self):
        return self.name

# Sistema de monitoreo
class MonitoringSystem:
    def __init__(self):
        self.metrics = {}  # Diccionario de métricas por balanceador

    def record_metrics(self, load_balancer):
        self.metrics[load_balancer] = {
            'request_count': load_balancer.request_count,
            'servers': {server.name: server.connection_count for server in load_balancer.servers}
        }

    def print_metrics(self):
        for lb, metrics in self.metrics.items():
            print(f"Balanceador: {lb}")
            print(f"Solicitudes Totales: {metrics['request_count']}")
            for server, connections in metrics['servers'].items():
                print(f"Servidor {server}: {connections} conexiones")

# Script de simulación
def simular_balanceo_de_carga():
    # Crear balanceadores de carga
    alb = ApplicationLoadBalancer()
    nlb = NetworkLoadBalancer()
    clb = ClassicLoadBalancer()

    # Crear servidores
    servidores = [Server(f"Servidor-{i}") for i in range(1, 6)]

    # Añadir servidores a los balanceadores
    for server in servidores:
        alb.add_server(server)
        nlb.add_server(server)
        clb.add_server(server)

    # Configurar políticas de distribución
    alb.set_policy(round_robin)
    nlb.set_policy(least_connections)
    clb.set_policy(ip_hash)

    # Crear sistema de monitoreo
    monitor = MonitoringSystem()

    # Generar tráfico de red simulado
    for i in range(50):
        request = {'ip': f"192.168.0.{random.randint(1, 255)}"}
        alb.distribute_request(request)
        nlb.distribute_request(request)
        clb.distribute_request(request)

    # Registrar métricas
    monitor.record_metrics(alb)
    monitor.record_metrics(nlb)
    monitor.record_metrics(clb)

    # Imprimir métricas
    monitor.print_metrics()

# Ejecutar la simulación
simular_balanceo_de_carga()
