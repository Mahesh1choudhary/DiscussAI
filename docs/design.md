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
| HTTP Client | httpx |
| LLM | GPT-5.1 (OpenAI API) |
| Metadata Store | PostgreSQL (Aiven - 1GB Basic) |
| Database Driver | psycopg2 |
| ORM | SQLAlchemy 2.0+ |
| Data Validation | Pydantic v2 |
| Config Management | YAML + Pydantic |
| Logging | Python logging |
| Vector Embeddings | OpenAI Embeddings API (optional) |
| Data Fetching | Custom scrapers (Reddit, LeetCode) |

### 3.1 Key Dependencies
- **FastAPI**: REST API framework with built-in validation and OpenAPI docs
- **SQLAlchemy**: Type-safe ORM with support for complex queries
- **Pydantic v2**: Data validation and serialization with strong type support
- **httpx**: Async HTTP client for external API calls (LLM, data sources)
- **psycopg2**: PostgreSQL driver optimized for production workloads
- **PyYAML**: Configuration management with environment-specific overrides
- **python-logging**: Structured logging for debugging and monitoring

## 4. Database Architecture

### 4.1 Database Hosting
- **Provider**: Aiven (PostgreSQL as a Service)
- **Rationale**: 
  - Eliminates database administration overhead
  - Automatic backups and high availability
  - Connection pooling built-in
  - Cost-effective for MVP phase
  - Easy migration path for production deployment

### 4.2 Storage Considerations
- **Current Capacity**: 1 GB
- **MVP Data Scope**: 
  - Discussion posts metadata (text summaries, not full content)
  - User profiles
  - Classification results
  - Embeddings cache (optional, for vector search optimization)
- **Scaling Strategy**: 
  - Aiven allows seamless upgrade to higher tiers
  - Monitor storage usage during MVP phase
  - Implement data archival/cleanup policies if needed
  - Consider partitioning strategies as dataset grows

### 4.3 Connection Management
- **Connection Pooling**: Configured via Aiven connection parameters
- **Configuration**: Environment-based YAML config for database credentials
- **SSL/TLS**: Enabled by default for secure communication with Aiven
- **Max Connections**: Aiven basic plan supports up to 25 concurrent connections

### 4.4 Database Schema
PostgreSQL is used to store:
- Discussion posts metadata (indexed for fast retrieval)
- User information (with auth tokens if needed)
- Classification results and metadata
- Post embeddings (optional, for similarity search)

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
