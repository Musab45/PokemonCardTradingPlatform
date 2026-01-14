from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from uuid import UUID as PyUUID

class TypeBase(BaseModel):
    """Base Type Schema"""
    name: str = Field(..., min_length=1, max_length=255, description='Type Name')
    
class TypeCreate(TypeBase):
    """Create Type Schema"""
    pass

class TypeResponse(TypeBase):
    """Schema for Type Response"""
    
    id: PyUUID
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)