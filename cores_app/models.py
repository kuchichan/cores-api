from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class Core(Base):
    __tablename__ = "Cores"

    id = Column(String(10), primary_key=True, index=True)
    reuse_count = Column(Integer)
    total_mass = Column(Integer)

    liked_by_users = relationship("User", back_populates="favourite_core")


class User(Base):
    __tablename__ = "Users"

    id = Column(
        Integer, primary_key=True, index=True
    )  # Because name is really bad candidate for a primary key
    name = Column(String(50))
    favourite_core_id = Column(
        String, ForeignKey("Cores.id", ondelete="SET NULL"), nullable=True
    )

    favourite_core = relationship("Core", back_populates="liked_by_users")
