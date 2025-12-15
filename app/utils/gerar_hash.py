import hashlib 
import os
from datetime import datetime,timezone
import secrets

def gerar_hash(seed: dict) -> dict:
    # Combina seed + aleatório para evitar colisões
    s = f"{seed}|{datetime.now(timezone.utc).isoformat()}|{secrets.token_hex(8)}"
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:32]  

def directorio(path:str):
    os.makedirs(path,exist_ok=True)
    return path