from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.schemas.usuario_schema import UsuarioCreate

def get_usuarios(db: Session):
  return db.query(Usuario).all()

def get_usuario(db: Session, usuario_id: int):
  return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def create_usuario(db: Session, usuario: UsuarioCreate):
  nuevo_usuario = Usuario(nombre=usuario.nombre, email=usuario.email)
  db.add(nuevo_usuario)
  db.commit()
  db.refresh(nuevo_usuario)
  return nuevo_usuario

def update_usuario(db: Session, usuario_id: int, usuario: UsuarioCreate):
  usuario_existente = db.query(Usuario).filter(Usuario.id == usuario_id).first()
  usuario_existente.nombre = usuario.nombre
  usuario_existente.email = usuario.email
  db.commit()
  db.refresh(usuario_existente)
  return usuario_existente

def delete_usuario(db: Session, usuario_id: int):
  usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
  if usuario:
    db.delete(usuario)
    db.commit()
    return usuario
