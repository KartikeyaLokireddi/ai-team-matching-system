from typing import List, Dict, Any
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from models import Student, Faculty, Project

model = SentenceTransformer("all-MiniLM-L6-v2")

def compute_student_project_score(student: Student, project: Project) -> float:
    student_text = f"{student.bio} Skills: {', '.join(student.skills)}. Interests: {', '.join(student.interests)}."
    project_text = f"{project.title}: {project.description}. Domain: {project.domain}."
    
    emb_student = model.encode([student_text])
    emb_project = model.encode([project_text])
    semantic_sim = float(cosine_similarity(emb_student, emb_project)[0][0])

    student_skills_set = {s.lower() for s in student.skills}
    project_skills_set = {s.lower() for s in project.required_skills}
    skill_overlap = len(student_skills_set.intersection(project_skills_set))
    skill_score = skill_overlap / len(project_skills_set) if project_skills_set else 0.0

    learning_goals_set = {g.lower() for g in student.learning_goals}
    learn_overlap = len(learning_goals_set.intersection(project_skills_set))
    learning_score = learn_overlap / len(project_skills_set) if project_skills_set else 0.0

    total_score = (0.40 * skill_score) + (0.35 * max(0.0, semantic_sim)) + (0.25 * learning_score)
    return round(total_score, 4)

def form_complementary_team(project: Project, candidates: List[Student], team_size: int = 4) -> Dict[str, Any]:
    required = set(s.lower() for s in project.required_skills)
    covered = set()
    selected_team = []
    pool = list(candidates)

    while len(selected_team) < team_size and pool:
        best_candidate = None
        best_new_coverage = -1

        for student in pool:
            s_skills = set(s.lower() for s in student.skills)
            uncovered_overlap = len((s_skills.intersection(required)) - covered)
            if uncovered_overlap > best_new_coverage:
                best_new_coverage = uncovered_overlap
                best_candidate = student

        if best_candidate and best_new_coverage > 0:
            selected_team.append(best_candidate)
            covered.update(set(s.lower() for s in best_candidate.skills).intersection(required))
            pool.remove(best_candidate)
        else:
            pool.sort(key=lambda s: compute_student_project_score(s, project), reverse=True)
            if pool:
                selected_team.append(pool.pop(0))

    skill_gaps = list(required - covered)
    return {
        "project_id": project.id,
        "project_title": project.title,
        "team": [{"id": s.id, "name": s.name, "skills": s.skills} for s in selected_team],
        "covered_skills": list(covered),
        "skill_gaps": skill_gaps,
        "gap_warning": f"Missing skills: {', '.join(skill_gaps)}" if skill_gaps else "Complete coverage."
    }