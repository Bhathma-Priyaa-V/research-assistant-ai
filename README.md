# 📚 Research Assistant AI - Backend

This is the **backend service** for a Research Assistant AI project.  
It is built with **Django** and **Django REST Framework (DRF)** to handle:

- Uploading **research papers** (PDFs, docs, etc.)  
- Extracting and storing **text, summaries, and metadata**  
- Providing **REST API endpoints** for integration with frontends or other services  

---

## 🚀 Features
- 📂 Upload and manage research papers  
- 🔑 Securely handle metadata (UUID, checksums)  
- 📝 JSON summaries for flexible storage  
- ⏱ Automatic timestamps for tracking uploads  
- 🌐 REST API for easy frontend/backend communication  

---

## 🔧 Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/your-username/research-assistant-ai.git
cd research-assistant-ai


### 2. Create Virtual Environment
```bash
# Create venv
python -m venv .venv  

# Activate venv
# On Linux/Mac:
source .venv/bin/activate  
# On Windows:
.venv\Scripts\activate


### 3. Install Dependencies
```bash
pip install -r requirements.txt

---

### 4. Apply Migrations
```bash
python manage.py migrate

---

### 5. Run Development Server
```bash
python manage.py runserver

---

Now your backend should be running.

---

## 🌐 API Endpoints

| Endpoint            | Method | Description                 |
|---------------------|--------|-----------------------------|
| `/api/papers/`      | GET    | List all papers             |
| `/api/papers/`      | POST   | Upload a new paper          |
| `/api/papers/{id}/` | GET    | Retrieve details of a paper |
| `/admin/`           | -      | Django admin panel          |

---

## ⚙️ Tech Stack

- Python 3.10+

- Django 5.x

- Django REST Framework (DRF)

- SQLite (default), PostgreSQL recommended for production

