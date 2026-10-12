from pydantic import BaseModel
from typing import List, Optional

class Student(BaseModel):
    id: str
    name: str
    skills: List[str]
    interests: List[str]
    learning_goals: List[str]
    career_goal: str
    bio: str

class Faculty(BaseModel):
    id: str
    name: str
    expertise: List[str]
    research_domains: List[str]
    mentoring_topics: List[str]
    bio: str

class Project(BaseModel):
    id: str
    title: str
    domain: str
    description: str
    required_skills: List[str]
    faculty_id: Optional[str] = None
