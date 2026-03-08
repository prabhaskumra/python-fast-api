# Project Goal

## Overview
Build an **enterprise-grade AI-powered Developer Tools Platform** with 2 microservices to learn Python backend development, transitioning from .NET/C# background.

---

## Microservices

### **Service 1: Code Analysis Service**
**Purpose**: Static code analysis, security scanning, quality metrics

**Key Features**:
- Parse Python code using AST (Abstract Syntax Tree)
- Security vulnerability scanning (bandit)
- Code complexity metrics (radon)
- Code quality analysis (pylint, flake8)
- Store analysis history in database

**Tech Stack**:
- FastAPI
- SQLAlchemy + Alembic (migrations)
- Built-in `ast` library
- `bandit`, `radon`, `pylint`
- PostgreSQL

**API Endpoints**:
- `POST /analyze` - Analyze code snippet
- `GET /reports/{project_id}` - Get analysis report
- `GET /metrics/{project_id}/trends` - Quality trends over time
- `POST /scan/security` - Security scan

---

### **Service 2: AI Code Assistant Service**
**Purpose**: AI-powered code explanation, completion, and assistance

**Key Features**:
- Code explanation (natural language)
- Generate unit tests
- Code completion suggestions
- Refactoring suggestions
- Bug fixing assistance
- Convert code Python ↔ C#

**Tech Stack**:
- FastAPI
- Anthropic Claude API / OpenAI GPT-4
- Redis (LLM response caching)
- SQLAlchemy + Alembic
- PostgreSQL

**API Endpoints**:
- `POST /explain` - Explain code snippet
- `POST /complete` - Code completion
- `POST /generate/tests` - Generate unit tests
- `POST /refactor` - Refactoring suggestions
- `POST /fix` - Fix bugs
- `POST /translate` - Convert Python ↔ C#

---

## Learning Objectives

### Python Skills
- FastAPI framework (REST APIs)
- SQLAlchemy ORM + Alembic migrations
- AST parsing and code introspection
- LLM API integration (Anthropic/OpenAI)
- Redis caching
- Async Python patterns
- Code analysis libraries

### Enterprise Patterns
- Microservices architecture
- Service-to-service communication
- Database per service pattern
- API authentication & authorization
- Error handling and logging
- Docker containerization
- Local dev environment (Docker Compose)

### .NET → Python Mapping
- EF Core → SQLAlchemy + Alembic
- ASP.NET Core → FastAPI
- Azure Functions → Celery (if needed)
- Dependency Injection → FastAPI DI
- appsettings.json → pydantic-settings + .env

---

## Development Approach

### Phase 1: MVP (Start Simple)
1. Basic FastAPI setup for both services
2. Single endpoint per service (minimal functionality)
3. Docker Compose for local dev
4. Prove architecture works

### Phase 2: Core Features
1. Add database (SQLAlchemy + Alembic)
2. Implement main endpoints
3. Add Redis caching
4. Error handling

### Phase 3: Polish
1. Authentication
2. Logging and monitoring
3. Unit tests (pytest)
4. Documentation

---

## Success Criteria
- 2 independent microservices running locally
- Database migrations working (Alembic)
- AI service successfully calls LLM APIs
- Code analysis service parses and analyzes Python code
- Docker Compose runs both services + databases + Redis
- Clean architecture, production-ready code
