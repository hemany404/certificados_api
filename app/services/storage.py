
from app.core.config import PDF_FOLDER, QR_FOLDER


def local_path_url(path: str) -> str:
    # Se a API estiver servindo arquivos estáticos você pode mapear a URL base
    # Ex: BASE_URL + "/static/pdfs/..." - por enquanto retornamos o caminho absoluto/local.
    return path