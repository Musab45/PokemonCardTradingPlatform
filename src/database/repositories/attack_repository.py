from src.database.repositories.base import BaseRepository
from src.models.attack import Attack
from sqlalchemy import select
from sqlalchemy.orm import Session
from typing import Optional

class AttackRepository(BaseRepository[Attack]):
    
    def __init__(self, db: Session):
        super().__init__(Attack, db)
        
    def get_all_attacks(self) -> list[Attack]:
        """Get all Attacks"""
        query = select(Attack)
        return self.db.execute(query).scalars().all()
        
    def get_by_name(self, name: str) -> Optional[Attack]:
        """Get Attack by name"""
        query = select(Attack).filter(Attack.name == name)
        return self.db.execute(query).scalar_one_or_none()