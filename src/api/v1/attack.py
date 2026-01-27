from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from src.config import get_settings
from src.database.core import get_db
from src.models.attack import Attack
from src.schemas.attack import AttackCreate, AttackResponse, AttackUpdate
from src.service.attack_service import AttackService

settings = get_settings()
router = APIRouter(prefix='/attacks', tags=['Attacks'])

@router.get(
    '/',
    response_model=list[AttackResponse],
    summary='Get all Attacks',
    description='Get all Attacks from DB'
)
async def get_all_attacks(db: Session = Depends(get_db)):
    attack_service = AttackService(db)
    return attack_service.get_all_attacks()

@router.get(
    '/{id}',
    response_model=AttackResponse,
    summary='Get Attack by ID',
    description='Get Attack by ID from DB'
)
async def get_attack_by_id(id: UUID, db: Session = Depends(get_db)):
    attack_service = AttackService(db)
    return attack_service.get_attack_by_id(id)

@router.post(
    '/',
    response_model=AttackResponse,
    summary='Create a new Attack',
    description='Create a new Attack in DB'
)
async def create_attack(attack: AttackCreate, db: Session = Depends(get_db)):
    attack_service = AttackService(db)
    return attack_service.create_attack(attack)

@router.post(
    '/{attack_id}/types/{type_id}',
    response_model=AttackResponse,
    summary='Add type to attack'
)
async def add_type_to_attack(
    attack_id: UUID, 
    type_id: UUID, 
    db: Session = Depends(get_db)
):
    attack_service = AttackService(db)
    return attack_service.add_type_to_attack(attack_id, type_id)

@router.put(
    '/{id}',
    response_model=AttackResponse,
    summary='Update an Attack by ID',
    description='Update an Attack by ID in DB'
)
async def attack_update(id: UUID, attack: AttackUpdate, db: Session = Depends(get_db)):
    attack_service = AttackService(db)
    return attack_service.update_attack(id, attack)

@router.delete(
    '/{id}',
    response_model=None,
    summary='Delete an Attack by ID',
    description='Delete an Attack by ID from DB'
)
async def delete_attack(id: UUID, db: Session = Depends(get_db)):
    attack_service = AttackService(db)
    return attack_service.delete_attack(id)

@router.delete(
    '/{attack_id}/types/{type_id}',
    response_model=AttackResponse,
    summary='Remove type from attack'
)
async def remove_type_from_attack(
    attack_id: UUID, 
    type_id: UUID, 
    db: Session = Depends(get_db)
):
    attack_service = AttackService(db)
    return attack_service.remove_type_from_attack(attack_id, type_id)