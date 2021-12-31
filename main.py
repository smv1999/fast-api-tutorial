from fastapi import FastAPI, Path

app = FastAPI()

students = {
    1: {
        "name": "Rahul",
        "age": 17,
        "class": "12th"
    },
    2: {
        "name": "Rakshan",
        "age": 15,
        "class": "10th"
    }
}


@app.get("/")
def index():
    return {"name": "Ayush"}


@app.get("/get-students/{student_id}")
def get_students(student_id: int = Path(None, description="The ID of the student you want to view", gt=0)):
    return students[student_id] if student_id in students else {"error": "The data for ID {} is not present".format(student_id)}


@app.get("/get-by-name")
def get_students(name: str = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not Found"}


@app.get("/get-students/")
def get_students():
    return students
