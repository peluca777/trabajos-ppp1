from typing import Annotated
from fastapi import APIRouter, HTTPException, Path, Query, status
from src.models.albums import Album, AlbumBase


router = APIRouter(
    prefix="/albums",
    tags=["Álbumes"],
)

# Tabla simulada de base de datos
albums_db: list[Album] = [
    Album(id=1, titulo="Thriller", artista="Michael Jackson", anio=1982, genero="Pop"),
    Album(id=2, titulo="Back in Black", artista="AC/DC", anio=1980, genero="Rock"),
    Album(id=3, titulo="The Dark Side of the Moon", artista="Pink Floyd", anio=1973, genero="Rock Progresivo"),
    Album(id=4, titulo="Nevermind", artista="Nirvana", anio=1991, genero="Grunge"),
]


def _siguiente_id() -> int:
    if not albums_db:
        return 1
    return max(a.id for a in albums_db) + 1


# ─── CREATE ────────────────────────────────────────────────────────────────────

@router.post(
    "/",
    response_model=Album,
    status_code=status.HTTP_201_CREATED,
    summary="Agregar álbum",
    description="Agrega un nuevo álbum a la base de datos.",
)
def crear_album(album: AlbumBase) -> Album:
    nuevo = Album(id=_siguiente_id(), **album.model_dump())
    albums_db.append(nuevo)
    return nuevo


# ─── READ ALL ──────────────────────────────────────────────────────────────────

@router.get(
    "/",
    response_model=list[Album],
    summary="Listar álbumes",
    description="Devuelve todos los álbumes. Permite filtrar por género.",
)
def listar_albums(
    genero: Annotated[
        str | None,
        Query(description="Filtrar por género musical", examples=["Rock"])
    ] = None,
) -> list[Album]:
    if genero:
        return [a for a in albums_db if a.genero.lower() == genero.lower()]
    return albums_db


# ─── READ ONE ──────────────────────────────────────────────────────────────────

@router.get(
    "/{album_id}",
    response_model=Album,
    summary="Obtener álbum por ID",
    description="Devuelve un álbum específico según su ID.",
    responses={
        404: {"description": "Álbum no encontrado"}
    },
)
def obtener_album(
    album_id: Annotated[
        int,
        Path(gt=0, description="ID del álbum a buscar", examples=[1])
    ],
) -> Album:
    for album in albums_db:
        if album.id == album_id:
            return album
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Álbum con id {album_id} no encontrado.",
    )


# ─── UPDATE ────────────────────────────────────────────────────────────────────

@router.put(
    "/{album_id}",
    response_model=Album,
    summary="Actualizar álbum",
    description="Reemplaza los datos de un álbum existente.",
    responses={
        404: {"description": "Álbum no encontrado"}
    },
)
def actualizar_album(
    album_id: Annotated[
        int,
        Path(gt=0, description="ID del álbum a actualizar", examples=[1])
    ],
    datos: AlbumBase,
) -> Album:
    for index, album in enumerate(albums_db):
        if album.id == album_id:
            actualizado = Album(id=album_id, **datos.model_dump())
            albums_db[index] = actualizado
            return actualizado
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Álbum con id {album_id} no encontrado.",
    )


# ─── DELETE ────────────────────────────────────────────────────────────────────

@router.delete(
    "/{album_id}",
    response_model=Album,
    summary="Eliminar álbum",
    description="Elimina un álbum de la base de datos y lo devuelve.",
    responses={
        404: {"description": "Álbum no encontrado"}
    },
)
def eliminar_album(
    album_id: Annotated[
        int,
        Path(gt=0, description="ID del álbum a eliminar", examples=[1])
    ],
) -> Album:
    for index, album in enumerate(albums_db):
        if album.id == album_id:
            return albums_db.pop(index)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Álbum con id {album_id} no encontrado.",
    )
