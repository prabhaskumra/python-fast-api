# Claude Code Configuration

This directory contains Claude Code agent configuration for the project.

## Commands

Custom slash commands available in this project:

- `/test` - Run pytest test suite
- `/migrate` - Generate and apply database migrations with Alembic
- `/run` - Start the FastAPI development server with uvicorn
- `/lint` - Run code quality checks (ruff, black, mypy)

## Hooks

- `user-prompt-submit.sh` - Runs before each user prompt (add custom validations here)

## Usage

Use slash commands by typing them in the chat, e.g., `/test` to run tests.
