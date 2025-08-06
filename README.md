# 3-Tier Python Web Application

This is a containerized 3-tier application consisting of:

**Frontend** – Python-based UI
- **Backend** – Flask API
- **Database** – PostgreSQL
- **Monitoring** – Postgres Exporter (Prometheus-compatible)

---

## 📁 Project Structure

3-tier-python-app/
├── Backend/
│ └── api.py
├── Frontend/
│ └── app.py
├── db_pass.txt
├── docker-compose.yml


---

## ⚙️ Services Overview

| Service           | Port      | Description                        |
|-------------------|-----------|------------------------------------|
| Frontend          | `3000`    | Simple Python UI                   |
| Backend (Flask)   | `5050`    | Exposes REST API `/api`            |
| PostgreSQL        | `5432`    | Database service                   |
| Postgres Exporter | `9187`    | Prometheus metrics exporter        |

---

## 🚀 Getting Started

### 1. Clone Repository

git clone https://github.com/your-username/3-tier-python-app.git
cd 3-tier-python-app
2. Create the DB Secret File
bash
Copy
Edit
echo "your_postgres_password" > db_pass.txt

🌐 Application Endpoints
Component	URL
Frontend UI	http://localhost:3000
Backend API	http://localhost:5050/api
Prometheus Exporter	http://localhost:9187
