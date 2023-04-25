
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from utils import get_engine


class Base(DeclarativeBase):
    pass


class Eptica(Base):
    __tablename__ = "Eptica"
    id:  Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[str] = mapped_column()
    entite: Mapped[str] = mapped_column()
    instance: Mapped[str] = mapped_column()
    nb_recus: Mapped[float] = mapped_column( nullable=True)

class Telephonie(Base):
    __tablename__ = "Telephonie"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date_appel: Mapped[str] = mapped_column()
    entite: Mapped[str] = mapped_column()
    famille: Mapped[str] = mapped_column()
    nombre_entrants_corrige: Mapped[float] = mapped_column(nullable=True)

def create_tables(engine):

    Base.metadata.create_all(engine)
    

if __name__ == "__main__":
    engine = get_engine()
    create_tables(engine)

