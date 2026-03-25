# 📘 FastAPI + PostgreSQL (Docker) — Development environment

This project uses:

- **FastAPI** (backend)
- **SQLAlchemy** (ORM)
- **PostgreSQL in Docker** (database)

This guide shows how to get everything running locally.

---

## 🚀 1. Start PostgreSQL (Docker)

Ensure Docker Desktop is running.

Start the database:

```bash
docker run --name recipes-db \
    -e POSTGRES_PASSWORD=dev \
    -e POSTGRES_USER=dev \
    -e POSTGRES_DB=recipes \
    -p 5432:5432 \
    -d postgres
```

Check if the database is running: 

```bash
docker ps
```

## 📦 2. Install Python dependencies
Create and activate a virtual environment.


```Powershell
python -m venv venv
venv\Scripts\activate
```

```bash
python -m venv venv 
source venv/bin/activate 
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🛠 3. Configure Alembic
Make sure your alembic.ini contains the correct database URL:

```
sqlalchemy.url = postgresql+psycopg://dev:dev@localhost:5432/recipes
```

## 🔄 4. Run database migrations
Upgrade the database to the latest version:

```bash
alembic upgrade head
```
Generate a new migration (if you change models):
```bash 
alembic revision --autogenerate -m "Describe your change"
```

## ▶️ 5. Start the FastAPI server
Run the development server:

```bash
uvicorn app.main:app --reload
```

The API will be available at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🧪 6. Testing the API
Once the server is running, open:

```
http://localhost:8000/docs
```

You can test all endpoints directly in the browser.

## 🧹 7. Stopping and cleaning up Docke
Stop the database:

```bash
docker stop recipes-db
```

Remove the container:

```bash
docker rm recipes-db
```

##🧩 Troubleshooting
Database connection errors
Make sure the container is running:

```bash
docker ps
```


## Virtual environment not activating
Use the correct command for your shell:
- PowerShell: venv\Scripts\activate
- Git Bash: source venv/Scripts/activate

## Migrations not applying
Check that your models are imported in app/db/base.py.
