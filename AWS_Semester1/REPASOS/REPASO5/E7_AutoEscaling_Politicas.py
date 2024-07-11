'''
Ejercicio 7: Simulacion de Auto Scaling con politicas de escalado personalizadas

Configurar un sistema de Auto Scaling con politicas de escalado personalizadas

'''
# Clase que simula un grupo de Auto Scaling con políticas de escalado personalizadas
class CustomAutoScalingGroup:
    def __init__(self, template, min_size, max_size, scaling_policy):
        """
        Inicializa un grupo de Auto Scaling.
        
        :param template: Plantilla de configuración del servidor.
        :param min_size: Número mínimo de servidores en el grupo.
        :param max_size: Número máximo de servidores en el grupo.
        :param scaling_policy: Función que define la política de escalado.
        """
        self.template = template  # Plantilla utilizada para crear nuevos servidores.
        self.min_size = min_size  # Tamaño mínimo del grupo de servidores.
        self.max_size = max_size  # Tamaño máximo del grupo de servidores.
        self.scaling_policy = scaling_policy  # Política de escalado personalizada.
        self.servers = [self.template.create_server() for _ in range(min_size)]  # Lista inicial de servidores creados según el tamaño mínimo.

    def escalar_hacia_fuera(self):
        """
        Agrega un servidor al grupo si no se ha alcanzado el tamaño máximo.
        """
        if len(self.servers) < self.max_size:
            self.servers.append(self.template.create_server())  # Crea y añade un nuevo servidor al grupo.
            print("Escalado hacia afuera: Se añadió un servidor")

    def escalar_hacia_adentro(self):
        """
        Remueve un servidor del grupo si no se ha alcanzado el tamaño mínimo.
        """
        if len(self.servers) > self.min_size:
            self.servers.pop()  # Elimina el último servidor de la lista.
            print("Escalado hacia adentro: Se eliminó un servidor")

    def ajustar_capacidad(self, valores_metricas):
        """
        Ajusta la capacidad del grupo de servidores basado en las métricas proporcionadas.
        
        :param valores_metricas: Lista de valores de métricas a considerar para el escalado.
        """
        if self.scaling_policy(valores_metricas):
            self.escalar_hacia_fuera()  # Escala hacia afuera si la política de escalado lo indica.
        else:
            self.escalar_hacia_adentro()  # Escala hacia adentro si la política de escalado lo indica.

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

# Función que define una política de escalado personalizada
def politica_escalado_personalizada(valores_metricas):
    """
    Ejemplo de política de escalado personalizada.
    
    :param valores_metricas: Lista de valores de métricas a considerar para el escalado.
    :return: True si se debe escalar hacia afuera, False si se debe escalar hacia adentro.
    """
    return sum(valores_metricas) / len(valores_metricas) > 70  # Escala hacia afuera si el promedio de las métricas supera 70.

# Ejemplo de uso de las clases
plantilla = ServerTemplate()  # Crea una plantilla de servidor.
asg = CustomAutoScalingGroup(template=plantilla, min_size=2, max_size=5, scaling_policy=politica_escalado_personalizada)  # Crea un grupo de Auto Scaling con 2 servidores mínimos y 5 máximos, y una política de escalado personalizada.

# Ajusta la capacidad basado en una lista de valores de métricas (por ejemplo, uso de CPU)
asg.ajustar_capacidad([50, 60, 80])  # Ajusta la capacidad del grupo según las métricas proporcionadas.
