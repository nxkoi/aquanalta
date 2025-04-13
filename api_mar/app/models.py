from fastapi import FastAPI, HTTPException
from app.models import Barco
import redis, os, math, json

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
r = redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)

app = FastAPI()
RAIO = 30.0

@app.post("/update")
def update(barco: Barco):
    r.hset("barcos", barco.id, barco.json())
    return {"status": "ok"}

@app.get("/nearby")
def nearby(id: str):
    if not r.hexists("barcos", id):
        raise HTTPException(status_code=404, detail="Barco não encontrado")

    barco_base = Barco.parse_raw(r.hget("barcos", id))
    vizinhos = []
    for k, v in r.hgetall("barcos").items():
        if k == id:
            continue
        outro = Barco.parse_raw(v)
        dist = math.dist((barco_base.pos.x, barco_base.pos.y), (outro.pos.x, outro.pos.y))
        if dist <= RAIO:
            vizinhos.append({
                "id": outro.id,
                "dist": round(dist, 2),
                "direcao": outro.mov.direcao,
                "velocidade": outro.mov.velocidade
            })
    return vizinhos
