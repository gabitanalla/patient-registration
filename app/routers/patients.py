from typing import Annotated

from fastapi import Body, APIRouter, File, UploadFile
from pydantic import BaseModel, Field, EmailStr

from app.database import create_patient

router = APIRouter(
    prefix='/patient',
    tags = ['patients']
)

class Patient(BaseModel):
    name: str = Field(min_length=5)
    email: EmailStr = Field(default=None)
    address: str = Field(min_length=5)
    phone: str = Field(min_length=5)

@router.post("/")
async def post_patient(patient: Patient):
    # try:
    create_patient(patient.name, patient.email, patient.address, patient.phone)
    #     return {"message": "Patient created"}
    # except:
    #     return {"message": "ERROR"}