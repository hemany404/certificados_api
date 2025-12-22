from fastapi import APIRouter,Depends,HTTPException
from app.dependecias import verificar_usuario
from app.models.modelos import Instituicao,Certificado
from sqlalchemy.orm import session
from app.core.database import pegar_db



instituicao_roteador = APIRouter(prefix="/instituicao",tags=["instituicao"])

@instituicao_roteador.post("/instituicao/deletar")
async def deletar_instituicao(
        session: session = Depends(pegar_db),
        instituicao: Instituicao = Depends(verificar_usuario)):
    
    instituicao = session.query(Instituicao).filter(Instituicao.id == instituicao.id).first()

    if not instituicao:
        raise HTTPException(status_code=404,detail="instituiçao não encontrada")
    
    session.delete( instituicao)
    session.commit()

    return {
        "mensagem":f"{instituicao.nome}deletada com sucesso"
    }
    

@instituicao_roteador.get("/lista_certificados_emitidos")
async def lista_certificado(
        session:session=Depends(pegar_db),
        instituicao:Instituicao = Depends(verificar_usuario)):
    certificados =session.query(Certificado).filter(Certificado.instituicao_id == instituicao.id).all()

    if not certificados:
        return HTTPException(status_code=404,detail="certificados não encontrado")
    
    return{
        "numero de certificados emitidos": len(certificados),
        "certificados": certificados
    }

@instituicao_roteador.get("/buscar_certiifcado_curso/{curso}")
async def buscar_certiifcado_curso(
        curso: str ,
        session:session = Depends(pegar_db),
        instituicao: Instituicao = Depends(verificar_usuario)):

    certificados =session.query(Certificado).filter(Certificado.instituicao_id == instituicao.id).all()
    
    for certificado in certificados:
        cont = 0
        if certificado.curso == curso:
            cont +=1
        else:
            raise HTTPException(status_code=404, detail="certificados não encontrado")    
        return{
            f"número de certificados no curso de {curso}": cont,
            "certificado": certificado
            
        }
         