'''
Ejercicio 5: Diseño de soluciones de alta disponibildiad Multi-Region

Diseñar una arquitectura de alta disponibilidad milti-region
'''

# Clase que representa un servidor
class Server:
    def __init__(self, name):
        """
        Inicializa un servidor con un nombre.
        
        :param name: Nombre del servidor.
        """
        self.name = name

# Clase que simula un balanceador de carga
class LoadBalancer:
    def __init__(self):
        """
        Inicializa un balanceador de carga con una lista vacía de servidores.
        """
        self.servers = []

    def add_server(self, server):
        """
        Añade un servidor al balanceador de carga.
        
        :param server: Instancia del servidor a añadir.
        """
        self.servers.append(server)

    def distribute_http_requests(self, requests):
        """
        Distribuye solicitudes HTTP entre los servidores disponibles.
        
        :param requests: Lista de solicitudes HTTP a distribuir.
        """
        if not self.servers:
            raise Exception("No servers available to handle the requests.")
        for request in requests:
            # Simulamos la distribución de solicitudes a los servidores de manera round-robin
            server = self.servers[0]  # Tomamos el primer servidor
            print(f"Request '{request}' handled by {server.name}")
            self.servers = self.servers[1:] + [server]  # Movemos el servidor al final de la lista

# Clase que representa una región con servidores y un balanceador de carga
class Region:
    def __init__(self, name):
        """
        Inicializa una región con un nombre, una lista vacía de servidores y un balanceador de carga.
        
        :param name: Nombre de la región.
        """
        self.name = name
        self.servers = []
        self.load_balancer = LoadBalancer()

    def add_server(self, server):
        """
        Añade un servidor a la región y al balanceador de carga.
        
        :param server: Instancia del servidor a añadir.
        """
        self.servers.append(server)
        self.load_balancer.add_server(server)

    def handle_request(self, request):
        """
        Maneja una solicitud HTTP distribuyéndola entre los servidores de la región.
        
        :param request: Solicitud HTTP a manejar.
        """
        self.load_balancer.distribute_http_requests([request])

# Clase que gestiona un sistema de alta disponibilidad multi-región
class MultiRegionHA:
    def __init__(self):
        """
        Inicializa un sistema de alta disponibilidad multi-región con una lista vacía de regiones.
        """
        self.regions = []

    def add_region(self, region):
        """
        Añade una región al sistema de alta disponibilidad.
        
        :region: Instancia de la región a añadir.
        """
        self.regions.append(region)

    def replicate_data(self):
        """
        Simula la replicación de datos entre todas las regiones.
        """
        print("Replicating data between regions...")
        for region in self.regions:
            print(f"Data replicated to region: {region.name}")

    def route_request(self, request):
        """
        Simula el enrutamiento de solicitudes entre regiones, incluyendo la conmutación por error.
        
        :request: Solicitud HTTP a enrutarse.
        """
        if not self.regions:
            raise Exception("No regions available to handle the request.")
        
        # Intentamos manejar la solicitud con la primera región disponible
        for region in self.regions:
            try:
                region.handle_request(request)
                return
            except Exception as e:
                print(f"Region {region.name} failed: {e}")
        
        # Si todas las regiones fallan
        print("All regions failed to handle the request.")

# Ejemplo de uso de las clases
region1 = Region("us-east-1")  # Creamos una región us-east-1
region2 = Region("us-west-1")  # Creamos una región us-west-1
server1 = Server("Server 1")  # Creamos un servidor llamado "Server 1"
server2 = Server("Server 2")  # Creamos un servidor llamado "Server 2"

# Añadimos los servidores a sus respectivas regiones
region1.add_server(server1)
region2.add_server(server2)

# Creamos un sistema de alta disponibilidad multi-región
ha_system = MultiRegionHA()

# Añadimos las regiones al sistema de alta disponibilidad
ha_system.add_region(region1)
ha_system.add_region(region2)

# Simulamos la replicación de datos entre regiones
ha_system.replicate_data()

# Enrutamos una solicitud HTTP a las regiones
ha_system.route_request("Request 1")
