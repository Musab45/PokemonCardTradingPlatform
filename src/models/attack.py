from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from src.database.base import Base
from src.models.associations import attack_type, character_attack

class Attack(Base):
    __tablename__ = "attacks"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(nullable=False)
    power: Mapped[int] = mapped_column(default=0)

    types = relationship(
        "Type",
        secondary=attack_type,
        back_populates="attacks",
    )

    characters = relationship(
        "Character",
        secondary=character_attack,
        back_populates="attacks",
    )