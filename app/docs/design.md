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


## 2. Initial Tech Stack ( Phase 1 - MVP)
| Layer | Technology |
|-----|-----------|
| Language | Python 3.10+ |
| API Framework | FastAPI |
| LLM | GPT (OpenAI API) |
| Metadata Store | SQLite |
| Vector Store | FAISS |
| ORM | SQLAlchemy |
| Embeddings | OpenAI Embeddings |
| Config | Pydantic |
| Logging | Python logging |