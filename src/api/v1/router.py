from fastapi import APIRouter
from src.api.v1 import type, attack

api_router = APIRouter()

api_router.include_router(type.router)
api_router.include_router(attack.router)