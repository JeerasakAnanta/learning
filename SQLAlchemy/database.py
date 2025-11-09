# Database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Load environment
from  config.setting import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

# Database config postgres
SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Create engine for database connection
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create session class for database connection
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create base class for database models
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# test db
get_db()