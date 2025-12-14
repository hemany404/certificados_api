from hashlib import sha256
def gerar_hash(nome_aluno,curso,instituicao,carga_horaria):
    itens =[b"nome_aluno",b"curso",b"instituicao",b"carga_horaria"]
    hash = sha256()
    for item in itens:
        hash.update(item)
    hash.hexdigest()  
