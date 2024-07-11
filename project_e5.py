"""
En este script se simulará un sistema completo de gestion de Archivos en la nube mediante AWS, especificamente usando el servicio de almancenamiento S3

Se ha integrado las principales funcionalidades de este servicio, así como tambien algunas características que permitirán un verdadero entorno de S3.

En cuanto a las librerias importadas:
- json para la creacion de politicas en este formato
- time para posibles simulaciones de tiempo de espera
- re para 
"""

import json 
import time
import re
class Buckets:
    """
    Esta clase simula la gestion integral de Buckets en AWS S3.
    
    Mediante la implementacion de distintos metodos estamos mostrando cada una de las opciones que nos ofrece AWS S3.
    """
    def __init__(self):
        """
        Con este primer metodo estamos inicializando la clase Buckets, la cual tendrá un atributo que permitirá almacenar los buckets en forma de Diccionario.
        """
        
        self.buckets={}

    def crear_buckets(self, nombre_bucket):
        """
        Mediante esta función, crearemos los diferentes buckets. 
        Toma como parametros el nombre del bucket a crear.
        """
        #empezamos con la creación de la variable caracteres_permitidos, la cual almacenará todos los caracteres que admite S3 para la creación de un bucket.
        caracteres_permitidos = re.compile(r'^[a-z0-9!_\-.*\'()]+$')
        #Mediante una primera condicional se validará que el nombre del bucket tenga más de 3 caracteres y menos de 63
        #tambien se validará que todo el nombre sea en minuscula y se validará que contenga los caracteres permitidos en la variable ya mencionada
        if (len(nombre_bucket)>3  and len(nombre_bucket)<63) and \
            (nombre_bucket.islower() or nombre_bucket) and \
            caracteres_permitidos.match(nombre_bucket):
            #despues de cumplir con todos los requerimientos, se pasará a crear un diccionario dentro del diccionario 'buckets' mediante la clave nombre_bucket, 
            #el cual tendrá como clave a los objetos y politicas del diccionario. Estos dos ultimos tambien serán en forma de diccionario.
            self.buckets[nombre_bucket]={'objetos': {}, 'politicas':{}}
            print(f"Se creó el bucket:{nombre_bucket}")
        else:
            print(f"El nombre del bucket {nombre_bucket} incumple con las buenas practicas para nombra un Bucket. Por favor, intenta con otro nombre")
    
    def crear_politicas(self, bucket, politica_json):
        """
        Mediante esta funcion se cargarán las politicas en formaton json.
        """
        self.buckets[bucket]['politicas']=json.loads(politica_json)
        print(f'Se creó la politica {politica_json}')
    
    
    def leer_bucket(self, bucket):
        """
        La funcion leer_buckets nos permitirá listar todos los objetos dentro de un bucket en especifico.
        Para realizar dicha acción, primero se comprueba que se tengan los permisos necesarios, ello mediante el acceso a las politicas adjuntas.
        """
        if bucket in self.buckets: 
            print(f"Al parecer quieres leer lo que contiene el bucket {bucket}. Verificaremos si tienes los permisos necesarios")
            permisos=self.buckets[bucket]['politicas']['Statement']
            for permiso in permisos:
                if 's3:ListBucket' in permiso['Action'] and permiso['Resource'] == bucket:
                    print(f"Se confirmó que tienes permiso de lectura al bucket {bucket}.")
                    print(list(self.buckets[bucket]['objetos']))
                else:
                    print(f"No existe el permiso para leer el bucket {bucket}")
        else:
            print(f'No existe el bucket {bucket}')
    
    def editar_bucket(self, bucket, key, valor):
        """
        La funcion editar_bucket nos permitirá editar el valor dentro de un objeto existente en el bucket escogido.
        """
        if bucket in self.buckets:
            print(f"Al parecer quieres editar el valor del objeto {key} dentro del bucket {bucket}. Verificaremos si tienes los permisos necesarios")
            permisos=self.buckets[bucket]['politicas']['Statement']
            for permiso in permisos:
                if 's3:EditObject' in permiso['Action'] and permiso['Resource'] == bucket:
                    print(f"Se confirmó que tienes permiso de edicion al bucket {bucket}.")
                    self.buckets[bucket]['objetos'][key]['valor']=valor
                    print(f"El nuevo valor del objeto {key} es: {self.buckets[bucket]['objetos'][key]['valor']}")
                else:
                    print(f"No existe el permiso para editar el bucket {bucket}")
        else:
            print(f'No existe el bucket {bucket}')

    def eliminar_objeto(self, bucket, key):
        """
        La funcion eliminar_bucket nos permtirá elimianr un objeto dentro del bucket escogido, siempre y cuando se cuente con los permisos necesarios.
        """

        if bucket in self.buckets:
            print(f"Al parecer quieres eliminar el objeto {key} del bucket {bucket}. Verificaremos si tienes los permisos necesarios")
            permisos=self.buckets[bucket]['politicas']['Statement']
            for permiso in permisos:
                if 's3:DeleteObject' in permiso['Action'] and permiso['Resource'] == bucket:
                    print(f"Se confirmó que tienes permiso de edicion al bucket {bucket}.")
                    del self.Buckets[bucket]['objetos'][key]
                    print("Se eliminó el objeto")
                
                else:
                    print(f"No existe el permiso para leer el bucket {bucket}")
        else:
            print(f'No existe el bucket {bucket}')
            

buckets_=Buckets()

class Objetos:
    """
    Con la clase objetos, simulamos la gestión integral de los objetos en AWS S3. 
    Estamos incluyendo metodos que nos permitan trabajar con caracteristicas unicas de los objetos, como los metadatos, por ejemplo.
    """

    def __init__(self):
        """
        Inicializamos la clase con la creacion del atributo objetos, el cual es un diccionarío que contendrá los objetos creados.
        
        """
        self.objetos={}

    def crear_objeto(self, key):
        """
        Mediante el metodo crear objetos, asigamos un diccionario a la clave key en el diccionario self.objetos.
        El diccionario asignado contiene tres claves como tal: metadatos, valor y politicas, las cuales a su ves tienen un diccionario vacio como valor.
        
        """
        self.objetos[key] = {'metadatos': {}, 'valor': {}, 'politicas': {}}
        print(f"Se creó el objeto {key}")
    
    def agregar_metadatos(self, key, metadatos):
        """
        Agregaremos metadatos al objeto previamente creado. 
        
        Ello lo hacemos mediante la actualizacion del diccionario 'metadatos', el cual estaba vacio.
        
        """

        if key in self.objetos:
            self.objetos[key]['metadatos']=metadatos
            print(f'El objeto {key} tiene la siguiente informacion como metadatos: tipo: {metadatos}')
        else:
            print(f"El diccionario {key} no existe")
    
    def crear_politicas_objetos(self, key, nombre_politica, politica):
        """
        Al igual que con los objetos, creamos politicas para cada objeto dentro de un bucket.

        """
        if key in self.objetos:
            self.objetos[key]['politicas'][nombre_politica]=json.loads(politica)
    
    def agregar_objetos_a_buckets(self, bucket, key, valor, buckets_):
        """
        Mediante esta función, agregaremos un objeto a un bucket en especifico.
        Esta función se hace interesante porque se trata de simular la encriptación del valor de un objeto en base al tipo de metadato que es. 
        Para la encriptación, se ha empleado cifrados conocidos como lo son el cifrado cesar y el cifrado vigenere.
        """
        if bucket in buckets_.buckets:
            print(f"Estamos a punto de subir el objeto {key} al bucket {bucket} ")
            print(f"Para mayor seguridad, primero cifraremos la informacion dentro del objeto {key}. Este proceso puede demorar un poco")
            if self.objetos[key]['metadatos']=='videos' or 'fotos':
                desplazamiento=int(input("Escoge cuanto de desplazamiento quieres para este cifrado: "))
                self.objetos[key]['valor']=tipo_cifrado.cifrado_cesar(valor, desplazamiento)

            elif self.objetos[key]['metadatos']=='documentos':
                clave=str(input('Ingrese la clave que quiere implementar en el cifrado: '))
                self.objetos[key]['valor']=tipo_cifrado.cifrado_vigenere(valor, clave)

            time.sleep(2)
            print("Ahora, procederemos a subir el objeto cifrado al bucket")
            buckets_.buckets[bucket]['objetos'][key]=self.objetos[key]
            print(f"El objeto {key} fue cifrado y subido al bucket {bucket}")
        else:
            print(f"No existe el bucket {bucket}")
    
    def descargar_objetos(self, bucket, key, buckets_):
        """
        Con esta función estamos simulando la descarga de un objeto. 
        
        Entonces, si para subirlo a un bucket se tuvo que cifrar, al momento de la descarga será necesario descifrar el valor del objeto mediante la clave definida al principio.

        """
        print(f"Procederemos con la descarga del objeto {key}")
        if bucket in buckets_.buckets:
            if key in buckets_.buckets[bucket]['objetos']:
                print("Primero,verificaremos que tipo de archivo es para realizar el descifrado correspondiente")
                if buckets_.buckets[bucket]['objetos'][key]['metadatos']=='videos' or 'fotos':
                    descifrar=buckets_.buckets[bucket]['objetos'][key]['valor']
                    desplazamiento=int(input('ingresa la cantidad de desplazamiento que ingresaste en el cifrado: '))
                    descarga=tipo_cifrado.descifrado_cesar(descifrar, desplazamiento)
                    print("La descarga se realizó con exito:")
                    print(descarga)
                
                elif buckets_.buckets[bucket]['objetos'][key]['metadatos']=='documentos':
                    descifrar=buckets_.buckets[bucket]['objetos'][key]['valor']
                    clave =str(input("Ingrese la clave que definió al momento de subir el objeto: "))
                    descarga=tipo_cifrado.descifrado_vigenere(descifrar, clave)
                    print("La descarga se realizó con exito:")
                    print(descarga)

                else:
                    print(f'Escoja un tipo de objeto disponible para cifrar')
            else:
                print(f'No existe el objeto {key} en el bucket {bucket}')
        else:
            print(f'No existe el buclet {bucket}')
 
objetos=Objetos()

class Tipo_Cifrado:
    """
    En esta clase se están implementando los dos tipos de cifrado que se usarán en la simulación, asi como su respectivo metodo de descifrado tambien.
    Asi mismo, para cada uno de los 4 metodos que se emplean en la clase se agrega el decorador staticmethod. 
    Ello se realizó basicamente porque las 4 funciones no dependen de una instancia de clase, lo cual hace más legible el codigo y es considerado una buena practica.
    Tambien se puede ejecutar sin agregar el decorador, pero para ello sería necesario una instancia de clase, incluso si el metodo no emplea self.
    """
    
    def cifrado_cesar(self, texto, desplazamiento):
        """
        Esta función no es propia, fue obtenida y adecuada de: https://lacriptadelhacker.wordpress.com/2020/10/25/criptografia-en-python-cifrado-cesar-y-vigenere/
        """
        resultado = ""
        for char in texto:
            if char.isalpha():
                desplazamiento_base = ord('A') if char.isupper() else ord('a')
                resultado += chr((ord(char) - desplazamiento_base + desplazamiento) % 26 + desplazamiento_base)
            else:
                resultado += char
        return resultado
    
    
    def cifrado_vigenere(self, texto, clave):
        """
        Esta funcion no es propia, fue obtenida y adecuada de: https://lacriptadelhacker.wordpress.com/2020/10/25/criptografia-en-python-cifrado-cesar-y-vigenere/
        """
        resultado = ""
        clave_repetida = (clave * (len(texto) // len(clave) + 1))[:len(texto)]
        for t, c in zip(texto, clave_repetida):
            if t.isalpha():
                desplazamiento_base = ord('A') if t.isupper() else ord('a')
                resultado += chr((ord(t) - desplazamiento_base + (ord(c.upper()) - ord('A'))) % 26 + desplazamiento_base)
            else:
                resultado += t
        return resultado
    
    
    def descifrado_cesar(self, texto_cifrado, desplazamiento):
        """
        Esta funcion no es propia, fue obtenida y adecuada de: https://lacriptadelhacker.wordpress.com/2020/10/25/criptografia-en-python-cifrado-cesar-y-vigenere/
        """
        resultado = ""
        for char in texto_cifrado:
            if char.isalpha():
                desplazamiento_base = ord('A') if char.isupper() else ord('a')
                resultado += chr((ord(char) - desplazamiento_base - desplazamiento) % 26 + desplazamiento_base)
            else:
                resultado += char
        return resultado
    

    def descifrado_vigenere(self, texto_cifrado, clave):
        """
        Esta funcion no es propia, fue obtenida y adecuada de: https://lacriptadelhacker.wordpress.com/2020/10/25/criptografia-en-python-cifrado-cesar-y-vigenere/
        """
        resultado = ""
        clave_repetida = (clave * (len(texto_cifrado) // len(clave) + 1))[:len(texto_cifrado)]
        for t, c in zip(texto_cifrado, clave_repetida):
            if t.isalpha():
                desplazamiento_base = ord('A') if t.isupper() else ord('a')
                resultado += chr((ord(t) - desplazamiento_base - (ord(c.upper()) - ord('A'))) % 26 + desplazamiento_base)
            else:
                resultado += t
        return resultado
    

tipo_cifrado=Tipo_Cifrado()

politica_admins="""
{
    "Version": "2024-06-14",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:PutObject", "s3:DeleteObject"],
            "Resource": "bucket_admins"
        }
    ]
}
"""

#USO
#Creamos un bucket
buckets_.crear_buckets("bucket_dev")

#creamos una politica y la agregamos a un bucket
buckets_.crear_politicas('bucket_dev', politica_admins)

#creamos un objeto
objetos.crear_objeto('Codigo_V1')

#agregamos metadatos a ese objeto
objetos.agregar_metadatos('Codigo_V1', 'documentoss')

#agregamos un objeto a un bucket
objetos.agregar_objetos_a_buckets('bucket_dev', 'Codigo_V1','print(holamundo)', buckets_)

#descargamos un objeto de un bucket
objetos.descargar_objetos('bucket_dev', 'Codigo_V1',buckets_)

#creamos otro objeto
objetos.crear_objeto('Foto_Ejecucion')
objetos.agregar_metadatos('Foto_Ejecucion', 'fotos')
objetos.agregar_objetos_a_buckets('bucket_dev', 'Foto_Ejecucion', 'Esta es una imagen.jpg', buckets_)
objetos.descargar_objetos('bucket_dev','Foto_Ejecucion', buckets_ )

#intentamos leer un bucket de acuerdo a la politica asignada
buckets_.leer_bucket('bucket_dev')

        

    