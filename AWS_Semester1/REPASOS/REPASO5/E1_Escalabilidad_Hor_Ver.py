"""
Ejercicio 1: Simulacion de escalabilidad vertical y horizontal

Entender las diferencias entre escalabilidad horizontal y vertical
"""
class Server:
    
    def __init__(self, cpu_capacidad, memoria_capacidad):
        self.cpu_capacidad=cpu_capacidad
        self.memoria_capacidad=memoria_capacidad
        self.current_load=0

    def scale_up(self,adicional_cpu, adiccional_memoria):
        self.cpu_capacidad+=adicional_cpu
        self.memoria_capacidad+=adiccional_memoria

class ServerCluster:
    "En esta clase simularemos la creacion de servidores, solo tomando en cuenta su capacidad de CPU y Memoria"
    def __init__(self):
        self.servers=[]
    
    def add_server(self, server):
        self.servers.append(server)
        print(f"Se agrego el servidor {server}")
    
    def remover_servidor(self, server):
        if server in self.servers:
            self.servers.pop(server)
    
    def distribuir_carga(self, carga):
        if not self.servers:
            print("No existen servidores")
            return
        carga_parcial_servidor=carga/len(self.servers)
        for server in self.servers:
            server.current_load=carga_parcial_servidor
            print(f"Carga parcial del servidor: {server} :\n {server.current_load}")
    

#USO
server1=Server(cpu_capacidad=4, memoria_capacidad=8)
server2=Server(cpu_capacidad=4, memoria_capacidad=8)
cluster=ServerCluster()
cluster.add_server(server1)
cluster.add_server(server2)
cluster.distribuir_carga(10)