from sqlalchemy import Column, Integer, String, Text
from database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False, index=True)
    author = Column(String(100), nullable=False, index=True)
    year = Column(Integer, nullable=False)
    genre = Column(String(50), nullable=False, index=True)
    description = Column(Text, nullable=False)
