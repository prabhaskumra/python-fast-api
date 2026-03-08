# Quick Start Guide

## 🚀 Run the Project (3 Easy Steps)

### Option 1: VS Code Debug (Recommended)

1. **Start databases**:
   ```bash
   docker-compose up -d postgres redis
   ```

2. **In VS Code**: Press `F5` → Select "All Services (Compound)"

3. **Access APIs**:
   - Code Analysis: http://localhost:8001/docs
   - AI Assistant: http://localhost:8002/docs

---

### Option 2: Command Line

1. **Start all services with Docker Compose**:
   ```bash
   docker-compose up
   ```

2. **Access APIs**:
   - Code Analysis: http://localhost:8001/docs
   - AI Assistant: http://localhost:8002/docs

---

## 📝 Test the APIs

### Code Analysis Service (Port 8001)

```bash
# Health check
curl http://localhost:8001/

# Analyze code
curl -X POST http://localhost:8001/analyze \
  -H "Content-Type: application/json" \
  -d '{"code": "def hello():\n    return \"world\"", "language": "python"}'
```

### AI Assistant Service (Port 8002)

```bash
# Health check
curl http://localhost:8002/

# Explain code
curl -X POST http://localhost:8002/explain \
  -H "Content-Type: application/json" \
  -d '{"code": "def add(a, b):\n    return a + b", "language": "python"}'
```

---

## 🛑 Stop Everything

```bash
# Stop services
docker-compose down

# Stop services and remove volumes (clean slate)
docker-compose down -v
```

---

## 📚 Interactive API Documentation

Once services are running, visit:
- **Code Analysis**: http://localhost:8001/docs
- **AI Assistant**: http://localhost:8002/docs

FastAPI automatically generates interactive Swagger UI where you can test all endpoints!

---

## 🐛 Debugging in VS Code

1. Set breakpoints in your code (click left of line number)
2. Press `F5` → Select service to debug
3. Make API request (use `/docs` or curl)
4. Code will pause at breakpoint
5. Inspect variables, step through code, etc.

**Just like Visual Studio debugging!**

---

## 📖 More Info

- Full setup guide: [documents/setup.md](documents/setup.md)
- Project goals: [documents/project-goal.md](documents/project-goal.md)
- Current progress: [documents/progress.md](documents/progress.md)
