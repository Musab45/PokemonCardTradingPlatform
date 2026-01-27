from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from uuid import UUID
from src.config import get_settings
from src.database.core import get_db
from src.models.type import Type
from src.schemas.type import TypeCreate, TypeUpdate, TypeResponse
from src.service.type_service import TypeService

settings = get_settings()
router = APIRouter(prefix='/types', tags=['Types'])

@router.get(
    '/',
   response_model=list[TypeResponse],
    summary='Get all types',
    description='Get all types from DB'
)
async def get_types(db: Session = Depends(get_db)):
    """Get all types"""
    type_service = TypeService(db)
    return type_service.get_all_types()

@router.get(
    '/{id}',
   response_model=TypeResponse,
    summary='Get type by ID',
    description='Get type by ID from DB'
)
async def get_type_by_name(id: UUID, db: Session = Depends(get_db)):
    """Get Type by name"""
    type_service = TypeService(db)
    return type_service.get_by_id(id)

@router.get(
    '/{name}',
   response_model=TypeResponse,
    summary='Get type by name',
    description='Get type by name from DB'
)
async def get_type_by_name(name: str, db: Session = Depends(get_db)):
    """Get Type by name"""
    type_service = TypeService(db)
    return type_service.get_type_by_name(name)

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

@router.put(
    '/{id}',
    response_model=TypeResponse,
    summary='Update type by ID',
    description='Update an existing type in the DB'
)
async def update_type(id: UUID, type: TypeUpdate, db: Session = Depends(get_db)):
    """Update type by ID"""
    type_service = TypeService(db)
    return type_service.update_type(id, type)

@router.delete(
    '/{id}',
    response_model=None,
    summary='Delete Type by ID',
    description='Delete a type from DB by ID'
)
async def delete_type(id: UUID, db: Session = Depends(get_db)):
    """Delete Type by ID"""
    type_service = TypeService(db)
    return type_service.delete_type(id)