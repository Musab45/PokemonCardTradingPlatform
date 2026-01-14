from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from uuid import uuid4

from src.database.base import Base
from src.models.associations import character_type, attack_type

class Type(Base):
    __tablename__ = "types"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    characters = relationship(
        "Character",
        secondary=character_type,
        back_populates="types",
    )

    attacks = relationship(
        "Attack",
        secondary=attack_type,
        back_populates="types",
    )