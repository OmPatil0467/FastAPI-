from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins to make requests
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# Sample marks data for students
marks_data = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 92,
    "Eve": 88,
    # Add more students and marks as needed
}

@app.get("/api")
def get_marks(name: str = None):
    if name:
        names = name.split(",")
        marks = [marks_data.get(n, "Not Found") for n in names]
        return JSONResponse(content={"marks": marks})
    return {"message": "Please provide student names"}
