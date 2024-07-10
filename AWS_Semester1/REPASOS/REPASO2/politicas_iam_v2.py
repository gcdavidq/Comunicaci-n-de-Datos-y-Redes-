import json

class IAMServicio:
    def __init__(self):
        self.usuarios = {}
        self.grupos = {}
        self.politicas = {}

iam_servicio = IAMServicio()

class Consola:
    def crear_usuario(self, iam_servicio, nombre_usuario):
        iam_servicio.usuarios[nombre_usuario] = {'politicas': []}
        print(f"Fue creado el usuario {nombre_usuario}")

    def crear_grupo(self, iam_servicio, nombre_grupo):
        iam_servicio.grupos[nombre_grupo] = {'politicas': [], 'usuarios': []}
        print(f"Se creó correctamente el grupo {nombre_grupo}")

    def crear_politica(self, iam_servicio, nombre_politica, politica_json):
        iam_servicio.politicas[nombre_politica] = json.loads(politica_json)
        print(f"Fue creada la política {nombre_politica}")

    def asignar_usuario_a_grupo(self, iam_servicio, nombre_usuario, nombre_grupo):
        if nombre_usuario in iam_servicio.usuarios and nombre_grupo in iam_servicio.grupos:
            iam_servicio.grupos[nombre_grupo]['usuarios'].append(nombre_usuario)
            print(f"Se asignó el usuario {nombre_usuario} al grupo {nombre_grupo}")

    def asignar_politica_a_usuario(self, iam_servicio, nombre_usuario, nombre_politica):
        if nombre_usuario in iam_servicio.usuarios:
            iam_servicio.usuarios[nombre_usuario]['politicas'].append(nombre_politica)
            print(f"Se asignó la política {nombre_politica} al usuario {nombre_usuario}")

    def asignar_politica_a_grupo(self, iam_servicio, nombre_grupo, nombre_politica):
        if nombre_grupo in iam_servicio.grupos:
            iam_servicio.grupos[nombre_grupo]['politicas'].append(nombre_politica)
            print(f"Se asignó la política {nombre_politica} al grupo {nombre_grupo}")

iam_consola = Consola()

class S3:
    def __init__(self):
        self.buckets = {}
        self.objetos = {}

    def crear_objeto(self, nombre_objeto):
        self.objetos[nombre_objeto] = {'permisos': []}
        print(f"Se acaba de crear el objeto {nombre_objeto}")

    def crear_bucket(self, nombre_bucket):
        self.buckets[nombre_bucket] = {'objetos': [], 'permisos': []}
        print(f"Se acaba de crear el bucket: {nombre_bucket}")

    def agregar_objeto_a_bucket(self, nombre_bucket, nombre_objeto):
        if nombre_objeto in self.objetos and nombre_bucket in self.buckets:
            self.buckets[nombre_bucket]['objetos'].append(nombre_objeto)
            print(f"Se agregó el objeto {nombre_objeto} al bucket {nombre_bucket}")

    def leer_bucket(self, nombre_bucket, nombre_usuario, iam_servicio):
        if nombre_bucket in self.buckets:
            politicas_servicio = iam_servicio.usuarios[nombre_usuario]['politicas']
            for politica in politicas_servicio:
                permisos = iam_servicio.politicas[politica]['Statement']
                for permiso in permisos:
                    if permiso['Action'] == 's3:ListBucket' and permiso['Resource'] == nombre_bucket:
                        print(f"El usuario {nombre_usuario} tiene permiso para leer el bucket {nombre_bucket}")
                        return list(self.buckets[nombre_bucket]['objetos'])
            print(f"El usuario {nombre_usuario} no tiene permiso de lectura en el bucket {nombre_bucket}")
        else:
            print(f"No existe el bucket {nombre_bucket}")

    def eliminar_objeto(self, nombre_bucket, nombre_objeto, nombre_usuario, iam_servicio):
        if nombre_bucket in self.buckets and nombre_objeto in self.buckets[nombre_bucket]['objetos']:
            politicas_servicio = iam_servicio.usuarios[nombre_usuario]['politicas']
            for politica in politicas_servicio:
                permisos = iam_servicio.politicas[politica]['Statement']
                for permiso in permisos:
                    if permiso['Action'] == 's3:DeleteObject' and permiso['Resource'] == f"{nombre_bucket}/{nombre_objeto}":
                        self.buckets[nombre_bucket]['objetos'].remove(nombre_objeto)
                        print(f"El objeto {nombre_objeto} ha sido eliminado del bucket {nombre_bucket} por el usuario {nombre_usuario}")
                        return
            print(f"El usuario {nombre_usuario} no tiene permiso para eliminar objetos en el bucket {nombre_bucket}")
        else:
            print(f"No existe el bucket {nombre_bucket} o el objeto {nombre_objeto} no se encuentra en el bucket")

    def editar_bucket(self, nombre_bucket, nombre_usuario, iam_servicio, nombre_objeto, nuevo_nombre_objeto):
        if nombre_bucket in self.buckets:
            politicas_servicio = iam_servicio.usuarios[nombre_usuario]['politicas']
            for politica in politicas_servicio:
                permisos = iam_servicio.politicas[politica]['Statement']
                for permiso in permisos:
                    if permiso['Action'] == 's3:PutObject' and permiso['Resource'] == f"{nombre_bucket}/{nombre_objeto}":
                        try:
                            index = self.buckets[nombre_bucket]['objetos'].index(nombre_objeto)
                            self.buckets[nombre_bucket]['objetos'][index] = nuevo_nombre_objeto
                            print(f"Se actualizó el nombre del objeto {nombre_objeto} a {nuevo_nombre_objeto} en el bucket {nombre_bucket}")
                            return
                        except ValueError:
                            print(f"El objeto {nombre_objeto} no se encuentra en el bucket {nombre_bucket}")
                            return
            print(f"El usuario {nombre_usuario} no tiene permiso para editar objetos en el bucket {nombre_bucket}")
        else:
            print(f"No existe el bucket {nombre_bucket}")

# Ejemplo
iam_consola.crear_usuario(iam_servicio, "Gian Carlos")
iam_consola.crear_grupo(iam_servicio, "Admins")
politica_admin = """
{
    "Version": "2024-06-14",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:PutObject", "s3:DeleteObject"],
            "Resource": ["Bucket_Admins", "Bucket_Admins/*"]
        }
    ]
}
"""
iam_consola.crear_politica(iam_servicio, "Politica_Admin", politica_admin)
iam_consola.asignar_politica_a_usuario(iam_servicio, "Gian Carlos", "Politica_Admin")

s3 = S3()
s3.crear_objeto("Docs_admins")
s3.crear_bucket("Bucket_Admins")
s3.agregar_objeto_a_bucket("Bucket_Admins", "Docs_admins")

objetos_bucket_admins = s3.leer_bucket('Bucket_Admins', 'Gian Carlos', iam_servicio)
if objetos_bucket_admins:
    print(f"Objetos en el bucket 'Bucket_Admins': {objetos_bucket_admins}")

s3.eliminar_objeto('Bucket_Admins', 'Docs_admins', 'Gian Carlos', iam_servicio)

s3.crear_objeto("Docs_admins")
s3.agregar_objeto_a_bucket("Bucket_Admins", "Docs_admins")
s3.editar_bucket('Bucket_Admins', 'Gian Carlos', iam_servicio, 'Docs_admins', 'Docs_actualizados')
