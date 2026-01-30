from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from app_v1.controller.healthcheck_controller import healthcheck_router
from app_v1.llm.llm_manager import LLMManager
from app_v1.llm.gpt51_model import GPT51Model


@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_llm_manager()
    yield


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.include_router(healthcheck_router)
    return app


def print_routes(app):
    print("Registered Routes:")
    for route in app.routes:
        print(f"Path: {getattr(route, 'path')}, Methods: {getattr(route, 'methods')}")


def initialize_llm_manager():
    llm_manager = LLMManager()
    llm_manager.set_classification_model(GPT51Model())


service_app = create_app()

# for local development
if __name__ == "__main__":
    uvicorn.run(service_app, host="0.0.0.0", port=8000, reload=False)
