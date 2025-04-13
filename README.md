# Aquanaltas 🌊🚢

**Aquanaltas** é um jogo distribuído onde cada barco é um container navegando em um mar digital. O mar é um servidor que sincroniza todos os barcos e simula comunicação entre eles quando estão próximos.

## Tecnologias:
- [x] Python + FastAPI (Servidor Mar)
- [x] Redis para comunicação entre réplicas
- [x] Kubernetes com Helm Charts
- [x] Containers Docker para barcos e mar
- [ ] Web frontend (em desenvolvimento)

## Como subir no cluster Kubernetes
```bash
cd helm-charts/mar
helm install mar .
