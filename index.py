from fastapi import FastAPI

from routes.routes import student_router

app = FastAPI()
app.include_router(student_router)
