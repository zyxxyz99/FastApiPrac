from fastapi import datastructures
from typing import Optional
import fastapi

from fastapi import FastAPI,Path
from pydantic import BaseModel

app = FastAPI() 

students = {
    1:{
        "Name": "John",
        "Age":22,
        "Major": "CS"
    }
}

class Student(BaseModel):
    name : str
    age : int
    year : int 

class UpdateStud(BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None
    year : Optional[int] = None

@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/get-student/{student_id}")
def getst(student_id: int = Path(description="The ID of the student to retrieve", gt=0, lt=3)):
    if student_id not in students:
        return {"error": "Student not found"}
    return students[student_id]

@app.get("/get-name")
def stname(name : str):
    for stid in students:
        if students[stid]["Name"] == name:
            return students[stid]
    return {"error": "Student not found"}

@app.post("/create-student/{student_id}") 
def create_stud(student_id : int, student : Student):
    if student_id in students: 
        return {"error" : "Student already exists"}

    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def upd_std(student_id : int, student : UpdateStud):
    if student_id not in students:
        return {"error":"Student doesnt exist"}
    
    if student.name != None:
        students[student_id].name = student.name 
    if student.age != None:
        students[student_id].age = student.age 
    if student.year != None: 
        students[student_id].year = student.year 
    
    return students[student_id]

@app.delete("/del-stud/{students_id}")
def del_st(student_id : int):
    if student_id not in students:
        return {"Error":"Student doesnt exist"}
    
    del students[student_id]
    return {"Success":"Deleted successfully"}