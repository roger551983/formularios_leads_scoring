from fastapi import APIRouter, UploadFile, File
from SERVICES.upload_excel_service import save_excel,save_dmn

router = APIRouter()

@router.post("/guardar_excel")
async def upload_excel(file: UploadFile = File(...)):
    return save_excel(file)

@router.post("/guardar_dmn")
async def upload_dmn(file: UploadFile = File(...)):
    return save_dmn(file)
