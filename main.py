from fastapi import FastAPI, Path
from typing import Optional


# uvicorn myapi:app --reload 

app = FastAPI()

students = {
    1: {
        "name": "John",
        "age": 17,
        "class": "12th"
    },
    2: {
        "name": "Peter",
        "age": 15,
        "class": "10th"
    }
}


@app.get("/")
def index():
    return {"name": "First Data"}


@app.get("/get-students/{student_id}")
def get_students(student_id: int = Path(None, description="The ID of the student you want to view", gt=0)):
    return students[student_id]


@app.get("/get-by-name")
def get_students(*, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not Found"}


@app.get("/get-students/")
def get_students():
    return students

@app.get("/sample")
def get_sample():
    return "Sample Output"

