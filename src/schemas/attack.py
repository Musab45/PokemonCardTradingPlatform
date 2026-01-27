from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from uuid import UUID as PyUUID

from src.schemas.type import TypeResponse

class AttackBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255, description='Attack Name')
    description: str | None = Field(None, max_length=255, description='Attack Description')
    power: int = Field(0, ge=0, description='Attack Power (must be >= 0)')
    
class AttackCreate(AttackBase):
    type_ids: list[PyUUID] = Field(default_factory=list, description='List of Type IDs')

class AttackUpdate(AttackBase):
    """Attack Update Schema"""
    type_ids: list[PyUUID] = Field(default_factory=list, description='List of Type IDs')

class AttackResponse(AttackBase):
    id: PyUUID
    types: list[TypeResponse] = []
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)