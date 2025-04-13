from pydantic import BaseModel

class Posicao(BaseModel):
    x: float
    y: float

class Movimento(BaseModel):
    direcao: float  # graus de 0 a 360
    velocidade: float  # unidades por segundo

class Barco(BaseModel):
    id: str
    pos: Posicao
    mov: Movimento