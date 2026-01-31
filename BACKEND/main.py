from fastapi import FastAPI
from API.upload_router import router as r
from API.camunda_router import router as camunda_r
from API.cliente_router import router as cliente_r
from API.prueba_router import router as prueba_r
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4300",
        "http://localhost:4200",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(r,  tags=["Files"])
app.include_router(camunda_r, prefix="/camunda",tags=["Camunda"])
app.include_router(cliente_r,prefix="/cliente",tags=["Cliente"])
app.include_router(prueba_r,tags=["Prueba"])

#prefix="/files",