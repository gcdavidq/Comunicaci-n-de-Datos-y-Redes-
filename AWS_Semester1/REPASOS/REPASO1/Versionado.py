class S3BucketWithVersioning: 
    def __init__(self): 
        # Inicializa un diccionario para almacenar las versiones de los objetos
        self.versions = {} 
     
    def put_object(self, bucket, key, data): 
        # Verifica si el bucket existe en el diccionario de versiones
        if bucket not in self.versions: 
            # Si no existe, inicializa un nuevo diccionario para el bucket
            self.versions[bucket] = {} 
        # Verifica si la clave existe en el diccionario del bucket
        if key not in self.versions[bucket]: 
            # Si no existe, inicializa una nueva lista para la clave
            self.versions[bucket][key] = [] 
        # Añade el nuevo dato a la lista de versiones de la clave
        self.versions[bucket][key].append(data)     
    
    def get_object(self, bucket, key, version=None): 
        # Si no se especifica una versión, devuelve la última versión del objeto
        if version is None: 
            return self.versions.get(bucket, {}).get(key, [])[-1] 
        # Si se especifica una versión, devuelve la versión correspondiente
        return self.versions.get(bucket, {}).get(key, [])[version]

# Ejemplo de uso de la clase S3BucketWithVersioning
bucket_versioning = S3BucketWithVersioning()

# Añadir objetos al bucket
bucket_versioning.put_object('my_bucket', 'my_key', 'data_v1')
bucket_versioning.put_object('my_bucket', 'my_key', 'data_v2')

# Obtener la última versión del objeto
print(bucket_versioning.get_object('my_bucket', 'my_key'))  # Output: 'data_v2'

# Obtener la versión específica del objeto
print(bucket_versioning.get_object('my_bucket', 'my_key', 0))  # Output: 'data_v1'
