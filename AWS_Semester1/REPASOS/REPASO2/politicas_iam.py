# Ejercicio 3:  Crea una política personalizada que otorgue permisos específicos a un bucket de S3.
#signa esta política a un usuario o grupo y verifica que los permisos funcionen
#correctamente. 
class IAM_Servicio:
  def __init__(self):
    self.usuarios={}
    self.grupos={}
    self.politicas={}
iam_servicio=IAM_Servicio()

class Consola:
  #funcion para crear usuarios:
  def crear_usuario(self, iam_servicio, nombre_usuario):
    iam_servicio.usuarios[nombre_usuario]={'politicas':[]}
    print(f"Se creó el usario {nombre_usuario}")

  #función para crear grupos:
  def crear_grupo(self, iam_servicio, nombre_grupo):
    iam_servicio.grupos[nombre_grupo]={'usuarios':[], 'politicas':[]}
    print(f"Se creó el grupo {nombre_grupo}")

  #función para crear politicas, tomando en cuenta su nombre, los permisos y los buckets
  def crear_politicas(self, iam_servicio, nombre_politica, permisos, buckets):
    iam_servicio.politicas[nombre_politica]={'permisos':permisos, 'buckets':buckets}
    print(f"Se creó la politica {nombre_politica}, la cual tiene los permisos de {permisos} en el bucket {buckets}")

  #funcion para agregar usuarios a los grupos
  def asignar_usuario_grupo(self, iam_servicio, nombre_grupo, nombre_usuario):
    if nombre_usuario in iam_servicio.usuarios and nombre_grupo in iam_servicio.grupos:
      iam_servicio.grupos[nombre_grupo]['usuarios'].append(nombre_usuario)
      #crearemos un bucle for para recorrer las politicas dentro del grupo
      for politica in iam_servicio.grupos[nombre_grupo]['politicas']:
        #si la politica no está dentro de las politicas del usuario, la agregamos
        if politica not in iam_servicio.usuarios[nombre_usuario]['politicas']:
          iam_servicio.usuarios[nombre_usuario]['politicas'].append(politica)
      print(f"Se heredaron las politicas del grupo {nombre_grupo} al usuario {nombre_usuario}")

  #funcion para agregar politicas a usuarios
  def asignar_politicas_usuario(self, iam_servicio, nombre_usuario, nombre_politica):
    if nombre_usuario in iam_servicio.usuarios:
      iam_servicio.usuarios[nombre_usuario]['politicas'].append(nombre_politica)
      print(f"Se asignó la politica {nombre_politica} al usuario {nombre_usuario}")

  #funcion par agregar politicas a grupos
  def asignar_politicas_grupos(self, iam_servicio, nombre_grupo, nombre_politica):
    if nombre_grupo in iam_servicio.grupos:
      iam_servicio.grupos[nombre_grupo]['politicas'].append(nombre_politica)
      print(f"Se agregó la politica {nombre_politica} al grupo {nombre_grupo}")

iam_consola=Consola()

print("CREAMOS LOS USUARIOS Y GRUPOS CORRESPONDIENTES")
iam_consola.crear_usuario(iam_servicio, 'Gian Carlos')
iam_consola.crear_usuario(iam_servicio, 'Michael Gavino')
iam_consola.crear_usuario(iam_servicio, 'Magno Luque')
iam_consola.crear_usuario(iam_servicio, 'Edithson Cavani')
iam_consola.crear_usuario(iam_servicio, 'Alexander Peralta')
iam_consola.crear_grupo(iam_servicio, 'Admins')
iam_consola.crear_grupo(iam_servicio, 'DevOps')

print("CREAMOS LAS POLITICAS PARA LOS GRUPOS Y USUARIOS")
iam_consola.crear_politicas(iam_servicio, 'Politic_Admins', ['leer', 'editar', 'eliminar'], 'Bucket_Admins')
iam_consola.crear_politicas(iam_servicio, 'Politic_DevOps', ['leer','editar'], 'Bucket_DevOps')
iam_consola.crear_politicas(iam_servicio, 'Politic_Extern', ['leer'], 'Bucket_Extern')

print("ASIGNAR POLITICAS A GRUPOS")
iam_consola.asignar_politicas_grupos(iam_servicio, 'DevOps', 'Politic_DevOps')
iam_consola.asignar_politicas_grupos(iam_servicio, 'Admins', 'Politic_Admins')

print("ASIGNAR POLITICAS A USUARIOS")
iam_consola.asignar_politicas_usuario(iam_servicio, 'Edithson Cavani', 'Politic_Extern')

print("ASIGNAR LOS USUARIOS A LOS GRUPOS")
iam_consola.asignar_usuario_grupo(iam_servicio, 'Admins', 'Gian Carlos')
iam_consola.asignar_usuario_grupo(iam_servicio, 'Admins', 'Magno Luque')
iam_consola.asignar_usuario_grupo(iam_servicio, 'DevOps', 'Michael Gavino')
iam_consola.asignar_usuario_grupo(iam_servicio, 'DevOps', 'Alexander Peralta')

#clase para crear y asignar politicas a buckets y objetos
class S3:
  def __init__ (self):
    self.buckets={}
    self.objetos={}

  def crear_objetos(self, nombre_objeto):
    self.objetos[nombre_objeto]={'objeto':[]}
    print(f"Se creó el objeto {nombre_objeto}")

  #funcion para crear buckets:
  def crear_bucket(self, nombre_bucket):
    self.buckets[nombre_bucket]={'objetos':[], 'permisos':[]}
    print(f"Se creó el bucket {nombre_bucket}")

  #funcion para asignar objetos a buckets:
  def objetos_buckets(self, nombre_bucket, nombre_objeto):
    if nombre_objeto in self.objetos and nombre_objeto in self.objetos:
      self.buckets[nombre_bucket]['objetos'].append(nombre_objeto)
      print(f"Se agregó el objeto {nombre_objeto} al bucket {nombre_bucket}")

  #funcion para simular el permiso de lectura a un bucket:
  def leer_buckets(self, nombre_bucket, nombre_usuario, iam_servicio):
    if nombre_bucket in self.buckets:
      #creamos una variable para leer las politicas de los usuarios
      politicas_servicio=iam_servicio.usuarios[nombre_usuario]['politicas']
      for politica in politicas_servicio:
        permiso=iam_servicio.politicas[politica]['permisos']
        buckets=iam_servicio.politicas[politica]['buckets']
        if 'leer' in permiso and nombre_bucket in buckets:
          print(f"El usuario {nombre_usuario} tiene permiso para leer el bucket {nombre_bucket}")
          return list(self.buckets[nombre_bucket]['objetos'])
      print(f"El usuario  {nombre_usuario} no tienene permiso de leer el bucket {nombre_bucket}")
    print(f"No existe el bucket {nombre_bucket}")

    #funcion para simular el permiso de edicion a un bucket:
  def editar_bucket(self, nombre_bucket, nombre_usuario, iam_servicio, nombre_objeto, nuevo_nombre_objeto):
        if nombre_bucket in self.buckets:
          #creamos una variable para leer las politicas de los usuarios
          politicas_servicio=iam_servicio.usuarios[nombre_usuario]['politicas']
          for politica in politicas_servicio:
            permiso=iam_servicio.politicas[politica]['permisos']
            buckets=iam_servicio.politicas[politica]['buckets']
            if 'editar' in permiso and nombre_bucket in buckets:
              #buscamos el index del objeto que queremos editar dentro del bucket
              index=self.buckets[nombre_bucket]['objetos'].index(nombre_objeto)
              self.buckets[nombre_bucket]['objetos'][index]=nuevo_nombre_objeto
              print(f"Se actualizó el nombre del objeto {nombre_objeto} a {nuevo_nombre_objeto} en el bucket {nombre_bucket}")
  
  def eliminar_bucket(self, nombre_bucket, nombre_usuario, iam_servicio, nombre_objeto):
        if nombre_bucket in self.buckets:
          #creamos una variable para leer las politicas de los usuarios
          politicas_servicio=iam_servicio.usuarios[nombre_usuario]['politicas']
          for politica in politicas_servicio:
            permiso=iam_servicio.politicas[politica]['permisos']
            buckets=iam_servicio.politicas[politica]['buckets']
            if 'eliminar' in permiso and nombre_bucket in buckets:
              print(self.buckets[nombre_bucket]['objetos'])
              print(nombre_objeto)
              self.buckets[nombre_bucket]['objetos'].remove(nombre_objeto)
              print(f"Se eliminó el objeto {nombre_objeto} del bucket {nombre_bucket}")


              

s3 = S3()
print("CREAMOS OBJETOS Y BUCKETS")
s3.crear_objetos("videos_programing")
s3.crear_objetos("Images_programing")
s3.crear_bucket("Bucket_developer")
s3.crear_objetos("Docs_admins")
s3.crear_bucket("Bucket_Admins")
s3.objetos_buckets("Bucket_developer", "videos_programing")
s3.objetos_buckets("Bucket_Admins", "Docs_admins")


# Verificamos permisos
objetos_bucket_admins = s3.leer_buckets('Bucket_Admins', 'Gian Carlos', iam_servicio)
if objetos_bucket_admins:
    print(f"Objetos en el bucket 'Bucket_Admins': {objetos_bucket_admins}")

s3.editar_bucket('Bucket_Admins', 'Gian Carlos', iam_servicio, 'Docs_admins', 'Documentos de administrador' )
s3.eliminar_bucket('Bucket_Admins', 'Gian Carlos', iam_servicio, 'Documentos de administrador' )








        





# Ejercicio 4: Implementación de Roles IAM para credenciales temporales

# Tarea: Configura un rol IAM que permita a una instancia EC2 acceder a un bucket de S3.
# Documenta el proceso y prueba el acceso desde la instancia.

    


