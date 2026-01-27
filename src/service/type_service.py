from uuid import uuid4, UUID
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.database.repositories.type_repository import TypeRepository
from src.schemas.type import TypeCreate, TypeUpdate
from src.models.type import Type
from src.core.exceptions import ConflictError, NotFoundError

class TypeService:
    """Service for Type related operations."""
    
    def __init__(self, db: Session):
        self.repository = TypeRepository(db)
        self.db = db
        
    def get_all_types(self)-> list[Type]:
        """Get all Types"""
        types = self.repository.get_all()
        return types
    
    def get_by_id(self, id: UUID) -> Type:
        """Get Type by ID"""
        type_obj = self.repository.get(id)
        if not type_obj:
         raise NotFoundError('Type not found')
        return type_obj
    
    def get_type_by_name(self, name: str) -> Type:
        """Get Type by name"""
        type_obj = self.repository.get_by_name(name=name)
        if not type_obj:
         raise NotFoundError('Type not found')
        return type_obj
        
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
        
    def update_type(self, id: UUID, type_data: TypeUpdate) -> Type:
        """Update an existing type"""
        try:
            # Get existing type
            type_obj = self.repository.get(id)
            if not type_obj:
                raise NotFoundError('Type not found')
            
            # Check if new name conflicts with another type
            if type_data.name != type_obj.name:
                existing_type = self.repository.get_by_name(type_data.name)
                if existing_type:
                    raise ConflictError('Type with this name already exists')
            
            # Update fields
            type_obj.name = type_data.name
            
            # Save changes
            updated_type = self.repository.update(type_obj)
            return updated_type
            
        except IntegrityError:
            self.db.rollback()
            raise ConflictError('Type with this name already exists')
        except (NotFoundError, ConflictError):
            raise
        except Exception as e:
            self.db.rollback()
            raise
        
        
    def delete_type(self, id: UUID) -> bool:
        type_obj = self.repository.get(id)
        if not type_obj:
            raise NotFoundError("Type not found")
        return self.repository.delete(id)