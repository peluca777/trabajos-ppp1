from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers import albums

app = FastAPI(
    title="Sistema de Gestión de Álbumes Musicales",
    description=(
        "API desarrollada con FastAPI para el TP Evaluativo de PP1 - Python. "
        "Permite gestionar un catálogo de álbumes musicales con operaciones CRUD completas."
    ),
    version="1.0.0",
)

# ─── CORS ─────────────────────────────────────────────────────────────────────

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── ROUTERS ──────────────────────────────────────────────────────────────────
app.include_router(albums.router)
