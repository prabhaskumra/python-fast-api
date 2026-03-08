# Project Documentation

**Purpose**: This folder contains all project documentation to ensure smooth handoffs between sessions and team members.

---

## Documentation Files

### 📋 [project-goal.md](project-goal.md)
**What**: Complete project overview, features, tech stack, learning objectives
**When to read**: Starting fresh or need reminder of overall goals
**Update frequency**: Rarely (only if project scope changes)

---

### 🏗️ [architecture.md](architecture.md)
**What**: Technical architecture decisions, tech stack rationale, folder structure
**When to read**: Understanding why certain technologies/patterns were chosen
**Update frequency**: When making significant architectural decisions

---

### 🛠️ [setup.md](setup.md)
**What**: Step-by-step development environment setup guide
**When to read**: First time setup or troubleshooting environment issues
**Update frequency**: When dev setup changes (new dependencies, Docker config, etc.)

---

### 📝 [decisions.md](decisions.md)
**What**: Log of all major technical decisions with context and rationale
**When to read**: Understanding past decisions or before making new ones
**Update frequency**: After each significant technical decision

---

### ✅ [progress.md](progress.md)
**What**: Session-by-session progress tracker, current status, next steps
**When to read**: **START HERE** - First file to check when resuming work
**Update frequency**: **End of every session** (MANDATORY)

---

## Workflow for New Sessions

### Starting a New Session
1. Read [progress.md](progress.md) - See what was last done and what's next
2. Check [decisions.md](decisions.md) - Review recent technical decisions
3. Reference [architecture.md](architecture.md) or [setup.md](setup.md) as needed
4. Start working!

### Ending a Session
1. **Update [progress.md](progress.md)** with:
   - Date
   - What you completed (with file references)
   - What's in progress
   - Specific next steps
   - Any blockers

2. **Update [decisions.md](decisions.md)** if you made any technical decisions

3. Commit changes with descriptive message

---

## Quick Reference

| Need to... | Check... |
|-----------|----------|
| Resume after break | [progress.md](progress.md) |
| Understand project goals | [project-goal.md](project-goal.md) |
| Set up environment | [setup.md](setup.md) |
| Understand tech choices | [architecture.md](architecture.md) |
| Review past decisions | [decisions.md](decisions.md) |

---

## For Claude Code Agents

**Important Instructions**:

When starting a new session:
1. **Always read `progress.md` first** to understand current state
2. Check `decisions.md` for recent technical decisions
3. Reference other docs as needed for context

When ending a session:
1. **Always update `progress.md`** with session summary
2. Update `decisions.md` if any significant decisions were made
3. Be specific about next steps so future sessions can continue smoothly

---

**Last Updated**: 2026-03-07
