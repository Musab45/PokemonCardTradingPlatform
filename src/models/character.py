from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from src.database.base import Base
from src.models.associations import character_type, character_attack

class Character(Base):
    __tablename__ = "characters"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(nullable=False)

    types = relationship(
        "Type",
        secondary=character_type,
        back_populates="characters",
    )

    attacks = relationship(
        "Attack",
        secondary=character_attack,
        back_populates="characters",
    )