# 🧠 Research Assistant AI

A Django-based backend for uploading, storing, and summarizing research papers using AI.

---

## 🚀 Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/your-username/research-assistant-ai.git
cd research-assistant-ai
2. Create Virtual Environment
bash
Copy code
# Create venv
python -m venv .venv

# Activate venv
# On Linux/Mac:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Apply Migrations
bash
Copy code
python manage.py migrate
5. Run Development Server
bash
Copy code
python manage.py runserver
Now your backend should be running 🎉

🌐 API Endpoints
Endpoint	Method	Description
/api/papers/	GET	List all papers
/api/papers/	POST	Upload a new paper
/api/papers/{id}/	GET	Retrieve details of a paper
/admin/	-	Django admin panel

🛠 Tech Stack
Python 3.10+

Django 5.x

Django REST Framework (DRF)

Database: SQLite (default), PostgreSQL recommended for production
