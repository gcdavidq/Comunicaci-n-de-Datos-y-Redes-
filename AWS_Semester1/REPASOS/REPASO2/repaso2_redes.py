import networkx as nx
import matplotlib.pyplot as plt
from ipaddress import ip_network, ip_address

class Dispositivo:
    '''
    Creamos la clase dispositivo que representa un dispositivo en la red.
    '''
    def __init__(self, nombre, tipo_dispositivo):
        '''
        Creamos un constructor init que inicializa una instancia de 'Dispositivo'
        con un nombre y un tipo_dispositivo.
        '''
        self.nombre = nombre
        self.tipo_dispositivo = tipo_dispositivo
        # Inicializamos una propiedad 'self.ip_address' con None, lo que significa que el dispositivo no tiene una dirección IP
        # asignada inicialmente.
        self.ip_address = None 

class Router(Dispositivo):
    '''
    La clase Router hereda del 'Dispositivo' y representa un router en la red.
    '''
    def __init__(self, nombre):
        '''
        Mediante este método, llamamos al constructor de la clase base.
        '''
        super().__init__(nombre, 'Router') # Esto quiere decir que Router se inicializa con un nombre dado y se establece su tipo
        # como 'Router'.
        self.tabla_rutas = {} # Inicializamos el atributo de tabla_rutas en donde se almacenarán las rutas de red del router.

    def add_route(self, red, next_hop):
        '''
        Emplearemos este metodo para agrega una entrada a la tabla de enrutamiento del router
        
        Parametro red: especifica la red de destino en formato CIDR
        Parametro next_hop Especifica la direccion IP del siguiente salgo (o router)
        que debe tomar el paguete para llegar a la red de destino
        '''
        self.tabla_rutas[red] = next_hop #creamos un diccionario donde la clave es la red de destino 
        # y el valor es el next_hop correspondiente
    
    def get_route(self, ip):
        '''
        Empleamos este metodo para encontrar el 'next_hop' para un paquete destinado a una direccion IP 
        especifica

        Parametro ip: se la direccion IP de destino del paquete
        '''
        for red, next_hop in self.tabla_rutas.items():
            if ip in ip_network(red):
                return next_hop
        return None

class Switch(Dispositivo):
    def __init__(self, nombre):
        super().__init__(nombre, 'Switch')

class PC(Dispositivo):
    def __init__(self, nombre):
        super().__init__(nombre, 'PC')

class Redes:
    def __init__(self):
        self.dispositivos = []
        self.bordes = []
    
    def agregar_dispositivo(self, dispositivo):
        self.dispositivos.append(dispositivo)
    
    def connect(self, dispositivo1, dispositivo2):
        self.bordes.append((dispositivo1, dispositivo2))
    
    def asignar_direccion_IP(self, cidr):
        red = ip_network(cidr)
        hosts = red.hosts()

        for dispositivo in self.dispositivos:
            if isinstance(dispositivo, PC):
                dispositivo.ip_address = str(next(hosts))
    
    def visualizar(self):
        G = nx.Graph()
        for dispositivo in self.dispositivos:
            G.add_node(dispositivo.nombre)
        
        for borde in self.bordes:
            G.add_edge(borde[0].nombre, borde[1].nombre)
        
        nx.draw(G, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_color='black')
        plt.show()
    
    def simular_trafico(self, src, dst):
        path = nx.shortest_path(self._build_graph(), source=src.nombre, target=dst.nombre)
        print(f"Path de {src.nombre} para {dst.nombre}: {' -> '.join(path)}")
    
    def _build_graph(self):
        G = nx.Graph()
        for dispositivo in self.dispositivos:
            G.add_node(dispositivo.nombre)
        
        for borde in self.bordes:
            G.add_edge(borde[0].nombre, borde[1].nombre)
        
        return G

# USO
network=Redes()

router1=Router("Router1")
router2=Router("Router2")
switch1=Switch("Switch1")
switch2=Switch("Switch2")
pc1=PC("PC1")
pc2=PC("PC2")
pc3=PC("PC3")
pc4=PC("PC4")

#Añadir dispositivos a la red
network.agregar_dispositivo(router1)
network.agregar_dispositivo(router2)
network.agregar_dispositivo(switch1)
network.agregar_dispositivo(switch2)
network.agregar_dispositivo(pc1)
network.agregar_dispositivo(pc2)
network.agregar_dispositivo(pc3)
network.agregar_dispositivo(pc4)


#Conectar dispositivos
network.connect(router1, switch1)
network.connect(router1, switch2)
network.connect(switch1, pc1)
network.connect(switch1, pc2)
network.connect(switch2, pc3)
network.connect(switch2, pc4)
network.connect(router1, router2)

#Asignar direcciones IP
network.asignar_direccion_IP('192.168.1.0/24')


#añadir rutas estáticas
router1.add_route('192.168.1.0/24', 'Router1')
router1.add_route('192.168.2.0/24', 'Router2')
router2.add_route('192.168.1.0/24', 'Router1')
router2.add_route('192.168.2.0/24', 'Router2')

#Visualizar la red
network.visualizar()

#Simular trafico
network.simular_trafico(pc1, pc3)


