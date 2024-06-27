import uuid

# Clase IAMService para simular el servicio IAM de AWS
class IAMService:
    def __init__(self):
        self.users = {}
        self.groups = {}
        self.policies = {}
        self.roles = {}

iam_service = IAMService()

# Clase IAMConsole para simular la consola IAM de AWS
class IAMConsole:
    def create_user(self, iam_service, user_name): # Función que permite crear un usuario
        iam_service.users[user_name] = {'policies': [], 'mfa_enabled': False, 'roles': []}
        print(f"User '{user_name}' created.")

    def create_group(self, iam_service, group_name): # Función que permite crear el grupo
        iam_service.groups[group_name] = {'policies': [], 'users': []}
        print(f"Group '{group_name}' created.")

    def create_role(self, iam_service, role_name, policy): # Función que permite crear los roles
        iam_service.roles[role_name] = {'policy': policy}
        iam_service.policies[role_name] = policy 
        print(f"Role '{role_name}' created with policy '{policy.name}'.")

iam_console = IAMConsole()

# Crear usuarios
iam_console.create_user(iam_service, "Gian Quezada")
iam_console.create_user(iam_service, "Carlos Marceliano1")
iam_console.create_user(iam_service, "Carlos Marceliano2")
iam_console.create_user(iam_service, "Carlos Marceliano3")

# Crear grupos
iam_console.create_group(iam_service, "admin-group")
iam_console.create_group(iam_service, "backend")
iam_console.create_group(iam_service, "frontend")
iam_console.create_group(iam_service, "base-de-datos")

# Función para listar usuarios
def list_users(iam_service):
    return list(iam_service.users.keys())

# Función para listar grupos
def list_groups(iam_service):
    return list(iam_service.groups.keys())

print("Users:", list_users(iam_service))
print("Groups:", list_groups(iam_service))

print("------")
print("Información Gian Quezada:",iam_service.users["Gian Quezada"])
print("Carlos Marceliano1:",iam_service.users["Carlos Marceliano1"])
print("Carlos Marceliano2:",iam_service.users["Carlos Marceliano2"])
print("Carlos Marceliano3:",iam_service.users["Carlos Marceliano3"])
print("------")

# Función que permite agregar los usuario 
def add_user_to_group(iam_service, user_name, group_name):
    if user_name in iam_service.users and group_name in iam_service.groups:
        iam_service.groups[group_name]['users'].append(user_name)
        for policy in iam_service.groups[group_name]['policies']:
            iam_service.users[user_name]["policies"].append(policy)
        print(f"User '{user_name}' added to group '{group_name}'.")

# Función para asignar una política a un usuario
def assign_policy_to_user(iam_service, user_name, policy):
    if user_name in iam_service.users:
        iam_service.users[user_name]['policies'].append(policy)
        print(f"Policy '{policy.name}' assigned to user '{user_name}'.")

# Función para asignar una política a un grupo
def assign_policy_to_group(iam_service, group_name, policy):
    if group_name in iam_service.groups:
        iam_service.groups[group_name]['policies'].append(policy)
        print(f"Policy '{policy.name}' assigned to group '{group_name}'.")

# Clase Policy para simular políticas de IAM
class Policy:
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions

    def __repr__(self):
        return f"(nombre='{self.name}', permisos={self.permissions})"

# Crear políticas para los grupos
admin_full_policy = Policy("AdminFullPolicy", ["s3:*", "ec2:*", "rds:*"])
backend_full_policy = Policy("BackendFullPolicy", ["ec2:*"])
frontend_full_policy = Policy("FrontendFullPolicy", ["s3:*"])
database_full_policy = Policy("DatabaseFullPolicy", ["rds:*"])

iam_service.policies["AdminFullPolicy"] = admin_full_policy
iam_service.policies["BackendFullPolicy"] = backend_full_policy
iam_service.policies["FrontendFullPolicy"] = frontend_full_policy
iam_service.policies["DatabaseFullPolicy"] = database_full_policy

# Asignar políticas a los grupos
assign_policy_to_group(iam_service, "admin-group", admin_full_policy)
assign_policy_to_group(iam_service, "backend", backend_full_policy)
assign_policy_to_group(iam_service, "frontend", frontend_full_policy)
assign_policy_to_group(iam_service, "base-de-datos", database_full_policy)

# Añadir usuarios a los grupos
add_user_to_group(iam_service, "Gian Quezada", "admin-group")
add_user_to_group(iam_service, "Carlos Marceliano1", "backend")
add_user_to_group(iam_service, "Carlos Marceliano2", "frontend")
add_user_to_group(iam_service, "Carlos Marceliano3", "base-de-datos")

print("-----Lista de grupos y sus contenidos-----")
print("administracion:",iam_service.groups["admin-group"])
print("backend:",iam_service.groups["backend"])
print("frontend:",iam_service.groups["frontend"])
print("base de datos:",iam_service.groups["base-de-datos"])

print("-----Lista de usuarios y su información-----")
print("Gian Quezada:",iam_service.users["Gian Quezada"])
print("Carlos Marceliano1:",iam_service.users["Carlos Marceliano1"])
print("Carlos Marceliano2:",iam_service.users["Carlos Marceliano2"])
print("Carlos Marceliano3:",iam_service.users["Carlos Marceliano3"])
print("------")

# Crear roles de consulta
ec2_read_only_policy = Policy("EC2ReadOnlyPolicy", ["ec2:Describe*"])
rds_read_only_policy = Policy("RDSReadOnlyPolicy", ["rds:Describe*"])

iam_service.users["Carlos Marceliano1"]["roles"] = rds_read_only_policy
iam_service.users["Carlos Marceliano2"]["roles"] = ec2_read_only_policy

print("-----Lista de grupos y sus contenidos-----")
print("administracion:",iam_service.groups["admin-group"])
print("backend:",iam_service.groups["backend"])
print("frontend:",iam_service.groups["frontend"])
print("base de datos:",iam_service.groups["base-de-datos"])

# Crear roles
iam_console.create_role(iam_service, "EC2ReadOnlyRole", ec2_read_only_policy)
iam_console.create_role(iam_service, "RDSReadOnlyRole", rds_read_only_policy)

# Función para generar credenciales temporales
def generate_temporary_credentials():
    access_key = str(uuid.uuid4())
    secret_key = str(uuid.uuid4())
    session_token = str(uuid.uuid4())
    print(f"Temporary credentials generated:\nAccess Key: {access_key}\nSecret Key:{secret_key}\nSession Token: {session_token}")
generate_temporary_credentials()


print("\nPara el caso del usuario 'Marceliano Quezada2'")
creds_backend_ec2 = generate_temporary_credentials()
print("\nPara el caso del usuario 'Marceliano Quezada1'")
creds_backend_rds = generate_temporary_credentials()

# Mostrar credenciales generadas
print("\n-----Lista de usuarios y su información-----")
print("Gian Quezada:",iam_service.users["Gian Quezada"])
print("Carlos Marceliano1:",iam_service.users["Carlos Marceliano1"])
print("Carlos Marceliano2:",iam_service.users["Carlos Marceliano2"])
print("Carlos Marceliano3:",iam_service.users["Carlos Marceliano3"])
print("------")
