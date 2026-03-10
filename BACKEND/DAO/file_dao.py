import shutil
from pathlib import Path
from fastapi import UploadFile
from CONFIGURACION.config import UPLOAD_EXCEL_DIR

def save_file(file: UploadFile) -> str:
    destino = UPLOAD_EXCEL_DIR / file.filename
    with destino.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return str(destino)