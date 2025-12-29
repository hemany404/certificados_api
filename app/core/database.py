from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# Criação do engine SQLAlchemy
db = create_engine("sqlite:///banco.db")


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db)


def pegar_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()