from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from typing import List, Optional
from database import get_db
from schema.books import Book, BookCreate, BookUpdate
from services.book_service import BookService

router = APIRouter(prefix="/books", tags=["books"])

@router.get("", response_model=List[Book])
def get_books(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db),
    title: Optional[str] = Query(None),
    author: Optional[str] = Query(None),
    genre: Optional[str] = Query(None)
):
    """
    Get all books with optional filtering
    """
    return BookService.get_books(db, skip, limit, title, author, genre)

@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    """
    Get a specific book by ID
    """
    book = BookService.get_book(db, book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    """
    Create a new book
    """
    return BookService.create_book(db, book)

@router.put("/{book_id}", response_model=Book)
def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    """
    Update an existing book
    """
    updated_book = BookService.update_book(db, book_id, book)
    if updated_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """
    Delete a book
    """
    success = BookService.delete_book(db, book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found")
    return None
