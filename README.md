# Patients Tracker FASTAPI

A simple **FastAPI** application for managing patient records. The API allows users to create, view, update, and delete patient appointment details.

## Features

* Create a new patient
* Get all patients
* Get a single patient by ID
* Update patient details
* Delete a patient
* SQLite database support
* Automatic API documentation using Swagger UI

## Technologies Used

* Python
* FastAPI
* SQLAlchemy
* Pydantic
* SQLite
* Uvicorn

## Project Structure

```text
Patients_tracker-FASTAPI/
│
├── main.py          # FastAPI application and routes
├── models.py        # SQLAlchemy database model
├── schemas.py       # Pydantic schemas
├── crud.py          # Database CRUD operations
├── database.py      # Database connection setup
├── README.md
└── patient.db       # SQLite database, created automatically
```

## Installation

Clone the repository:

```bash
git clone https://github.com/odoshew-crypto/Patients_tracker-FASTAPI.git
cd Patients_tracker-FASTAPI
```

Create and activate a virtual environment:

```bash
python -m venv patient
```

Activate it on Windows:

```bash
patient\Scripts\activate
```

Install dependencies:

```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

## Running the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## API Documentation

Open Swagger UI in your browser:

```text
http://127.0.0.1:8000/docs
```

Open ReDoc documentation:

```text
http://127.0.0.1:8000/redoc
```

## API Endpoints

| Method | Endpoint                 | Description            |
| ------ | ------------------------ | ---------------------- |
| POST   | `/patients/`             | Create a new patient   |
| GET    | `/patients/`             | Get all patients       |
| GET    | `/patients/{patient_id}` | Get patient by ID      |
| PUT    | `/patients/{patient_id}` | Update patient details |
| DELETE | `/patients/{patient_id}` | Delete patient         |

## Patient Fields

```json
{
  "name": "John Doe",
  "phone": "0712345678",
  "doctor": "Dr. Smith",
  "appointment_date": "2026-06-27",
  "status": "scheduled"
}
```

## Example Request
you can try this
Create a patient:

```bash
curl -X POST "http://127.0.0.1:8000/patients/" \
-H "Content-Type: application/json" \
-d "{\"name\":\"John Doe\",\"phone\":\"0712345678\",\"doctor\":\"Dr. Smith\",\"appointment_date\":\"2026-06-27\",\"status\":\"scheduled\"}"
```
-Deployed the project using Render tool and the project is live in public and can be accessed through this URL  https://patients-tracker-fastapi-1.onrender.com
## Author

Created by **odoshew-crypto**.

