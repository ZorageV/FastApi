from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# while True:
#     try:
#         conn = psycopg2.connect(host="localhost",database="fastapi",user="postgres",password="zorage",cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("DB connected")
#         break
#     except Exception as error:
#         print("Connecting to DB failed")

# url = dialect+driver://username:password@host:port/database_name
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:zorage@localhost/fastapi"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()