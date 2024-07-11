'''
Ejercicio 6: Simulación de un sistema de firewall para aplicaciones Web (WAF)

Implementar un sistema de firewall para aplicaciones web.
'''

# Clase que simula un firewall para aplicaciones web
class WebApplicationFirewall:
    def __init__(self):
        """
        Inicializa un WAF con una lista vacía de reglas.
        """
        self.reglas = []  # Lista para almacenar las reglas de protección

    def agregar_regla(self, regla):
        """
        Agrega una regla de protección al WAF.
        
        :param regla: Función que define una regla de protección.
        """
        self.reglas.append(regla)

    def aplicar_reglas(self, solicitud):
        """
        Aplica las reglas del WAF a una solicitud.
        
        :param solicitud: Diccionario que representa una solicitud HTTP.
        :return: True si la solicitud pasa todas las reglas, False si es bloqueada.
        """
        for regla in self.reglas:
            if not regla(solicitud):
                print(f"Solicitud bloqueada por la regla: {regla.__name__}")
                return False
        return True

# Función para bloquear solicitudes de IPs específicas
def regla_bloquear_ip(solicitud):
    """
    Regla para bloquear solicitudes basadas en IP.
    
    :param solicitud: Diccionario que representa una solicitud HTTP.
    :return: True si la IP no está bloqueada, False si está bloqueada.
    """
    ips_bloqueadas = ["192.168.0.1"]  # Lista de IPs bloqueadas
    return solicitud["ip"] not in ips_bloqueadas

# Función para prevenir ataques de SQL injection
def regla_sql_injection(solicitud):
    """
    Regla para prevenir ataques de SQL injection.
    
    :param solicitud: Diccionario que representa una solicitud HTTP.
    :return: True si la solicitud no contiene palabras clave de SQL, False si contiene.
    """
    palabras_clave = ["select", "drop", "insert", "delete"]  # Palabras clave de SQL
    return not any(palabra in solicitud["query"].lower() for palabra in palabras_clave)

# Función para prevenir ataques de Cross-Site Scripting (XSS)
def regla_xss(solicitud):
    """
    Regla para prevenir ataques de XSS.
    
    :param solicitud: Diccionario que representa una solicitud HTTP.
    :return: True si la solicitud no contiene scripts, False si contiene.
    """
    return "<script>" not in solicitud["content"].lower()

# Clase que representa un balanceador de carga
class LoadBalancer:
    def __init__(self):
        """
        Inicializa un balanceador de carga con una lista vacía de servidores.
        """
        self.servidores = []

    def agregar_servidor(self, servidor):
        """
        Agrega un servidor al balanceador de carga.
        
        :param servidor: Instancia del servidor a añadir.
        """
        self.servidores.append(servidor)

    def distribuir_solicitudes_http(self, solicitudes):
        """
        Distribuye solicitudes HTTP entre los servidores disponibles.
        
        :param solicitudes: Lista de solicitudes HTTP a distribuir.
        """
        if not self.servidores:
            raise Exception("No hay servidores disponibles para manejar las solicitudes.")
        for solicitud in solicitudes:
            # Simulamos la distribución de solicitudes a los servidores de manera round-robin
            servidor = self.servidores[0]  # Tomamos el primer servidor
            print(f"Solicitud '{solicitud}' manejada por {servidor.nombre}")
            self.servidores = self.servidores[1:] + [servidor]  # Movemos el servidor al final de la lista

# Clase que representa un servidor
class Server:
    def __init__(self, nombre):
        """
        Inicializa un servidor con un nombre.
        
        :param nombre: Nombre del servidor.
        """
        self.nombre = nombre

# Ejemplo de uso de las clases
waf = WebApplicationFirewall()  # Creamos una instancia de WAF
# Agregamos reglas al WAF
waf.agregar_regla(regla_bloquear_ip)
waf.agregar_regla(regla_sql_injection)
waf.agregar_regla(regla_xss)

# Creamos instancias de servidores
servidor1 = Server("Servidor 1")
servidor2 = Server("Servidor 2")

# Creamos una instancia de balanceador de carga
balanceador = LoadBalancer()

# Agregamos los servidores al balanceador de carga
balanceador.agregar_servidor(servidor1)
balanceador.agregar_servidor(servidor2)

# Definimos una solicitud de ejemplo
solicitud = {"ip": "192.168.0.2", "query": "SELECT * FROM users", "content": "Hola Mundo"}

# Aplicamos el WAF a la solicitud antes de pasarla a los servidores
if waf.aplicar_reglas(solicitud):
    # Si la solicitud pasa a través del WAF, la distribuimos entre los servidores
    balanceador.distribuir_solicitudes_http([solicitud])
else:
    print("Solicitud bloqueada por el WAF")
