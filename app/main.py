from fastapi import FastAPI
from app.config import engine, Base
from app.routes.usuario_routes import usuario_bp

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(usuario_bp, prefix="/usuarios", tags=["usuarios"])
