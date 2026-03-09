# AI Agent Development Guide

This repository may be developed with the assistance of AI coding tools such as:

- GitHub Copilot
- Cursor
- AI pair programming agents

To ensure consistency, the following rules must be followed.

---

# Development Principles

1. Follow the architecture defined in `docs/system-architecture.md`.
2. Implement one checklist task at a time from `roadmap/development-checklist.md`.
3. Avoid large multi-feature implementations in a single step.
4. Maintain modular and maintainable code.

---

# Implementation Order

The system must be developed in this order:

1. Infrastructure
2. Backend API
3. Resume Intelligence
4. Job Scraping
5. Matching Engine
6. AI Generation
7. Agent System
8. Frontend
9. Deployment

Do not implement AI agents before the data pipeline exists.

---

# Coding Standards

### Python

Follow PEP8.

Use:

- snake_case for variables
- clear function names
- docstrings for modules

Example:

```python
def parse_resume(file_path: str) -> dict:
    """Extract structured data from a resume file."""
```
