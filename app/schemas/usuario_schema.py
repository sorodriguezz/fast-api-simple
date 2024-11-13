from pydantic import BaseModel

class UsuarioBase(BaseModel):
  nombre: str
  email: str

class UsuarioCreate(UsuarioBase):
  pass

class UsuarioResponse(UsuarioBase):
  id: int

  class Config:
    orm_mode = True
