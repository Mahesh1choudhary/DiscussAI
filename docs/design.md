# Project Design Document - LeetCodeDiscussAI

## 1. Overview
This project is an AI-powered tool to classify leetcode discussion posts into predefined categories
using an LLM-based approach and retrieve the same.
Major classification of a post -> Company name, Role( SDE I, II, etc and equivalents), post type(interview experience, compensation, preparation strategy, and online assessments, etc)


The system uses a Large Language Model (LLM) for semantic understanding and is designed to evolve from a lightweight local setup to a scalable production-ready architecture.

## 2. Goals & Non-Goals

### Goals
- Automatically classify discussion posts with high accuracy
- Minimize LLM calls using vector similarity search
- Maintain clean separation of concerns
- Enable easy migration to production-grade infrastructure

### Non-Goals
- Real-time streaming ingestion (out of scope for MVP)
- User authentication and authorization
- Fine-tuning custom ML models (LLM APIs only)


## 3. Initial Tech Stack ( Phase 1 - MVP)
| Layer | Technology |
|-----|-----------|
| Language | Python 3.10+ |
| API Framework | FastAPI |
| LLM | GPT (OpenAI API) |
| Metadata Store | PostgreSQL (Aiven) |
| Database Driver | psycopg2 |
| ORM | SQLAlchemy |
| Config | Pydantic & YAML |
| Logging | Python logging |

## 4. Database Architecture

### 4.1 Database Hosting
- **Provider**: Aiven (PostgreSQL as a Service)
- **Rationale**: 
  - Eliminates database administration overhead
  - Automatic backups and high availability
  - Connection pooling built-in
  - Scalable and production-ready from day one
  - Easy migration path for production deployment

### 4.2 Connection Management
- **Connection Pooling**: Configured via Aiven connection parameters
- **Configuration**: Environment-based YAML config for database credentials
- **SSL/TLS**: Enabled by default for secure communication with Aiven

### 4.3 Database Schema
PostgreSQL is used to store:
- Discussion posts metadata
- User information
- Classification results
- Caching/embeddings (future)

## 5. Data Layer Architecture

### 5.1 Repository Pattern
```
Controller/API
    ↓
Service Layer
    ↓
Repository Layer (CRUD operations)
    ↓
SQLAlchemy ORM
    ↓
PostgreSQL (Aiven)
```

### 5.2 Models
- **User**: User profiles and credentials
- **Post**: LeetCode discussion posts
- **Classification**: Classification results and metadata

## 6. Configuration Management

### 6.1 Environment-based Configuration
```yaml
database:
  backend: "postgresql"
  postgresql:
    host: "aiven-postgres-host"
    port: "5432"
    user: "avnadmin"
    password: "secure_password"
    db_name: "discussai_db"
    pool_min: 2
    pool_max: 10
```

### 6.2 Config Loading
- YAML-based configuration for flexibility
- Support for multiple environments (local, staging, production)
- Secure credential management via environment variables
