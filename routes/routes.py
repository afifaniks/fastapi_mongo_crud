from bson import ObjectId
from fastapi import APIRouter

from config.database import connection
from models.student import Student
from schemas.student import list_student_entity, student_entity

student_router = APIRouter()


@student_router.get("/")
async def index() -> str:
    return "HTTP 200"


@student_router.get("/students")
async def get_students():
    return list_student_entity(connection.local.student.find())


@student_router.get("/students/{student_id}")
async def get_student_by_id(student_id):
    return student_entity(connection.local.student.find_one({"_id": ObjectId(student_id)}))


@student_router.post("/students")
async def create_student(student: Student):
    connection.local.student.insert_one(dict(student))
    return list_student_entity(connection.local.student.find())


@student_router.put("/students/{student_id}")
async def update_student(student_id, student: Student):
    connection.local.student.find_one_and_update(
        {"_id": ObjectId(student_id)},
        {"$set": dict(student)}
    )

    return student_entity(connection.local.student.find_one({"_id": ObjectId(student_id)}))


@student_router.delete("/students/{student_id}")
async def delete_student(student_id):
    connection.local.student.find_one_and_delete(
        {"_id": ObjectId(student_id)}
    )

    return {"DELETED": True}
