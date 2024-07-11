'''
Ejercicio4: Simulacion de elasticidad con autoscaling groups
'''

class AutoScalingGroup:
    def __init__(self, template, min_size, max_size):
        """
        Inicializa un grupo de Auto Scaling.
        
        :param template: Plantilla de configuración del servidor.
        :param min_size: Número mínimo de servidores en el grupo.
        :param max_size: Número máximo de servidores en el grupo.
        """
        self.template = template  # Plantilla utilizada para crear nuevos servidores.
        self.min_size = min_size  # Tamaño mínimo del grupo de servidores.
        self.max_size = max_size  # Tamaño máximo del grupo de servidores.
        self.servers = [self.template.create_server() for _ in range(min_size)]  # Lista inicial de servidores creados según el tamaño mínimo.
        self.cpu_usage_threshold = 70  # Umbral de uso de CPU para escalar.

    def scale_out(self):
        """
        Agrega un servidor al grupo si no se ha alcanzado el tamaño máximo.
        """
        if len(self.servers) < self.max_size:
            self.servers.append(self.template.create_server())  # Crea y añade un nuevo servidor al grupo.
            print("Scaled out: Added a server")

    def scale_in(self):
        """
        Remueve un servidor del grupo si no se ha alcanzado el tamaño mínimo.
        """
        if len(self.servers) > self.min_size:
            self.servers.pop()  # Elimina el último servidor de la lista.
            print("Scaled in: Removed a server")

    def adjust_capacity(self, cpu_usages):
        """
        Ajusta la capacidad del grupo de servidores basado en el uso promedio de CPU.
        
        :param cpu_usages: Lista de porcentajes de uso de CPU de los servidores.
        """
        average_cpu_usage = sum(cpu_usages) / len(cpu_usages)  # Calcula el uso promedio de CPU.
        if average_cpu_usage > self.cpu_usage_threshold:
            self.scale_out()  # Escala hacia afuera si el uso promedio de CPU supera el umbral.
        elif average_cpu_usage < self.cpu_usage_threshold and len(self.servers) > self.min_size:
            self.scale_in()  # Escala hacia adentro si el uso promedio de CPU es inferior al umbral y hay más servidores que el mínimo.

# Clase que representa la plantilla del servidor
class ServerTemplate:
    def create_server(self):
        """
        Crea y retorna una nueva instancia de servidor.
        """
        return Server()  # Retorna una nueva instancia de Server.

# Clase que representa un servidor
class Server:
    pass  # Implementación vacía para la simulación del servidor.

# Ejemplo de uso de las clases
template = ServerTemplate()  # Crea una plantilla de servidor.
asg = AutoScalingGroup(template=template, min_size=2, max_size=5)  # Crea un grupo de Auto Scaling con 2 servidores mínimos y 5 máximos.
asg.adjust_capacity([50, 60, 80])  # Ajusta la capacidad basado en una lista de usos de CPU.
