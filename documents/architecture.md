# Architecture Decisions

## Service Architecture

### Service Count: 2 Microservices
**Decision**: Build 2 services instead of original 3
**Reason**: Repository Service (Git operations, dependency management) deemed too complex for initial Python learning. Focus on core capabilities: AI integration and code analysis.
**Services**:
1. Code Analysis Service - Static analysis, security scanning, metrics
2. AI Code Assistant Service - LLM-powered code assistance

---

## Technology Choices

### Web Framework: FastAPI
**Why**:
- Modern async support (better than Flask)
- Automatic OpenAPI/Swagger documentation
- Type hints and Pydantic validation (similar to C# strongly-typed models)
- Excellent performance
- Best documentation in Python ecosystem

**Alternative Considered**: Flask (too basic, no async support)

---

### Database: PostgreSQL
**Why**:
- Production-grade, enterprise-ready
- Familiar from .NET development
- Excellent SQLAlchemy support
- Can use separate DBs per service for true microservices isolation

**Alternative Considered**: SQLite (not production-ready), MySQL (PostgreSQL more feature-rich)

---

### ORM: SQLAlchemy + Alembic
**Why**:
- SQLAlchemy is the closest Python equivalent to EF Core
- Alembic provides migrations (like EF migrations)
- Industry standard, battle-tested
- Supports async operations

**Alternative Considered**: Tortoise ORM (less mature), Django ORM (requires Django framework)

---

### Caching: Redis
**Why**:
- Fast in-memory caching for LLM responses (reduce API costs)
- Can also serve as message broker if needed later
- Industry standard
- Simple key-value operations

**Alternative Considered**: Memcached (Redis more versatile)

---

### LLM Provider: Anthropic Claude + OpenAI (optional)
**Why**:
- Claude: Excellent code understanding, longer context
- OpenAI: GPT-4 as alternative/comparison
- Both have simple Python SDKs

---

### Code Analysis Libraries
- **ast** (built-in): Python AST parsing, zero dependencies
- **bandit**: Security vulnerability scanning
- **radon**: Code complexity metrics (cyclomatic complexity, maintainability index)
- **pylint**: Code quality analysis

**Why**: All are industry-standard, well-documented, actively maintained

---

## Development Environment

### Containerization: Docker + Docker Compose
**Why**:
- Consistent dev environment across machines
- Easy to run all services + dependencies (PostgreSQL, Redis)
- Familiar from .NET/Azure background

### IDE: VS Code
**Why**:
- Excellent Python extension
- Multi-root workspace support for microservices
- Debugging support for multiple services
- Familiar from .NET development

---

## Database Strategy

### Option A: Single PostgreSQL, Multiple Schemas (Chosen for now)
- Simple local dev setup
- Easy to start with
- Can split to separate DBs later

### Option B: Separate PostgreSQL per Service
- True microservices isolation
- More complex Docker Compose setup
- Migration path for later if needed

**Decision**: Start with Option A, migrate to Option B in Phase 3 if needed

---

## Communication Pattern

### Service-to-Service: REST APIs (for now)
- Simple HTTP calls between services
- Can add gRPC later if performance needed

**Future Consideration**: Message queue (RabbitMQ, Kafka) for async operations

---

## Authentication (Phase 3)
- JWT tokens (similar to .NET Identity)
- FastAPI dependency injection for auth middleware
- Consider OAuth2 for future GitHub integration

---

## Folder Structure (To be implemented)

```
python-fast-api/
├── services/
│   ├── code-analysis/          # Service 1
│   │   ├── app/
│   │   │   ├── main.py         # FastAPI app
│   │   │   ├── models/         # SQLAlchemy models
│   │   │   ├── routes/         # API endpoints
│   │   │   ├── services/       # Business logic
│   │   │   └── db/             # Database config
│   │   ├── alembic/            # Migrations
│   │   ├── tests/
│   │   ├── requirements.txt
│   │   └── Dockerfile
│   │
│   └── ai-assistant/           # Service 2
│       ├── app/
│       │   ├── main.py
│       │   ├── models/
│       │   ├── routes/
│       │   ├── services/
│       │   └── db/
│       ├── alembic/
│       ├── tests/
│       ├── requirements.txt
│       └── Dockerfile
│
├── shared/                     # Shared utilities (if needed)
├── documents/                  # Project documentation
├── docker-compose.yml
└── README.md
```

---

## Python Version
**Decision**: Python 3.11+
**Reason**:
- Modern async/await improvements
- Better type hints
- Performance improvements
- Still widely supported

---

## Notes
- Keep services loosely coupled
- Each service should be independently deployable
- Follow clean architecture principles
- Use dependency injection (FastAPI's DI system)
