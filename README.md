# Python FastAPI Enterprise Microservices

## Overview
This is an enterprise-grade microservices project built with Python and FastAPI, designed to demonstrate production-ready patterns and best practices. The project serves as a learning platform for transitioning from .NET (5 years experience with Azure Functions, Visual Studio, and EF Core) to Python backend development.

## Learning Objectives
- Master FastAPI for building modern Python backend services
- Understand microservices architecture in Python
- Learn Python equivalents of .NET tools and frameworks
- Implement database migrations and ORM patterns

## Tech Stack Mapping: .NET → Python

| .NET Experience | Python Equivalent |
|----------------|-------------------|
| **Azure Functions** | Azure Functions (Python), AWS Lambda |
| **Visual Studio / launch.json** | VS Code with Python debugger, launch.json configurations |
| **EF Core** | SQLAlchemy (ORM), Tortoise ORM |
| **EF Migrations** | Alembic (database migrations) |
| **ASP.NET Core** | FastAPI, Flask |
| **Dependency Injection** | FastAPI's dependency injection system |
| **appsettings.json** | Environment variables, .env files, pydantic-settings |

## Tech Stack

### Core Framework
- **FastAPI** - Modern, fast web framework for building APIs
- **Uvicorn** - ASGI server for running FastAPI applications

### Database & ORM
- **SQLAlchemy** - SQL toolkit and ORM
- **Alembic** - Database migration tool
- **PostgreSQL/MySQL/SQLite** - Database options

### Additional Libraries
- **Pydantic** - Data validation using Python type hints
- **pydantic-settings** - Application configuration management
- **python-dotenv** - Environment variable management
- **pytest** - Testing framework
- **httpx** - Async HTTP client for testing

## Project Goals
- Build enterprise-grade microservices architecture
- Implement proper database migrations and data management
- Apply industry best practices and design patterns
- Create production-ready, scalable, and maintainable code
- Follow clean architecture and SOLID principles

## Getting Started

**Quick Start**: See [QUICKSTART.md](QUICKSTART.md) for immediate setup instructions.

**Full Setup Guide**: See [documents/setup.md](documents/setup.md) for detailed environment setup.

### Running the Services

```bash
# Start databases
docker-compose up -d postgres redis

# In VS Code: Press F5 → Select "All Services (Compound)"
# Or run manually:
# Terminal 1: cd services/code-analysis && uvicorn app.main:app --reload --port 8001
# Terminal 2: cd services/ai-assistant && uvicorn app.main:app --reload --port 8002
```

**Access APIs**:
- Code Analysis: http://localhost:8001/docs
- AI Assistant: http://localhost:8002/docs

## Project Structure

```
python-fast-api/
├── services/
│   ├── code-analysis/              # Service 1: Code Analysis
│   │   ├── app/
│   │   │   ├── main.py            # FastAPI application
│   │   │   ├── models/            # SQLAlchemy models
│   │   │   ├── routes/            # API routes
│   │   │   ├── services/          # Business logic
│   │   │   └── db/                # Database config
│   │   ├── tests/
│   │   ├── requirements.txt
│   │   ├── Dockerfile
│   │   └── .env
│   │
│   └── ai-assistant/              # Service 2: AI Code Assistant
│       ├── app/
│       │   ├── main.py            # FastAPI application
│       │   ├── models/            # SQLAlchemy models
│       │   ├── routes/            # API routes
│       │   ├── services/          # Business logic
│       │   └── db/                # Database config
│       ├── tests/
│       ├── requirements.txt
│       ├── Dockerfile
│       └── .env
│
├── documents/                      # Project documentation
│   ├── project-goal.md            # Project objectives
│   ├── architecture.md            # Architecture decisions
│   ├── setup.md                   # Development setup
│   ├── decisions.md               # Decision log
│   └── progress.md                # Progress tracker
│
├── .vscode/
│   ├── launch.json                # VS Code debug configs
│   └── settings.json              # Python settings
│
├── .claude/                       # Claude Code agent tools
│   ├── commands/                  # Slash commands
│   └── hooks/                     # Git hooks
│
├── venv/                          # Python virtual environment
├── docker-compose.yml             # Docker services config
├── .env                           # Environment variables
├── .gitignore
├── README.md                      # This file
└── QUICKSTART.md                  # Quick start guide
```

## Current Status

**Phase 1 (MVP)**: ✅ Complete
- Both services running with basic endpoints
- Docker Compose configured for PostgreSQL + Redis
- VS Code debugging configured
- Interactive API documentation at `/docs`

**Next**: Phase 2 - Database integration, real code analysis, LLM integration

See [documents/progress.md](documents/progress.md) for detailed progress.
