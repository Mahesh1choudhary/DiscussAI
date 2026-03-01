# Changelog
All notable changes to this project will be documented in this file.

## [Unreleased]

### Added
- **Database Infrastructure**: Integrated Aiven PostgreSQL Basic (1GB storage) for metadata persistence
- **Tech Stack Update**: 
  - Added SQLAlchemy 2.0+ ORM for database operations
  - Added Pydantic v2 for data validation and serialization
  - Added httpx as async HTTP client for external API calls
  - Added PyYAML for configuration management
  - Specified GPT-5.1 as LLM provider via OpenAI API
  - Added support for OpenAI Embeddings API (optional, for vector search optimization)
- **Design Documentation**: 
  - Comprehensive database architecture section with Aiven hosting details
  - Storage considerations and scaling strategy for 1GB basic plan
  - Connection management and security (SSL/TLS)
  - Data layer architecture using repository pattern
  - Configuration management approach for multiple environments
- **Key Dependencies Documentation**:
  - FastAPI for REST API framework
  - psycopg2 as PostgreSQL driver
  - Custom scrapers for Reddit and LeetCode data fetching

### Technical Specifications
- **Database Plan**: Aiven Basic with 1GB storage capacity
- **Max Connections**: 25 concurrent connections supported by Aiven basic plan
- **ORM Version**: SQLAlchemy 2.0+ for type-safe database operations
- **Data Validation**: Pydantic v2 with strong type support
- **API Framework**: FastAPI with built-in OpenAPI documentation

### Architecture Decisions
- Chose Aiven managed PostgreSQL over SQLite for production readiness
- Implemented repository pattern for clean data layer separation
- Configured YAML-based environment-specific database credentials
- Enabled SSL/TLS for secure Aiven connection
- Planned for seamless scaling to higher Aiven tiers as needed

