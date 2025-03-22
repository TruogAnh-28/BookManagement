from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import or_
from models.books import Book
from schema.books import BookCreate, BookUpdate

class BookService:
    """
    Service class for Book-related operations
    This class handles the business logic for book operations
    """

    @staticmethod
    def get_books(
        db: Session, 
        skip: int = 0, 
        limit: int = 100,
        title: Optional[str] = None,
        author: Optional[str] = None,
        genre: Optional[str] = None
    ) -> List[Book]:
        """
        Get all books with optional filtering
        """
        query = db.query(Book)
        
        # Apply filters if provided
        if title or author or genre:
            filter_conditions = []
            if title:
                filter_conditions.append(Book.title.ilike(f"%{title}%"))
            if author:
                filter_conditions.append(Book.author.ilike(f"%{author}%"))
            if genre:
                filter_conditions.append(Book.genre.ilike(f"%{genre}%"))
                
            if filter_conditions:
                query = query.filter(or_(*filter_conditions))
        
        return query.offset(skip).limit(limit).all()

    @staticmethod
    def get_book(db: Session, book_id: int) -> Optional[Book]:
        """
        Get a specific book by ID
        """
        return db.query(Book).filter(Book.id == book_id).first()

    @staticmethod
    def create_book(db: Session, book: BookCreate) -> Book:
        """
        Create a new book
        """
        db_book = Book(**book.dict())
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book

    @staticmethod
    def update_book(db: Session, book_id: int, book: BookUpdate) -> Optional[Book]:
        """
        Update an existing book
        """
        db_book = BookService.get_book(db, book_id)
        if db_book:
            # Update model with provided values, skipping None values
            update_data = book.dict(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_book, key, value)
            
            db.commit()
            db.refresh(db_book)
        
        return db_book

    @staticmethod
    def delete_book(db: Session, book_id: int) -> bool:
        """
        Delete a book
        Returns True if book was deleted, False if book not found
        """
        db_book = BookService.get_book(db, book_id)
        if db_book:
            db.delete(db_book)
            db.commit()
            return True
        
        return False