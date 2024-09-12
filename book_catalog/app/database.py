from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

##SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
SQLALCHEMY_DATABASE_URL = "postgresql://miranda_pena_carrasquillo:5K0QsSQvdlIUFeizNDewOvul7jdPGs6z@dpg-crfskcbv2p9s73a2b9lg-a.singapore-postgres.render.com/library_db_izwe"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
