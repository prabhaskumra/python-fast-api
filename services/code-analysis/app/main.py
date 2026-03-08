from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="Code Analysis Service",
    description="Static code analysis, security scanning, and quality metrics",
    version="0.1.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "service": "Code Analysis Service",
        "status": "running",
        "version": "0.1.0"
    }


@app.get("/health")
async def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "service": "code-analysis",
        "database": "not_connected"  # Will update when DB is configured
    }


class CodeRequest(BaseModel):
    code: str
    language: str = "python"


@app.post("/analyze")
async def analyze_code(request: CodeRequest):
    """
    Analyze Python code snippet

    MVP: Returns basic info (line count, character count)
    Future: Will include AST parsing, complexity metrics, security scanning
    """
    lines = request.code.split('\n')
    return {
        "status": "success",
        "analysis": {
            "line_count": len(lines),
            "character_count": len(request.code),
            "non_empty_lines": len([line for line in lines if line.strip()])
        },
        "language": request.language,
        "message": "MVP: Basic analysis complete. Advanced features coming soon."
    }
