from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from src.config import get_settings
from src.database.core import get_db
from src.models.type import Type
from src.schemas.type import TypeCreate, TypeResponse
from src.service.type_service import TypeService

settings = get_settings()
router = APIRouter(prefix='/types', tags=['Types'])

@router.post(
    '/',
    response_model=TypeResponse,
    summary='Create new type',
    description='Add a new type to the DB'
)
async def create_type(type: TypeCreate, db: Session = Depends(get_db)):
    """Create new type"""
    type_service = TypeService(db)
    return type_service.create_type(type)