from uuid import uuid4, UUID
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.database.repositories.type_repository import TypeRepository
from src.schemas.type import TypeCreate
from src.models.type import Type
from src.core.exceptions import ConflictError

class TypeService:
    """Service for Type related operations."""
    
    def __init__(self, db: Session):
        self.repository = TypeRepository(db)
        self.db = db
        
    def create_type(self, type_data: TypeCreate) -> Type:
        """Create new type"""
        try:
            # check if type already exists
            existing_type = self.repository.get_by_name(type_data.name)
            if existing_type:
                # implement logging
                raise ConflictError('Type with name already exists')
            
            type = Type(
                id=uuid4(),
                **type_data.model_dump()
            )
            
            created_type = self.repository.create(type)
            #logg
            return created_type
        
        except IntegrityError as e:
            #logg
            self.db.rollback()
            raise ConflictError('Type with name already exists')
        except Exception as e:
            #logg
            self.db.rollback()
            raise