from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import date

class BookBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    author: str = Field(..., min_length=1, max_length=100)
    year: int = Field(..., gt=999, le=date.today().year)
    genre: str = Field(..., min_length=1, max_length=50)
    description: str = Field(..., min_length=1)

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    author: Optional[str] = Field(None, min_length=1, max_length=100)
    year: Optional[int] = Field(None, gt=999, le=date.today().year)
    genre: Optional[str] = Field(None, min_length=1, max_length=50)
    description: Optional[str] = Field(None, min_length=1)

    @validator('*')
    def check_at_least_one_field(cls, v, values):
        if v is None and not values:
            raise ValueError('At least one field must be provided for update')
        return v

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True
