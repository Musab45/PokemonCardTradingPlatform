from typing import Generic, TypeVar, Type, Optional, Any
from sqlalchemy.orm import Session
from sqlalchemy import select, func
from uuid import UUID

ModelType = TypeVar('ModelType')

class BaseRepository(Generic[ModelType]):
    
    def __init__(self, model: Type[ModelType], db: Session):
        self.model = model
        self.db = db
        
    def create(self, obj: ModelType) -> ModelType:
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj