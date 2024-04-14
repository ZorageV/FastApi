from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# url = dialect+driver://username:password@host:port/database_name
db_url = "postgresql://zorage:zorage@host:localhost/fastapi"

engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()