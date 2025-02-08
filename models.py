# filepath: /c:/Users/Balagsa/ml_backend/models.py
from sqlalchemy import Column, Integer, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class DiagnosisRecord(Base):
    __tablename__ = 'diagnosis_records'
    id = Column(Integer, primary_key=True)
    symptoms = Column(Text)
    diagnosis = Column(Text)

# Configure MySQL database connection
DATABASE_URI = 'mysql+mysqlconnector://root:@localhost/sds_capstone'
engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)