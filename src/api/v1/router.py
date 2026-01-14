from fastapi import APIRouter
from src.api.v1 import type

api_router = APIRouter()

api_router.include_router(type.router)