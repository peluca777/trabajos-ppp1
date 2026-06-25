from typing import Annotated
from pydantic import BaseModel, Field


class AlbumBase(BaseModel):
    """Modelo para creación y edición (sin id)."""
    titulo: Annotated[
        str,
        Field(
            min_length=1,
            max_length=100,
            description="Título del álbum",
            examples=["Thriller"]
        )
    ]
    artista: Annotated[
        str,
        Field(
            min_length=1,
            max_length=100,
            description="Nombre del artista o banda",
            examples=["Michael Jackson"]
        )
    ]
    anio: Annotated[
        int,
        Field(
            ge=1900,
            le=2100,
            description="Año de lanzamiento del álbum",
            examples=[1982]
        )
    ]
    genero: Annotated[
        str,
        Field(
            min_length=2,
            max_length=50,
            description="Género musical del álbum",
            examples=["Pop"]
        )
    ]


class Album(AlbumBase):
    """Modelo completo de respuesta (incluye id)."""
    id: Annotated[
        int,
        Field(
            gt=0,
            description="Identificador único del álbum",
            examples=[1]
        )
    ]
