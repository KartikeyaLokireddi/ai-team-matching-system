import requests

BASE_URL = "http://127.0.0.1:8000"

# 1. Register a faculty project requiring diverse skills
project_data = {
    "id": "proj-101",
    "title": "Smart Agriculture Disease Detection & Cloud Analytics",
    "domain": "AI / Cloud",
    "description": "An end-to-end platform featuring computer vision for crop leaf disease detection, a React frontend dashboard, Node.js API, and AWS cloud deployment.",
    "required_skills": ["Python", "Machine Learning", "React", "Node.js", "AWS"]
}
r = requests.post(f"{BASE_URL}/api/projects", json=project_data)
print("Create Project:", r.json())

# 2. Register students with complementary skills
students = [
    {
        "id": "s1",
        "name": "Student A",
        "skills": ["React", "CSS", "JavaScript"],
        "interests": ["Frontend Development", "UI/UX"],
        "learning_goals": ["Node.js"],
        "career_goal": "Frontend Developer",
        "bio": "Experienced building responsive web apps with React."
    },
    {
        "id": "s2",
        "name": "Student B",
        "skills": ["Python", "Machine Learning", "OpenCV"],
        "interests": ["Computer Vision", "Deep Learning"],
        "learning_goals": ["Cloud"],
        "career_goal": "AI/ML Engineer",
        "bio": "Trained CNN models for image classification in Python."
    },
    {
        "id": "s3",
        "name": "Student C",
        "skills": ["Node.js", "Express", "MongoDB"],
        "interests": ["Backend Systems", "APIs"],
        "learning_goals": ["System Architecture"],
        "career_goal": "Backend Developer",
        "bio": "Built REST APIs using Express and Node."
    },
    {
        "id": "s4",
        "name": "Student D",
        "skills": ["AWS", "Docker", "Linux"],
        "interests": ["DevOps", "Cloud Computing"],
        "learning_goals": ["Kubernetes"],
        "career_goal": "Cloud Architect",
        "bio": "Hands-on with AWS EC2, S3, and containerized Docker apps."
    }
]

for s in students:
    res = requests.post(f"{BASE_URL}/api/students", json=s)
    print(f"Registered {s['name']}:", res.json())

# 3. Test Complementary Team Formation
print("\n--- Testing Team Formation ---")
team_res = requests.post(f"{BASE_URL}/api/teams/form?project_id=proj-101&team_size=4")
print("Team Formation Output:")
import json
print(json.dumps(team_res.json(), indent=2))