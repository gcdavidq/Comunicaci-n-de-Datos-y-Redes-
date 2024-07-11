'''
Ejercicio 7: Implementacion de un Servicio de DNS Dinamico

Implementa un servicio de DNS dinámico en Python que pueda gestionar múltiples
registros, incluyendo registros A, CNAME y MX, y simular resoluciones de nombres de dominio. 
'''

class DNS:
    def __init__(self):
        # Inicializa el diccionario de registros DNS con sub-diccionarios para 'A', 'CNAME', y 'MX'
        self.records = {
            'A': {},
            'CNAME': {},
            'MX': {}
        }

    def add_record(self, record_type, name, value):
        # Añade un nuevo registro al diccionario correspondiente
        if record_type in self.records:
            self.records[record_type][name] = value
        else:
            # Imprime un mensaje si el tipo de registro no es soportado
            print(f"Record type {record_type} not supported")

    def delete_record(self, record_type, name):
        # Elimina un registro del diccionario correspondiente si existe
        if record_type in self.records and name in self.records[record_type]:
            del self.records[record_type][name]
        else:
            # Imprime un mensaje si el registro no se encuentra
            print(f"Record {name} not found in {record_type} records")

    def update_record(self, record_type, name, value):
        # Actualiza un registro existente con un nuevo valor
        if record_type in self.records and name in self.records[record_type]:
            self.records[record_type][name] = value
        else:
            # Imprime un mensaje si el registro no se encuentra
            print(f"Record {name} not found in {record_type} records")

    def resolve(self, name):
        # Resuelve un nombre DNS a su dirección IP o valor correspondiente
        if name in self.records['A']:
            return self.records['A'][name]
        elif name in self.records['CNAME']:
            # Sigue la cadena de CNAMEs hasta encontrar un registro 'A'
            cname = self.records['CNAME'][name]
            return self.resolve(cname)
        elif name in self.records['MX']:
            return self.records['MX'][name]
        else:
            # Devuelve None si no se encuentra el nombre
            return None

    def __str__(self):
        # Convierte el diccionario de registros en una cadena para su visualización
        return str(self.records)

# Simulación de la CLI
def main():
    # Crea una instancia de la clase DNS
    dns = DNS()
    while True:
        # Solicita al usuario un comando
        command = input("Enter command (add, delete, update, resolve, exit): ")
        if command == 'add':
            # Solicita detalles del registro a añadir
            record_type = input("Enter record type (A, CNAME, MX): ")
            name = input("Enter name: ")
            value = input("Enter value: ")
            dns.add_record(record_type, name, value)
        elif command == 'delete':
            # Solicita detalles del registro a eliminar
            record_type = input("Enter record type (A, CNAME, MX): ")
            name = input("Enter name: ")
            dns.delete_record(record_type, name)
        elif command == 'update':
            # Solicita detalles del registro a actualizar
            record_type = input("Enter record type (A, CNAME, MX): ")
            name = input("Enter name: ")
            value = input("Enter new value: ")
            dns.update_record(record_type, name, value)
        elif command == 'resolve':
            # Solicita el nombre a resolver y muestra el resultado
            name = input("Enter name to resolve: ")
            ip = dns.resolve(name)
            if ip:
                print(f"IP for {name} is {ip}")
            else:
                print(f"{name} not found")
        elif command == 'exit':
            # Sale del bucle y termina el programa
            break
        else:
            # Maneja comandos inválidos
            print("Invalid command")

if __name__ == "__main__":
    # Llama a la función main para iniciar el programa
    main()
