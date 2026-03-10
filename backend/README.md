# Backend Setup Guide

This guide provides instructions for setting up and running the AI Job Agent backend API.

## Prerequisites

- **Python**: Version 3.12 or later
- **Poetry**: Python dependency management tool
- **System Dependencies** (macOS):
  - libxml2 and libxslt (for lxml parsing)

## Installation

### 1. Install Poetry

If Poetry is not installed, install it using the official installer:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Add Poetry to your PATH by adding this to your shell configuration (e.g., `~/.zshrc`):

```bash
export PATH="$HOME/.local/bin:$PATH"
```

### 2. Install System Dependencies

For macOS users, install required libraries:

```bash
brew install libxml2 libxslt
```

### 3. Clone and Setup Project

```bash
git clone <repository-url>
cd ai-job-agent/backend
```

### 4. Install Python Dependencies

```bash
poetry install
```

This will create a virtual environment and install all required dependencies.

## Configuration

### Environment Variables

Create a `.env` file in the backend directory with the following variables:

```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/ai_job_agent

# Redis
REDIS_URL=redis://localhost:6379

# OpenAI API
OPENAI_API_KEY=your_openai_api_key

# Pinecone
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENVIRONMENT=your_pinecone_environment

# Application
APP_ENV=development
DEBUG=True
```

### Database Setup

1. Install PostgreSQL
2. Create database: `ai_job_agent`
3. Run migrations (when implemented)

## Running the Application

### Development Mode

```bash
poetry run dev
```

This starts the server with auto-reload enabled on `http://localhost:8000`

### Production Mode

```bash
poetry run start
```

This starts the server on `http://0.0.0.0:8000` for production deployment.

### Manual Commands

You can also run commands directly:

```bash
# Development with reload
poetry run uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Production
poetry run uvicorn main:app --host 0.0.0.0 --port 8000

# With workers (for production)
poetry run uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

## Available Scripts

The following Poetry scripts are available:

- `poetry run dev`: Start development server with auto-reload
- `poetry run start`: Start production server
- `poetry run test`: Run tests (when implemented)
- `poetry run lint`: Run code linting (when implemented)

## API Documentation

Once the server is running, visit:

- **API Docs**: `http://localhost:8000/docs` (Swagger UI)
- **Alternative Docs**: `http://localhost:8000/redoc`
- **Health Check**: `http://localhost:8000/health`

## Project Structure

```
backend/
├── main.py                 # FastAPI application entry point
├── pyproject.toml          # Poetry configuration and dependencies
├── api/
│   ├── routes/            # API route handlers
│   │   ├── applications.py
│   │   ├── jobs.py
│   │   └── resume.py
│   └── schemas/           # Pydantic models
├── services/              # Business logic
├── database/              # Database models and connections
└── README.md              # This file
```

## Development

### Code Quality

```bash
# Format code
poetry run black .

# Lint code
poetry run ruff .

# Type checking (when implemented)
poetry run mypy .
```

### Testing

```bash
poetry run test
```

## Deployment

### Docker

Build and run with Docker:

```bash
docker build -t ai-job-agent-backend .
docker run -p 8000:8000 ai-job-agent-backend
```

### Production Considerations

- Set `APP_ENV=production` and `DEBUG=False`
- Use environment variables for all configuration
- Configure proper logging
- Set up database migrations
- Use a reverse proxy (nginx) in front of the application
- Implement health checks and monitoring

## Troubleshooting

### Common Issues

1. **Module not found**: Ensure you're running commands from the `backend` directory
2. **Port already in use**: Change the port with `--port` option
3. **Dependencies fail to install**: Ensure system dependencies are installed
4. **Python version issues**: Verify Python 3.12+ is being used

### Getting Help

- Check the API documentation at `/docs`
- Review FastAPI documentation
- Check Poetry documentation for dependency management