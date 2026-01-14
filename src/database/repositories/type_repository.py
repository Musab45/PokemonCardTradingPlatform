from sqlalchemy.orm import Session
from sqlalchemy import select
from src.database.repositories.base import BaseRepository
from src.models.type import Type
from typing import Optional

class TypeRepository(BaseRepository[Type]):
    
    def __init__(self, db: Session):
        super().__init__(Type, db)
        
    def get_by_name(self, name: str) -> Optional[Type]:
        """Get a Type by name."""
        query = select(Type).filter(Type.name == name)
        return self.db.execute(query).scalar_one_or_none()