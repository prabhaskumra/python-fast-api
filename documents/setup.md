# Development Setup Guide

## Prerequisites

### Required Software
- **Python 3.11+** - [Download](https://www.python.org/downloads/)
- **Docker Desktop** - [Download](https://www.docker.com/products/docker-desktop)
- **VS Code** - [Download](https://code.visualstudio.com/)
- **Git** - Already installed on macOS

### Verify Installations
```bash
python --version    # Should be 3.11+
docker --version
git --version
```

---

## First Time Setup

### 1. Clone Repository (if not already)
```bash
git clone <repo-url>
cd python-fast-api
```

### 2. Create Virtual Environment
```bash
# Create venv
python -m venv venv

# Activate (macOS/Linux)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Verify
which python  # Should point to venv/bin/python
```

### 3. Install Dependencies (when requirements.txt exists)
```bash
pip install -r services/code-analysis/requirements.txt
pip install -r services/ai-assistant/requirements.txt

# Or install dev dependencies
pip install -r requirements-dev.txt  # If exists
```

### 4. Environment Variables

Create `.env` files for each service:

**services/code-analysis/.env**
```env
DATABASE_URL=postgresql://user:password@localhost:5432/code_analysis
ENVIRONMENT=development
LOG_LEVEL=DEBUG
```

**services/ai-assistant/.env**
```env
DATABASE_URL=postgresql://user:password@localhost:5432/ai_assistant
REDIS_URL=redis://localhost:6379/0
ANTHROPIC_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here  # Optional
ENVIRONMENT=development
LOG_LEVEL=DEBUG
```

**Root .env** (for Docker Compose)
```env
POSTGRES_USER=devuser
POSTGRES_PASSWORD=devpassword
REDIS_PASSWORD=redispassword
```

---

## Running the Project

### Option 1: VS Code Debug (Recommended for Development) 🎯
**This is like running with F5 in Visual Studio!**

1. **Start dependencies** (PostgreSQL + Redis):
   ```bash
   docker-compose up postgres redis
   ```

2. **In VS Code**:
   - Press `F5` or click Run & Debug icon
   - Select service from dropdown:
     - "Code Analysis Service" - Run service 1
     - "AI Assistant Service" - Run service 2
     - "All Services (Compound)" - Run both at once
   - Set breakpoints, inspect variables, step through code

3. **Access APIs**:
   - Code Analysis: http://localhost:8001/docs
   - AI Assistant: http://localhost:8002/docs

**Benefits**:
- ✅ Full debugging support (breakpoints, watch, call stack)
- ✅ Auto-reload on code changes
- ✅ Environment variables loaded from `.env`
- ✅ Just like .NET debugging experience!

---

### Option 2: Docker Compose (Full Stack)
```bash
# Start all services (APIs + Databases)
docker-compose up

# Start in detached mode
docker-compose up -d

# View logs
docker-compose logs -f

# Stop all services
docker-compose down

# Rebuild after code changes
docker-compose up --build
```

---

### Option 3: Command Line (Manual)
```bash
# Terminal 1: Start PostgreSQL + Redis
docker-compose up postgres redis

# Terminal 2: Code Analysis Service
cd services/code-analysis
source ../../venv/bin/activate
uvicorn app.main:app --reload --port 8001

# Terminal 3: AI Assistant Service
cd services/ai-assistant
source ../../venv/bin/activate
uvicorn app.main:app --reload --port 8002
```

---

## Database Migrations

### Initial Setup (first time only)
```bash
cd services/code-analysis

# Initialize Alembic
alembic init alembic

# Create first migration
alembic revision --autogenerate -m "Initial migration"

# Apply migration
alembic upgrade head
```

### Regular Migrations (after model changes)
```bash
# Generate migration
alembic revision --autogenerate -m "Description of changes"

# Apply migration
alembic upgrade head

# Rollback last migration
alembic downgrade -1

# View migration history
alembic history
```

Repeat for `services/ai-assistant/`

---

## VS Code Configuration

### Recommended Extensions
- Python (Microsoft)
- Pylance
- Docker
- PostgreSQL (Chris Kolkman)
- Redis (Dunn)

### Workspace Settings (.vscode/settings.json)
```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "python.testing.pytestEnabled": true
}
```

### Launch Configuration (.vscode/launch.json)

**This allows you to run/debug each service from VS Code (like .NET launch settings)**

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Code Analysis Service",
      "type": "python",
      "request": "launch",
      "module": "uvicorn",
      "args": [
        "app.main:app",
        "--reload",
        "--host", "0.0.0.0",
        "--port", "8001"
      ],
      "cwd": "${workspaceFolder}/services/code-analysis",
      "env": {
        "PYTHONPATH": "${workspaceFolder}/services/code-analysis"
      },
      "envFile": "${workspaceFolder}/services/code-analysis/.env",
      "console": "integratedTerminal",
      "justMyCode": true
    },
    {
      "name": "AI Assistant Service",
      "type": "python",
      "request": "launch",
      "module": "uvicorn",
      "args": [
        "app.main:app",
        "--reload",
        "--host", "0.0.0.0",
        "--port", "8002"
      ],
      "cwd": "${workspaceFolder}/services/ai-assistant",
      "env": {
        "PYTHONPATH": "${workspaceFolder}/services/ai-assistant"
      },
      "envFile": "${workspaceFolder}/services/ai-assistant/.env",
      "console": "integratedTerminal",
      "justMyCode": true
    },
    {
      "name": "All Services (Compound)",
      "type": "compound",
      "configurations": [
        "Code Analysis Service",
        "AI Assistant Service"
      ],
      "presentation": {
        "hidden": false,
        "group": "microservices",
        "order": 1
      }
    }
  ]
}
```

**Usage**:
- Press `F5` or go to Run & Debug panel
- Select service from dropdown (Code Analysis, AI Assistant, or All Services)
- Set breakpoints in your code
- Debug just like .NET in Visual Studio!

**Compound Configuration**: Select "All Services" to run both microservices at once (like running multiple projects in Visual Studio)

---

## Testing

### Run Tests
```bash
# All tests
pytest

# Specific service
cd services/code-analysis
pytest

# With coverage
pytest --cov=app --cov-report=html
```

### Run Linting
```bash
# Using /lint command (Claude Code)
/lint

# Manual
ruff check .
black --check .
mypy app/
```

---

## Useful Commands

### Python Package Management
```bash
# Install new package
pip install package-name

# Update requirements.txt
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt
```

### Docker
```bash
# View running containers
docker ps

# Access container shell
docker exec -it <container_name> bash

# View logs for specific service
docker-compose logs -f code-analysis

# Rebuild specific service
docker-compose up --build code-analysis
```

### Database
```bash
# Connect to PostgreSQL (from host)
psql -h localhost -U devuser -d code_analysis

# Connect to PostgreSQL (from Docker)
docker-compose exec postgres psql -U devuser -d code_analysis

# Connect to Redis
docker-compose exec redis redis-cli
```

---

## Troubleshooting

### Port Already in Use
```bash
# Find process using port 8001
lsof -i :8001

# Kill process
kill -9 <PID>
```

### Database Connection Issues
- Verify PostgreSQL is running: `docker-compose ps`
- Check `.env` file has correct credentials
- Ensure database exists: `docker-compose exec postgres psql -U devuser -l`

### Virtual Environment Not Activating
- Delete `venv/` folder and recreate: `rm -rf venv && python -m venv venv`
- Ensure using correct Python version: `python --version`

---

## API Documentation

Once services are running:

- **Code Analysis Service**: http://localhost:8001/docs
- **AI Assistant Service**: http://localhost:8002/docs

FastAPI auto-generates interactive Swagger UI documentation.

---

## Notes

- Always activate venv before working: `source venv/bin/activate`
- Keep requirements.txt updated when adding dependencies
- Run migrations before starting services if models changed
- Use Docker Compose for consistent environment
