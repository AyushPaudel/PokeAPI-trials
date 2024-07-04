from sqlalchemy import String, ForeignKey, Column
from sqlalchemy.dialects.postgresql import ARRAY

from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    email: Mapped[str] = mapped_column(
        String(200),
        unique=True,
        index=True
    )
    password: Mapped[str] = mapped_column(String(100))


class Pokemon(Base):
    __tablename__ = "pokemons"
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    name: Mapped[str] = mapped_column(index=True)
    ability = Column(ARRAY(String))
    type = Column(ARRAY(String), index=True)
    image: Mapped[str]
