from uuid import uuid4, UUID
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from src.models.type import Type
from src.core.exceptions import NotFoundError, ConflictError
from src.database.repositories.attack_repository import AttackRepository
from src.models.attack import Attack
from src.schemas.attack import AttackCreate, AttackUpdate


class AttackService:
    """Service for Attack related operations"""
    
    def __init__(self, db: Session):
        self.repository = AttackRepository(db)
        self.db = db
        
    def get_all_attacks(self):
        """Get all Attacks"""
        attacks = self.repository.get_all_attacks()
        return attacks
    
    def get_attack_by_id(self, id: UUID) -> Attack:
        """Get Attack by ID"""
        attack_obj = self.repository.get(id)
        if not attack_obj:
            raise NotFoundError("Attack not found")
        return attack_obj
    
    def get_by_name(self, name: str) -> Attack:
        """Get Attack by name"""
        attack_obj = self.repository.get_by_name(name)
        if not attack_obj:
            raise NotFoundError("Attack not found")
        return attack_obj
    
    def create_attack(self, attack_data: AttackCreate) -> Attack:
        """Create a new Attack"""
        try:
            existing_attack = self.repository.get_by_name(attack_data.name)
            if existing_attack:
                raise ConflictError("Attack with name already exists")
            
            attack = Attack(
            id=uuid4(),
            name=attack_data.name,
            description=attack_data.description,
            power=attack_data.power
            )
            
            if attack_data.type_ids:
                for type_id in attack_data.type_ids:
                    type_obj = self.db.query(Type).filter(Type.id == type_id).first()
                    if not type_obj:
                        raise NotFoundError(f"Type with id {type_id} not found")
                    attack.types.append(type_obj)
            
            created_attack = self.repository.create(attack)
            return created_attack
        
        except IntegrityError:
            self.db.rollback()
            raise ConflictError("Attack with name already exists")
        except ConflictError:
            raise
        except Exception as e:
            self.db.rollback()
            raise
        
    def add_type_to_attack(self, attack_id: UUID, type_id: UUID) -> Attack:
        """Add Type to an Attack"""
        attack_obj = self.repository.get(attack_id)
        if not attack_obj:
            raise NotFoundError("Attack not found")
        
        type_obj = self.db.query(Type).filter(Type.id == type_id).first()
        if not type_obj:
            raise NotFoundError("Type not found")
        
        if type_obj not in attack_obj.types:
            attack_obj.types.append(type_obj)
            self.db.commit()
            self.db.refresh(attack_obj)
            
        return attack_obj
        
    def update_attack(self, id: UUID, attack_data: AttackUpdate) -> Attack:
        """Update an Attack"""
        try:
            attack_obj = self.repository.get(id)
            if not attack_obj:
                raise NotFoundError("Attack not found")
            
            if attack_data.name != attack_obj.name:
                existing_attack = self.repository.get_by_name(attack_data.name)
                if existing_attack:
                    raise ConflictError("Attack with this name already exists")

            attack_obj.name = attack_data.name
            attack_obj.description = attack_data.description
            attack_obj.power = attack_data.power
            
            if attack_data.type_ids is not None:
                attack_obj.types.clear() # removing existing types
                for type_id in attack_data.type_ids:
                    type_obj = self.db.query(Type).filter(Type.id == type_id).first()
                    if not type_obj:
                        raise NotFoundError(f"Type with id {type_id} not found")
                    attack_obj.types.append(type_obj)
            
            updated_attack = self.repository.update(attack_obj)
            return updated_attack
            
        except IntegrityError:
            self.db.rollback()
            raise ConflictError("Attack with this name already exists")
        except (NotFoundError, ConflictError):
            raise
        except Exception as e:
            self.db.rollback()
            raise
            
        
    def delete_attack(self, id: UUID) -> bool:
        """Delete an Attack"""
        attack_obj = self.repository.get(id)
        if not attack_obj:
            raise NotFoundError("Attack not Found")
        return self.repository.delete(id)
    
    def delete_type_from_attack(self, type_id: UUID, attack_id: UUID) -> Attack:
        """Delete a Type from an Attack"""
        attack_obj = self.repository.get(attack_id)
        if not attack_obj:
            raise NotFoundError("Attack not found")
        
        type_obj = self.db.query(Type).filter(Type.id == type_id).first()
        if not type_obj:
            raise NotFoundError("Type not found")
        
        if type_obj in attack_obj.types:
            attack_obj.types.remove(type_obj)
            self.db.commit()
            self.db.refresh(attack_obj)
        
        return attack_obj