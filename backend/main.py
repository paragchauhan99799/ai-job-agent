"""
Main Application Entry Point

This module serves as the entry point for the FastAPI backend application.
It initializes the app, includes routers, and provides health checks.
"""

from fastapi import FastAPI
from backend.api.routes import applications, jobs, resume

# Initialize FastAPI application
app = FastAPI(
    title="AI Job Agent Backend",
    description="Backend API for AI-powered job matching and application system",
    version="0.1.0",
)

# Include API routers
app.include_router(applications.router, prefix="/api/v1", tags=["applications"])
app.include_router(jobs.router, prefix="/api/v1", tags=["jobs"])
app.include_router(resume.router, prefix="/api/v1", tags=["resume"])


@app.get("/health", tags=["health"])
async def health_check():
    """
    Health check endpoint to verify the service is running.
    """
    return {"status": "healthy", "service": "AI Job Agent Backend"}