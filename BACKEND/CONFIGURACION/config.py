from pathlib import Path
from dotenv import load_dotenv
import os

#ruta_archivo = os.path.join("CONFIGURACION", "variables_entorno.env")

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / "CONFIGURACION" / "variables_entorno.env"
print("Archivos encontrados:")
x = BASE_DIR / "CONFIGURACION" 
for f in x.iterdir():
    print(f.name)


if not ENV_PATH.exists():
    raise RuntimeError(f"No existe el archivo de entorno: {ENV_PATH}")

load_dotenv(ENV_PATH, override=True)

UPLOAD_EXCEL_DIR = os.getenv("UPLOAD_EXCEL_DIR")

if not UPLOAD_EXCEL_DIR:
    raise RuntimeError("UPLOAD_EXCEL_DIR no está definida")

UPLOAD_EXCEL_DIR = Path(UPLOAD_EXCEL_DIR.strip())
UPLOAD_EXCEL_DIR.mkdir(parents=True, exist_ok=True)

CAMUNDA_LOGIN_URL =os.getenv("CAMUNDA_LOGIN_URL")
CAMUNDA_BASE_URL =os.getenv("CAMUNDA_BASE_URL")
CAMUNDA_USER =os.getenv("CAMUNDA_USER")
CAMUNDA_PASSWORD=os.getenv("CAMUNDA_PASSWORD")




