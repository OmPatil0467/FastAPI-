from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"]
)

# Load student marks
def load_marks():
    json_path = os.path.join(os.path.dirname(__file__), "../q-vercel-python.json")
    with open(json_path, "r") as file:
        data = json.load(file)
    return {student["name"]: student["marks"] for student in data}

marks_data = load_marks()

@app.get("/api")
def get_marks(name: list[str]):
    return {"marks": [marks_data.get(n, None) for n in name]}
