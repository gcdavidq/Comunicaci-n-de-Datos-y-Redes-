'''
En este script simularemos el empleo de los servicios de AWS CloudFront, Route53 y VPC
'''

# Ejercicio 1: Introducción a las Redes On-Premises y Corporativas Básicas:

import networkx as nx  # para trabajar con grafos
import matplotlib.pyplot as plt  # para trabajar con gráficos
from ipaddress import ip_network
import time

# Empezamos con la creación de un grafo vacío
G = nx.Graph()

# Añadimos nodos (dispositivos)
G.add_node("Router")
G.add_node("Switch1")
G.add_node("Switch2")
G.add_node("PC1")
G.add_node("PC2")
G.add_node("PC3")
G.add_node("PC4")

# Añadir enlaces (conexiones)
G.add_edges_from([("Router", "Switch1"),
                  ("Router", "Switch2"),
                  ("Switch1", "PC1"),
                  ("Switch1", "PC2"),
                  ("Switch2", "PC3"),
                  ("Switch2", "PC4")])

# Dibujamos el grafo
#nx.draw(G, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_color="black")
#plt.show()

#Ejercicio2: Redireccionamiento IP y CIDR
#Esciribir un script que calcule y muestre rangos de direcciones IP basados en CIDR

#Definimos un rango CIDR

cidr='192.168.1.0/24'

#creamos una red basada en el CIDR creado

red = ip_network(cidr)

#mostrar todas las direcciones Ip en la red
print(f"Rango de direcciones IP para {cidr}")

for ip in red.hosts():
    print(ip)

#Ejercicio 3: Redes Privadas (VPCs) y subredes
#Simularemos la creacion de VPCs y subredes usando clases en Python para representar estos elementos

class VPC:
    def __init__(self, cidr):
        self.cidr=cidr
        self.subredes=[]
    
    def agregar_subred(self, cidr):
        subred=Subred(cidr)
        self.subredes.append(subred)

class Subred:
    def __init__(self, cidr):
        self.cidr=cidr


#Creamos una VPC
vpc=VPC('10.0.0.0/16')

#Añadir subredes

vpc.agregar_subred('10.0.1.0/24')
vpc.agregar_subred('10.0.2.0/24')


#Mostrar la configuracion de la VPC
print(f"VPC CIDR: {vpc.cidr}")

for subred in vpc.subredes:
    print(f"Subred CIDR: {subred.cidr}")

#Ejercicio4: DNS y enrutamiento con simulación básica en Route53 
#Podemos simlar la resolucion de nombres y el enrutamiento básico mediante diccionarios

#Simulacion de un DNS con registro A y CNAME

dns_records={
    'example.com':'192.168.1.10',
    'www.example.com':'example.com'
}

def resolver_dns(name):
    if name in dns_records:
        value=dns_records[name]

        #Resolver CNAME
        if value in dns_records:
            value=dns_records[value]

        return value 
    
    return None
#Probar la resolucion de DNS
print(f"IP de example.com: {resolver_dns('example.com')}")
print(f"IP de www.example.com: {resolver_dns('www.example.com')}")

#Ejercicio5: Implementacion de una CDN básica en Python
#Simularemos una CDN que almacena en caché el contenido y responde a las solicitudes

class CDN:
    def __init__(self):
        self.cache={}

    def obtener_contenido(self, url):
        if url in self.cache:
            print("Contenido enviado desde cache") 
            return self.cache[url]
        
        else:
            content=self.buscar_desde_origen(url)
            self.cache[url]=content
            return content
    
    def buscar_desde_origen(self, url):
        print("Buscando contenido desde el servidor original...")
        time.sleep(2)
        return f"Contenido de {url}"

#creamos un objeto de CDN
cdn=CDN()

#solicitar contenido

print(cdn.obtener_contenido("https://example.com/imagen"))
print(cdn.obtener_contenido("https://example.com/imagen"))
        
 