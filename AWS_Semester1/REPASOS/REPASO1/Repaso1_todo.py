'''
En este script, simularemos el servicio de AWS IAM empleando python
'''
import json
class IAM_Service: 
    '''
    Creamos una clase que simule las principales caracteristicas del servicio, como lo son:
    - Usuarios
    - Grupos
    - Politicas
    - Roles
    '''
    def __init__(self): #Inicializamos la clase

        self.usuarios={}
        self.grupos={}
        self.politicas={}
        self.roles={}
    
iam_servicio=IAM_Service() #creamos un objeto de la clase, el cual nos servirá para más adelante.

class IAM_Consola:
    '''
    Esta clase nos permtirá trabajar con el servicio IAM, simulando las principales acciones que se pueden hacer dentro de este.
    '''
    def crear_usuario(self, iam_servicio, nombre_usuario):
        '''
        Con este metodo, creamos usuarios dentro del diccionario 'usuarios'.
        - Entrada: nombre del usuario
        - Salida: agregar un nombre de usuario como clave en el diccionario 'usuarios' 
        '''
        iam_servicio.usuarios[nombre_usuario]={'politicas':[], 'mfa_activo':False}
        print(f"Se creó el usuario {nombre_usuario}")
    
    def crear_grupo(self, iam_servicio, nombre_grupo):
        '''
        Con este metodo, creamos grupos dentro del diccionario 'grupos'.
        - Entrada: Nombre del grupo
        - Salida: Agregar un nombre de grupo como clave en el diccionario 'grupos'
        '''
        iam_servicio.grupos[nombre_grupo]={'usuarios': {}, 'politicas':[]}
        print(f"Se creó el grupo {nombre_grupo}")
    
    def listar_usuarios(self, iam_servicio):
        '''
        Con esta funcion listamos los usuarios existentes.
        '''
        return list(iam_servicio.usuarios.keys()) #se emplea keys para listar por claves
    
    def listar_grupos(self, iam_servicio):
        return list(iam_servicio.grupos.keys())
    
    def agregar_usuario_grupo(self, iam_servicio, nombre_grupo, nombre_usuario):
        '''
        Con este metodo, agregamos un usuario especifo a un grupo especifico.
        - Entrada: nombre de usuario y nombre de grupo.
        - Salida: nueva clave en el diccionario con clave 'usuarios' del diccionario grupos.
        '''
        #primero verificamos que el nombre del grupo exista dentro del diccionario grupos
        if nombre_grupo in iam_servicio.grupos:
            iam_servicio.grupos['usuarios'].append(nombre_usuario) #agregamos un nuevo valor al diccionario 'usuarios'
            print(f"El usuario {nombre_usuario} fue agregado al grupo {nombre_grupo}")
        else:
            print(f"No existe el grupo  {nombre_grupo}")
        
    def asignar_politica_usuario(self, iam_servicio, nombre_usuario, nombre_politica):
        '''
        Con este metodo agregaremos una politica en formato json a un usuario en especifico.
        '''
        if nombre_usuario in iam_servicio.usuarios:
            iam_servicio.usuarios['politicas']=json.loads(nombre_politica) #reemplazamos el valor que existe en 'politicas' por el valor de la nueva politica.
            print(f"Se asignó la politica {nombre_politica} al usuario {nombre_usuario}")
        else:
            print(f"No existe el usuario {nombre_usuario}. Crea este usuario y vuelve a intentarlo")

    def asignar_politica_grupo(self, iam_servicio, nombre_grupo, nombre_politica):
        if nombre_grupo in iam_servicio.grupos:
            iam_servicio.grupos['politicas']=json.loads(nombre_politica)
            print(f"Se asignó la politica {nombre_politica} al grupo {nombre_grupo}")
        else:
            print(f"No existe el grupo {nombre_grupo}")
    
iam_consola=IAM_Consola()

#Creamos un usuario: 
iam_consola.crear_usuario(iam_servicio, "Gian Carlos")

#creamos un grupo:
iam_consola.crear_grupo(iam_servicio, "Admin")

#funcion para listar usuarios
lista= iam_consola.listar_usuarios(iam_servicio)
print(lista)





    

    




