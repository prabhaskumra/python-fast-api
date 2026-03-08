# Decision Log

**Purpose**: Track all significant technical decisions, alternatives considered, and rationale. Update this after each session or major decision.

---

## 2026-03-07: Project Initialization

### Decision: Use 2 Microservices Instead of 3
**Context**: Original plan had 3 services (Code Analysis, AI Assistant, Repository Management)
**Decision**: Build only 2 services (Code Analysis + AI Assistant)
**Reason**: Repository service too complex for initial Python learning goals. Focus on AI integration and code analysis capabilities.
**Trade-offs**:
- ✅ Reduced scope, faster learning
- ✅ Still demonstrates microservices architecture
- ❌ Less comprehensive platform
**Status**: Approved

---

### Decision: FastAPI as Web Framework
**Context**: Need modern Python web framework
**Alternatives Considered**:
- Flask: Too basic, no async, manual OpenAPI docs
- Django: Too heavy, not API-focused
- FastAPI: Modern, async, auto docs, type hints
**Decision**: FastAPI
**Reason**: Best developer experience, closest to modern .NET Core patterns, excellent documentation
**Status**: Approved

---

### Decision: SQLAlchemy + Alembic for Database
**Context**: Need ORM and migration tool (coming from EF Core background)
**Alternatives Considered**:
- Django ORM: Requires Django framework
- Tortoise ORM: Less mature, smaller community
- Peewee: Too simple for enterprise use
**Decision**: SQLAlchemy 2.0 + Alembic
**Reason**: Industry standard, most similar to EF Core, excellent async support
**Status**: Approved

---

### Decision: PostgreSQL as Primary Database
**Context**: Need production-grade relational database
**Alternatives Considered**:
- SQLite: Not production-ready, no concurrent writes
- MySQL: Less feature-rich than PostgreSQL
- PostgreSQL: Industry standard, feature-rich
**Decision**: PostgreSQL
**Reason**: Production-grade, familiar from enterprise work, excellent Python support
**Status**: Approved

---

### Decision: Redis for Caching
**Context**: Need caching for LLM API responses (cost reduction)
**Alternatives Considered**:
- Memcached: Less versatile than Redis
- In-memory Python dict: Not persistent, doesn't scale
**Decision**: Redis
**Reason**: Fast, can also serve as message broker later, industry standard
**Status**: Approved

---

### Decision: Anthropic Claude as Primary LLM
**Context**: Need LLM provider for AI Assistant service
**Alternatives Considered**:
- OpenAI GPT-4: Good but more expensive
- Local models (Ollama): Slower, requires GPU
**Decision**: Anthropic Claude (with optional OpenAI support)
**Reason**: Excellent code understanding, longer context windows, competitive pricing
**Status**: Approved

---

### Decision: Docker Compose for Local Development
**Context**: Need consistent dev environment
**Alternatives Considered**:
- Kubernetes: Overkill for local dev
- Manual setup: Inconsistent across machines
**Decision**: Docker Compose
**Reason**: Simple, consistent, familiar from .NET background
**Status**: Approved

---

### Decision: Python 3.11+
**Context**: Choose Python version
**Alternatives Considered**:
- Python 3.9/3.10: Older, missing performance improvements
- Python 3.12: Too new, less library support
**Decision**: Python 3.11
**Reason**: Modern features, stable, well-supported by libraries
**Status**: Approved

---

## Template for Future Decisions

### Decision: [Title]
**Date**: YYYY-MM-DD
**Context**: [Why this decision is needed]
**Alternatives Considered**:
- Option 1: [Description + pros/cons]
- Option 2: [Description + pros/cons]
**Decision**: [What was chosen]
**Reason**: [Rationale]
**Trade-offs**:
- ✅ [Benefits]
- ❌ [Drawbacks]
**Status**: [Approved / Pending / Rejected]
**Owner**: [Who made/approved decision]

---

## Notes

- Add new decisions at the top (reverse chronological)
- Link to relevant GitHub issues/PRs if applicable
- Update status if decision is revisited
- Include "Owner" for accountability in team settings
