from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import  models, schemas, crud
from database import engine,get_db

models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Patients_model", description="A simple API to know patients", version="1.0.0")

# Create 
@app.post("/patients/", response_model=schemas.PatientResponse)
def create_patient(patient: schemas.PatientCreate,  db: Session = Depends(get_db)):
    return crud.create_patient(db,patient)


#  read all
@app.get("/patients/", response_model=List[schemas.PatientResponse])
def get_patients( db: Session = Depends(get_db)):
    return crud.get_patients(db)


# read one
@app.get("/patients/{patients_id}", response_model=schemas.PatientResponse)
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = crud.get_patient(db, patient_id)

    if not patient:
        raise HTTPException(status_code=404, detail="patient not found")

    return patient

# update

@app.put("/patients/{patient_id}", response_model=schemas.PatientResponse)
def update_patient(patient_id: int, data: schemas.PatientUpdate, db: Session = Depends(get_db)):
    patient = crud.update_patient(db,patient_id, data)
    if not patient:
        raise HTTPException(status_code=404, detail="patient not found")
    return patient
# delete
@app.delete("/patients/{patient_id}", response_model=schemas.PatientResponse)
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = crud.delete_patient(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="patient not found")
    return patient