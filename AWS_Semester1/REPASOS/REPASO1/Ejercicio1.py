class IAMService:
  def __init__(self):
    #creamos los atributos que necesitaremos. 
    self.users={}
    self.groups={}
    self.roles={}
    self.policies_roles={}
    self.policies_users={}
    self.policies_groups={}
iam_service=IAMService()

class IAMConsole:

  #creamos el metodo para crear un usuario
  def create_user(self,iam_service,username):
    # Añadir un nuevo usuario con una lista vacía de políticas
    iam_service.users[username]={'policies_user':[]}
    print(f"User {username} created")

  #Creamos el metodo crear grupo
  def create_group(self,iam_service,groupname):
    iam_service.groups[groupname]={'policies_group':[], 'users':[]}
    print(f"Group {groupname} created")

  #Para mostrar los usuarios
  def list_users(self,iam_service):
    users = list(iam_service.users.keys())
    print(f"Users: {users}")
    return users
  #Para mostrar los grupos
  def list_groups(self,iam_service):
    groups=list(iam_service.groups.keys())
    print(f"Groups: {groups}")
    return groups

  #Para añadir usuarios a grupos y asignar politicas a usuarios y grupos
  def add_user_to_group(self, iam_service,username,groupname):
    if username in iam_service.users and groupname in iam_service.groups:
      iam_service.groups[groupname]['users'].append(username)
      print(f"User {username} added to group {groupname}")

  #Asignar politicas para usuarios
  def add_policy_user(self, iam_service,username,policyname):
    if username in iam_service.users:
      iam_service.users[username]['policies_user'].append(policyname)
      print(f"Policy {policyname} added to user {username}")
    else:
      print(f"Group {username} does not exist. Policy {policyname} not added.")



  #Asignar politicas para grupos
  def add_policy_group(self, iam_service,groupname,policyname):
    if groupname in iam_service.groups:
      iam_service.groups[groupname]['policies_group'].append(policyname)
      print(f"Policy {policyname} added to group {groupname}")
    else:
      print(f"Group {groupname} does not exist. Policy {policyname} not added.")


#Creamos una clase para definir los permisos mediante las politicas IAM
class IAMPolicy:
  def __init__(self, name, permissions):
    self.name = name
    self.permissions = permissions

  #llamamos al metodo especial str
  def __str__(self):
    return f"Policy: {self.name}, Permissions: {self.permissions}"

iam_console=IAMConsole()
iam_console.create_user(iam_service, "Juan")
iam_console.create_group(iam_service, "Desarrolladores")
iam_console.list_users(iam_service)
iam_console.list_groups(iam_service)
iam_console.add_user_to_group(iam_service, "Juan", "Desarrolladores")


admin_policy=IAMPolicy("AdminsPolic",["s3:ListBucket", "ec2:StartInstances"] )
print(admin_policy)
group_admin_policy=IAMPolicy("PoliticsGroupsDevelopers",["s3:*", "ec2:*"] )
print(group_admin_policy)

#Agregamos las politicas a los IAMServices
iam_service.policies_users["Juan"] = (admin_policy)
iam_service.policies_groups["Desarrolladores"] = (group_admin_policy)

#Otra forma de agregar:
iam_console.add_policy_user(iam_service, "Juan", "AdminsPolic")
iam_console.add_policy_group(iam_service, "Marketin", "PoliticsGroupsDevelopers")