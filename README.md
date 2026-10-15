# AI-Assisted Student-Faculty Guidance & Team Formation System

An intelligent platform designed to automate balanced, complementary team formation for academic projects and pair teams with suitable faculty mentors using semantic embeddings and NLP.

---

## 📌 Project Overview

Manual team formation often results in unbalanced groups with overlapping skill sets or isolated domain gaps. This system analyzes student skill profiles, technical strengths, and project interests using sentence embeddings to form diverse, high-performing teams, while aligning them with faculty research domains.

---

## 🚀 Current Features

- **Semantic Profiling:** Converts free-form student skills and project interests into high-dimensional vector representations using `all-MiniLM-L6-v2`.
- **Complementary Matching:** Uses clustering and similarity metrics (`scikit-learn`) to balance diverse technical skill sets across teams.
- **FastAPI Backend:** High-performance REST API endpoints for profile ingestion and team allocation generation.
- **Interactive UI Prototype:** Lightweight frontend built with HTML and Tailwind CSS to test input profiles and inspect generated groups.
- **Codespaces Ready:** Configured to run directly in GitHub Codespaces with zero local environment setup.

---

## 🛠️ Tech Stack

- **Backend:** Python 3.10+, [FastAPI](https://fastapi.tiangolo.com/), Uvicorn
- **Machine Learning & NLP:** [Sentence-Transformers](https://sbert.net/) (`all-MiniLM-L6-v2`), [scikit-learn](https://scikit-learn.org/), NumPy
- **Frontend:** HTML5, Tailwind CSS, JavaScript (Fetch API)
- **Database (Planned):** PostgreSQL with SQLAlchemy
- **Environment:** GitHub Codespaces / Local venv

---

## 📂 Repository Structure

```text
ai-team-matching-system/
├── app/
│   ├── main.py              # FastAPI app initialization and routing
│   ├── matching.py          # Embedding generation & team formation logic
│   ├── models.py            # Pydantic data schemas
│   └── static/
│       ├── index.html       # Prototype UI
│       └── app.js           # Client-side API calls
├── requirements.txt         # Project dependencies
└── README.md
