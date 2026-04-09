from fastapi import FastAPI

app = FastAPI()
usuarios = ["Marcos"] 

@app.get("/ver-usuarios") # GET
async def ver_usuarios():
    return {"usuarios": usuarios} # Muestra la lista de usuarios

@app.post("/agregar-usuario") # POST
async def agregar_usuario(nombre: str):
    usuarios.append(nombre) # Agrega usuarios nuevos
    return {"mensaje": "Usuario agregado", "usuarios": usuarios}

@app.put("/modificar-usuarios") # PUT
async def saludar(posición: int, nombre: str):
    if posición < len(usuarios): 
        usuarios[posición] = nombre 
        return{"mensaje": "Usuario modificado corréctamente", "usuarios": usuarios}  

@app.delete("/borrar-usuarios") # DELETE
async def borrar_usuario(posición: int):
    if posición < len(usuarios): 
        eliminar = usuarios.pop(posición)
        return{"mensaje": "Usuario elimnado correctamente", "usuarios": usuarios}
    return {"Error": "No hay usuarios cargados en esa posición"}


@app.get("/")
async def inicio():
    return {"Hola": "Mundo"}


@app.post("/post")
async def saludar():
    return {"Hola": "mundo"}



@app.get("/hola/{nombre}")
async def saludar_nombre(nombre: str):
    return {"mensaje": f"Hola {nombre}"}

@app.get("/info")
async def info(nombre: str, edad: int):
    return {"nombre": nombre, "edad": edad}

usuarios = []

@app.post("/usuarios")
async def crear_usuario(nombre: str):
    usuarios.append(nombre)
    return {"mensaje": "Usuario creado", "usuarios": usuarios}

@app.get("/usuarios")
async def listar_usuarios():
    return {"usuarios": usuarios}

usuarios_db = {
    "marcos": "1234",
    "jijo": "jijo"
}

@app.post("/login")
async def login(usuario: str, password: str):
    if usuario in usuarios_db and usuarios_db[usuario] == password:
        return {"mensaje": "Login exitoso"}
    else:
        return {"error": "Credenciales incorrectas"}
    
@app.post("/registro")
async def regist_user(usuario: str, password: str):
    if usuario in usuarios_db:
        return {"error": "El usuario ya existe"}
    
    if len(password) < 4:
        return {"error": "La contraseña es muy corta"}
    usuarios_db[usuario] = password
    return {"mensaje": "Usuario registrado correctamente"}

