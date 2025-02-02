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
}

@app.get("/api")
def get_marks(names: str = ""):
    if names:
        names_list = names.split(",")
        marks = [marks_data.get(n.strip(), "Not Found") for n in names_list]
        return JSONResponse(content={"marks": marks})
    return JSONResponse(content={"message": "Please provide student names"}, status_code=400)
