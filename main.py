from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
import os
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
SECRETY_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACESS_TOKEN_MINUTO_EXPIRACAO = int(os.getenv("ACESS_TOKEN_MINUTO_EXPIRACAO",30))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
bcrypt_context = CryptContext(schemes=["bcrypt"],deprecated= "auto")
oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/login-form")

from app.routers.auth import auth_roteador
from app.routers.certificados import certificado_roteador
from app.routers.verificacao import roteador_verificacao
from app.routers.instituicoes import instituicao_roteador


app.include_router(auth_roteador)
app.include_router(certificado_roteador)
app.include_router(roteador_verificacao)
app.include_router(instituicao_roteador)

