from fastapi import FastAPI, Path, Query, Body

app = FastAPI()

#Los Big Four
discos = [
    {"id": 1, "banda": "Metallica", "album": "Master of Puppets", "anio": 1986},
    {"id": 2, "banda": "Megadeth", "album": "Rust in Peace", "anio": 1990},
    {"id": 3, "banda": "Slayer", "album": "Reign in Blood", "anio": 1986},
    {"id": 4, "banda": "Anthrax", "album": "Among the Living", "anio": 1987}
]

#GET: Obtener todos los discos
@app.get("/discos")
async def get_discos(genero: str = Query(None, min_length=3, max_length=15)):
    # Genero es un query opcional con validación de texto
    return discos

#GET: Obtener por ID
@app.get("/discos/{id}")
async def get_disco_by_id(id: int = Path(..., gt=0)):
    for disco in discos:
        if disco["id"] == id:
            return disco
    return {"Detail": "Not found"}

#POST: Crear disco 
@app.post("/discos")
async def crear_disco(
    id: int = Body(...), 
    banda: str = Body(...), 
    album: str = Body(...), 
    anio: int = Body(..., gt=1980) # Validacion: año debe ser mayor a 1980
):
    nuevo_disco = {"id": id, "banda": banda, "album": album, "anio": anio}
    discos.append(nuevo_disco)
    return nuevo_disco

#PUT: Editar disco
@app.put("/discos/{id}")
async def editar_disco(
    id: int = Path(..., gt=0), 
    album: str = Body(..., min_length=1), 
    anio: int = Body(...)
):
    for disco in discos:
        if disco["id"] == id:
            disco["album"] = album
            disco["anio"] = anio
            return disco
    return {"Detail": "Not Found"}

#DELETE: Borrar disco
@app.delete("/discos/{id}")
async def borrar_disco(id: int = Path(..., gt=0)):
    for disco in discos:
        if disco["id"] == id:
            discos.remove(disco)
            return {"Detail": "Borrado exitosamente"}
    return {"Detail": "No encontrado"}