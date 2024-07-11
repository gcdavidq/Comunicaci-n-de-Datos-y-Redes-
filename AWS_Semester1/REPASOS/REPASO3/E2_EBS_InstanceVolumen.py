class EBSVolume:
    def __init__(self, volume_id, size):
        self.volume_id = volume_id
        self.size = size
        self.data = ""
        self.attached_instance = None

    def attach_to_instance(self, instance_id):
        if self.attached_instance is None:
            self.attached_instance = instance_id
            print(f"Volumen EBS {self.volume_id} adjuntado a la instancia {instance_id}.")
        else:
            print(f"Volumen EBS {self.volume_id} ya está adjuntado a la instancia {self.attached_instance}.")

    def detach_from_instance(self):
        if self.attached_instance is not None:
            print(f"Volumen EBS {self.volume_id} desadjuntado de la instancia {self.attached_instance}.")
            self.attached_instance = None
        else:
            print(f"Volumen EBS {self.volume_id} no está adjuntado a ninguna instancia.")

class InstanceStoreVolume:
    def __init__(self, volume_id, size):
        self.volume_id = volume_id
        self.size = size
        self.data = ""
        self.attached_instance = None

    def attach_to_instance(self, instance_id):
        if self.attached_instance is None:
            self.attached_instance = instance_id
            print(f"Volumen de almacenamiento de instancia {self.volume_id} adjuntado a la instancia {instance_id}.")
        else:
            print(f"Volumen de almacenamiento de instancia {self.volume_id} ya está adjuntado a la instancia {self.attached_instance}.")

    def detach_from_instance(self):
        if self.attached_instance is not None:
            print(f"Volumen de almacenamiento de instancia {self.volume_id} desadjuntado de la instancia {self.attached_instance}.")
            self.attached_instance = None
        else:
            print(f"Volumen de almacenamiento de instancia {self.volume_id} no está adjuntado a ninguna instancia.")

class EC2:
    def __init__(self):
        self.instances = {}
        self.ebs_volumes = {}
        self.instance_store_volumes = {}

    def create_instance(self, instance_id):
        self.instances[instance_id] = {'ebs_volumes': [], 'instance_store_volumes': []}
        print(f"Se creó la instancia {instance_id}.")

    def create_ebs_volume(self, volume_id, size):
        if volume_id not in self.ebs_volumes:
            self.ebs_volumes[volume_id] = EBSVolume(volume_id, size)
            print(f"Se creó el volumen EBS {volume_id} con tamaño {size}GB.")
        else:
            print(f"El volumen EBS {volume_id} ya existe.")

    def create_instance_store_volume(self, volume_id, size):
        if volume_id not in self.instance_store_volumes:
            self.instance_store_volumes[volume_id] = InstanceStoreVolume(volume_id, size)
            print(f"Se creó el volumen de almacenamiento de instancia {volume_id} con tamaño {size}GB.")
        else:
            print(f"El volumen de almacenamiento de instancia {volume_id} ya existe.")

    def attach_ebs_volume(self, volume_id, instance_id):
        if volume_id in self.ebs_volumes and instance_id in self.instances:
            volume = self.ebs_volumes[volume_id]
            if volume.attached_instance is None:
                volume.attach_to_instance(instance_id)
                self.instances[instance_id]['ebs_volumes'].append(volume_id)
            elif volume.attached_instance == instance_id:
                print(f"El volumen EBS {volume_id} ya está adjuntado a la instancia {instance_id}.")
            else:
                print(f"El volumen EBS {volume_id} ya está adjuntado a otra instancia {volume.attached_instance}.")
        else:
            print(f"No se puede adjuntar el volumen EBS {volume_id} a la instancia {instance_id} porque no existe uno de ellos.")

    def detach_ebs_volume(self, volume_id):
        if volume_id in self.ebs_volumes:
            instance_id = self.ebs_volumes[volume_id].attached_instance
            self.ebs_volumes[volume_id].detach_from_instance()
            if instance_id:
                self.instances[instance_id]['ebs_volumes'].remove(volume_id)
        else:
            print(f"El volumen EBS {volume_id} no existe.")

    def attach_instance_store_volume(self, volume_id, instance_id):
        if volume_id in self.instance_store_volumes and instance_id in self.instances:
            volume = self.instance_store_volumes[volume_id]
            if volume.attached_instance is None:
                volume.attach_to_instance(instance_id)
                self.instances[instance_id]['instance_store_volumes'].append(volume_id)
            elif volume.attached_instance == instance_id:
                print(f"El volumen de almacenamiento de instancia {volume_id} ya está adjuntado a la instancia {instance_id}.")
            else:
                print(f"El volumen de almacenamiento de instancia {volume_id} ya está adjuntado a otra instancia {volume.attached_instance}.")
        else:
            print(f"No se puede adjuntar el volumen de almacenamiento de instancia {volume_id} a la instancia {instance_id} porque no existe uno de ellos.")

    def detach_instance_store_volume(self, volume_id):
        if volume_id in self.instance_store_volumes:
            instance_id = self.instance_store_volumes[volume_id].attached_instance
            self.instance_store_volumes[volume_id].detach_from_instance()
            if instance_id:
                self.instances[instance_id]['instance_store_volumes'].remove(volume_id)
        else:
            print(f"El volumen de almacenamiento de instancia {volume_id} no existe.")

    def simulate_failure(self, volume_id):
        if volume_id in self.ebs_volumes:
            print(f"Simulando fallo en el volumen EBS {volume_id}.")
            self.ebs_volumes[volume_id].data = "DATO PERDIDO"
        elif volume_id in self.instance_store_volumes:
            print(f"Simulando fallo en el volumen de almacenamiento de instancia {volume_id}.")
            self.instance_store_volumes[volume_id].data = "DATO PERDIDO"
        else:
            print(f"El volumen {volume_id} no existe.")

    def show_state(self):
        print("Estado actual de instancias y volúmenes:")
        for instance_id, details in self.instances.items():
            print(f"Instancia {instance_id}:")
            print(f"  Volúmenes EBS: {details['ebs_volumes']}")
            print(f"  Volúmenes de almacenamiento de instancia: {details['instance_store_volumes']}")

# Crear una instancia de EC2
ec2 = EC2()

# Crear una instancia EC2
ec2.create_instance('InstanciaPrincipal')

# Crear volúmenes EBS y de almacenamiento de instancia
ec2.create_ebs_volume('EBS1', 50)
ec2.create_instance_store_volume('IS1', 20)

# Adjuntar volúmenes a la instancia
ec2.attach_ebs_volume('EBS1', 'InstanciaPrincipal')
ec2.attach_instance_store_volume('IS1', 'InstanciaPrincipal')

# Mostrar el estado actual
ec2.show_state()

# Simular un fallo en un volumen EBS
ec2.simulate_failure('EBS1')

# Mostrar el estado después del fallo
ec2.show_state()
