from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.usuario_crud import get_usuarios, get_usuario, create_usuario, delete_usuario, update_usuario
from app.schemas.usuario_schema import UsuarioCreate, UsuarioResponse
from app.config import SessionLocal

usuario_bp = APIRouter()

def get_db():
  db = SessionLocal()
  try:
      yield db
  finally:
      db.close()

@usuario_bp.get("/", response_model=list[UsuarioResponse])
def leer_usuarios(db: Session = Depends(get_db)):
  return get_usuarios(db)

@usuario_bp.get("/{usuario_id}", response_model=UsuarioResponse)
def leer_usuario(usuario_id: int, db: Session = Depends(get_db)):
  usuario = get_usuario(db, usuario_id)
  if usuario is None:
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
  return usuario

@usuario_bp.post("/", response_model=UsuarioResponse)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
  return create_usuario(db, usuario)

@usuario_bp.put("/{usuario_id}", response_model=UsuarioResponse)
def actualizar_usuario(usuario_id: int, usuario: UsuarioCreate, db: Session = Depends(get_db)):
  usuario_existente = get_usuario(db, usuario_id)
  if usuario_existente is None:
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
  return update_usuario(db, usuario_id, usuario)

@usuario_bp.delete("/{usuario_id}", response_model=UsuarioResponse)
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
  usuario = delete_usuario(db, usuario_id)
  if usuario is None:
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
  return usuario
