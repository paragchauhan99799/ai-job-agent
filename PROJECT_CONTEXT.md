# PROJECT CONTEXT — AI Job Agent

## Overview

AI Job Agent is an autonomous AI-powered system that discovers job opportunities, evaluates them against a candidate’s resume, ranks the best matches, generates personalized cover letters, and assists in managing job applications.

The project explores how **agentic AI systems** can automate the repetitive workflow of modern job searching.

This repository is designed as a **production-grade system architecture** rather than a simple demo project.

---

# System Objectives

The system should:

1. Discover relevant job opportunities automatically.
2. Parse and understand a candidate’s resume.
3. Match jobs using semantic similarity and structured scoring.
4. Generate personalized cover letters.
5. Track applications and job matches in a dashboard.
6. Eventually support autonomous job application workflows.

---

# Core System Components

The platform is composed of the following major components:

### Frontend

User interface for interacting with the system.

Responsibilities:

- Dashboard
- Job match viewing
- Application tracking
- Resume upload
- Cover letter preview

Technology:

- Next.js
- React
- TailwindCSS

---

### Backend API

Responsible for system orchestration and exposing APIs.

Responsibilities:

- Resume upload
- Job retrieval
- Application tracking
- AI agent orchestration

Technology:

- Python
- FastAPI

---

### AI Agent System

Implements the autonomous job workflow.

Agents:

- Job Discovery Agent
- Job Matching Agent
- Cover Letter Agent
- Orchestrator Agent

Framework:

- LangGraph
- LangChain

---

### Job Scraping System

Responsible for collecting job postings from multiple platforms.

Sources (initially):

- Indeed
- LinkedIn
- Company career pages

Technologies:

- Playwright
- BeautifulSoup
- Scrapy

---

### Matching Engine

Evaluates the relevance between candidate resumes and job descriptions.

Techniques:

- Embedding similarity
- Skill extraction
- Weighted scoring algorithm

---

### Vector Database

Stores embeddings for fast semantic similarity search.

Technology:

- Pinecone (preferred)
- Alternative: Weaviate

---

### Storage Layer

Stores structured application data.

Database:

PostgreSQL

Tables include:

- users
- resumes
- jobs
- job_matches
- applications

---

### Task Queue System

Handles background tasks.

Examples:

- job scraping
- embedding generation
- cover letter generation

Technology:

- Redis
- Celery

---

# High-Level Workflow

The system workflow:

1. User uploads resume
2. Resume parser extracts structured information
3. Resume embeddings are generated
4. Job scrapers collect job listings
5. Job embeddings are generated
6. Matching engine ranks job opportunities
7. AI generates personalized cover letters
8. Dashboard displays results

---

# Engineering Goals

This repository aims to demonstrate:

- AI system design
- agent-based architectures
- vector search pipelines
- production-grade backend engineering
- scalable architecture

The goal is to build a **realistic AI engineering portfolio project**.

---

# Development Philosophy

The project should be built with:

- modular architecture
- clear separation of concerns
- maintainable services
- scalable components

AI agents should be treated as **independent services** within the system.

---

# Development Strategy

Development will proceed incrementally through milestones:

1. Foundation
2. Resume Intelligence
3. Job Discovery
4. Matching Engine
5. AI Generation
6. Agent System
7. Frontend Dashboard
8. Deployment

Each phase is defined in the `roadmap` directory.
