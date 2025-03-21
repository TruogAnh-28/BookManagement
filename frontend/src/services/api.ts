import axios from 'axios'
import { Book, BookInput } from '../types/Book'

// Create an axios instance
const api = axios.create({
  baseURL: 'http://localhost:8000',
  headers: {
    'Content-Type': 'application/json',
  },
})

// Get all books
export const getBooks = async (): Promise<Book[]> => {
  try {
    const response = await api.get('/books')
    return response.data
  } catch (error) {
    console.error('Error fetching books:', error)
    throw error
  }
}

// Get a single book by ID
export const getBook = async (id: number): Promise<Book> => {
  try {
    const response = await api.get(`/books/${id}`)
    return response.data
  } catch (error) {
    console.error(`Error fetching book with ID ${id}:`, error)
    throw error
  }
}

// Create a new book
export const createBook = async (book: BookInput): Promise<Book> => {
  try {
    const response = await api.post('/books', book)
    return response.data
  } catch (error) {
    console.error('Error creating book:', error)
    throw error
  }
}

// Update an existing book
export const updateBook = async (book: Book): Promise<Book> => {
  try {
    const response = await api.put(`/books/${book.id}`, book)
    return response.data
  } catch (error) {
    console.error(`Error updating book with ID ${book.id}:`, error)
    throw error
  }
}

// Delete a book
export const deleteBook = async (id: number): Promise<void> => {
  try {
    await api.delete(`/books/${id}`)
  } catch (error) {
    console.error(`Error deleting book with ID ${id}:`, error)
    throw error
  }
}
