from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from models import Student, Faculty, Project
from matching import compute_student_project_score, form_complementary_team

app = FastAPI(title="AI Student-Faculty Matching System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

STUDENTS_DB: List[Student] = []
PROJECTS_DB: List[Project] = []
FACULTY_DB: List[Faculty] = []

@app.get("/")
def home():
    return {"status": "API is online"}

@app.post("/api/students")
def register_student(student: Student):
    STUDENTS_DB.append(student)
    return {"message": "Student registered", "student_id": student.id}

@app.post("/api/projects")
def register_project(project: Project):
    PROJECTS_DB.append(project)
    return {"message": "Project added", "project_id": project.id}

@app.post("/api/recommend/projects")
def recommend_projects(student: Student):
    results = []
    for proj in PROJECTS_DB:
        score = compute_student_project_score(student, proj)
        results.append({
            "project_id": proj.id,
            "title": proj.title,
            "domain": proj.domain,
            "required_skills": proj.required_skills,
            "compatibility_score": score
        })
    results.sort(key=lambda x: x["compatibility_score"], reverse=True)
    return {"recommendations": results}

@app.post("/api/teams/form")
def generate_team(project_id: str, team_size: int = 4):
    target_project = next((p for p in PROJECTS_DB if p.id == project_id), None)
    if not target_project:
        return {"error": "Project not found"}
    return form_complementary_team(target_project, STUDENTS_DB, team_size=team_size)