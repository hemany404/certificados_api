
 Certificados API - Emissão e Verificação de Certificados Digitais

Este projeto é uma API construída com *FastAPI* que permite a *emissão*, *armazenamento*, *verificação pública* e *gerenciamento* de certificados digitais. É ideal para instituições de ensino, cursos online e treinamentos que desejam gerar certificados personalizados, com *QR Code*, segurança e validação confiável.

---

🚀 Funcionalidades

- ✅ Cadastro de instituições emissoras
- 🧾 Emissão de certificados digitais com:
  - Nome do aluno
  - Curso
  - Carga horária
  - Data de emissão
  - QR Code único com link de verificação
- 🔐 Geração de *hash único* para validação
- 🌐 Verificação pública de certificados via endpoint


---

🧱 Tecnologias Utilizadas

| Tecnologia | Finalidade        |
| ---------- | ----------------- |
| FastAPI    | Framework Backend |
| SQLAlchemy | ORM               |
| JWT        | Autenticação      |
| Sqlite     | Banco de dados    |
| Alembic    | Migrações         |
| Pydantic   | Validação         |
| Reportlab  |  PDF         |
| Hashlib    |  Hash        |

---

🏗 Estrutura de Pastas

```
certificados_api/
├── app/
│   ├── main.py
│   ├── models/
│   ├── schemas/
│   ├── routers/
│   ├── core/
│   ├── services/
│   └── utils/
├── requirements.txt
├── README.md
```

---

⚙️ Como Rodar

1. Clone o projeto:
   ```bash
   git clone https://github.com/hemany404/certificados_api.git
   ```

2. Crie o ambiente virtual e instale as dependências:
   ```bash
   python -m venv venv
   venv\Scripts\activate no Windows
   pip install -r requirements.txt
   ```

3. Execute a API:
   ```bash
   uvicorn app.main:app --reload
   ```

4. Acesse a documentação Swagger:
   ```
   http://127.0.0.1:8000/docs
   ```

---

📦 Endpoints Principais

- *POST /instituicoes/* – Criar instituição
- *POST /instituicoes/* – Fazer login
- *POST /certificados/* – Emitir certificado
- *GET /verificar/{hash}* – Verificar autenticidade
- *GET /certificados/* – Listar certificados
- *GET /certificados/* – Buscar certificados pelo curso


---

🛡 Segurança

- JWT Token para rotas protegidas
- Hash único nos certificados




