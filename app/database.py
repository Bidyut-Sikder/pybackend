


from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

username = "postgres"
password = "bidyut"
host = "localhost"  # Use the appropriate host
port = "5432"       # Default PostgreSQL port
database = "pybackend"

# Create the connection string
DATABASE_URL = f"postgresql://{username}:{password}@{host}:{port}/{database}"



engine = create_engine(DATABASE_URL)



SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)


Base=declarative_base()























