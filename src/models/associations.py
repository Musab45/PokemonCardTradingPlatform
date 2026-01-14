# app/models/associations.py

from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from uuid import UUID as PyUUID

from src.database.base import Base

character_type = Table(
    "character_type",
    Base.metadata,
    Column("character_id", UUID(as_uuid=True), ForeignKey("characters.id"), primary_key=True),
    Column("type_id", UUID(as_uuid=True), ForeignKey("types.id"), primary_key=True),
)

attack_type = Table(
    "attack_type",
    Base.metadata,
    Column("attack_id", UUID(as_uuid=True), ForeignKey("attacks.id"), primary_key=True),
    Column("type_id", UUID(as_uuid=True), ForeignKey("types.id"), primary_key=True),
)

character_attack = Table(
    "character_attack",
    Base.metadata,
    Column("character_id", UUID(as_uuid=True), ForeignKey("characters.id"), primary_key=True),
    Column("attack_id", UUID(as_uuid=True), ForeignKey("attacks.id"), primary_key=True),
)