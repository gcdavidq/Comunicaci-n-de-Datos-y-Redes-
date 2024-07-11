'''
Ejercicio3: Simulador de balanceadores de carga

Simular la distribucion de tráfico web utilizando balanceadores de carga
'''

class BalanceadorCarga:
    def __init__(self):
        self.servidores=[]
    
    def agregar_servidores(self, servidor):
        self.servidores.append(servidor)
    
    def distribuir_http_pedido(self, pedidos):
        print("Distribuyendo pedidos HTTP ...")
        for i, pedidos in enumerate(pedidos):
            servidor=self.servidores[i%len(self.servidores)]
            servidor.manejar_pedido(pedidos)
    
    def distribuir_tcp_pedidos(self, pedidos):
        print("Distribuyendo pedidos TCP")
        for i, pedidos in enumerate(pedidos):
            servidor=self.servidores[i%len(self.servidores)]
            servidor.manejar_pedido(pedidos)

class Servidor:
    def __init__(self, nombre):
        self.nombre=nombre
    
    def manejar_pedido(self, pedidos):
        print(f"Servidor {self.no} menjando el pedido: {pedidos}")

#USO:
servidor1=Servidor("Servidor1")
servidor2=Servidor("Servidor2")
balancear_carga=BalanceadorCarga()

balancear_carga.agregar_servidores(servidor1)
balancear_carga.agregar_servidores(servidor2)

balancear_carga.distribuir_http_pedido(['Pedido1', 'Pedido2', 'Pedido3'])
balancear_carga.distribuir_tcp_pedidos(["TCP Pedido1", "TCP Pedido2"])