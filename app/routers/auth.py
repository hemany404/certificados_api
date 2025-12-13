from fastapi import APIRouter, Depends, HTTPException,BackgroundTasks
from sqlalchemy.orm import session
from app.models.modelos import Instituicao
from app.dependecias import verificar_usuario
from jose import jwt,JWTError
from app.core.database import pegar_db
from app.schemas.schema import InstituicaoSchema,LoginSchema
from main import bcrypt_context,SECRETY_KEY,ALGORITHM,ACESS_TOKEN_MINUTO_EXPIRACAO
from datetime import datetime,timedelta,timezone
from fastapi.security import OAuth2PasswordRequestForm


auth_roteador = APIRouter(prefix="/auth", tags=["autenticação"])

def criar_token(id_instituicao: int, duracao_token = timedelta(minutes=ACESS_TOKEN_MINUTO_EXPIRACAO)):
    data_expircao = datetime.now(timezone.utc) + duracao_token
    dic_info = {"sub":str(id_instituicao), "expiracao": str(data_expircao)}
    jwt_codificado = jwt.encode(dic_info,SECRETY_KEY,ALGORITHM)
    return jwt_codificado

def autenticar_usuario(email,senha,session):
    instituicao = session.query(Instituicao).filter(Instituicao.email == email).first()
    if not instituicao:
        return False
    elif not bcrypt_context.verify(senha,instituicao.senha):
        return False
    return instituicao

@auth_roteador.post("/criar_conta")
async def criar_conta(instituicao_schema: InstituicaoSchema, session: session = Depends(pegar_db)):
    instituicao = session.query(Instituicao).filter(Instituicao.email == instituicao_schema.email).first()

    if instituicao:
        raise HTTPException(status_code=400,detail="este email já está cadastrado")
    else:
        senha_criptografada = bcrypt_context.hash(instituicao_schema.senha)
        nova_instituicao = Instituicao(instituicao_schema.nome,instituicao_schema.email,senha_criptografada,instituicao_schema.logo_url)
        session.add(nova_instituicao)
        session.commit()
        return{
            "mensagem":"instituição cadastrada com sucesso"
        }
    
@auth_roteador.post("/login")   
async def login(login_schema: LoginSchema, session: session = Depends(pegar_db)):
    Instituicao = autenticar_usuario(login_schema.email,login_schema.senha,session)
    if not Instituicao:
        raise HTTPException(status_code=400,detail="instituição não encontrado ou cadastrado")
    
    else:
        acess_token = criar_token(Instituicao.id)
        refresh_token = criar_token(Instituicao.id, duracao_token=timedelta(days=30))                              
        return{
            "access_token":acess_token,
            "refresh_token":refresh_token,
            "token_type":"Bearer"
        }
    
@auth_roteador.post("/login-form")   
async def login_form(dados_formulario: OAuth2PasswordRequestForm = Depends(), session: session = Depends(pegar_db)):
    instituicao = autenticar_usuario(dados_formulario.username,dados_formulario.password,session)
    if not instituicao:
        raise HTTPException(status_code=400,detail="instituição não encontrado ou cadastrado")
    
    else:
        acess_token = criar_token(instituicao.id)
        return{
            "access_token":acess_token,
            "token_type":"Bearer"
        }       
    
@auth_roteador.post("/refresh_token")
async def utilizar_refresh_token(instituicao: Instituicao = Depends(verificar_usuario)):
    access_token = criar_token(instituicao.id)
    return{
        "access": access_token,
        "token_type":"Bearer"
    }   







