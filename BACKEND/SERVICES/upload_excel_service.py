from fastapi import UploadFile, HTTPException
from DAO.file_dao import save_file

def save_excel(file: UploadFile):
    if not file.filename.lower().endswith((".xlsx", ".xls")):
     raise HTTPException(
        status_code=400,
        detail="Solo se permiten archivos Excel (.xlsx o .xls)"
    )

    ruta_excel =save_file(file)

    return{
        "memsaje":"Archivo Guardado",
        "path":ruta_excel
    }