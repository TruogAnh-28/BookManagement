# Book Management Application

A comprehensive book management application with Vue 3 frontend and FastAPI backend with PostgreSQL database. This application allows you to manage your book collection with features for adding, editing, viewing, and deleting books.

## Features

- 📚 View all books in an attractive card layout
- 🔍 Search books by title, author, genre, or description
- 🔄 Sort books by different fields (title, author, year, genre)
- ➕ Add new books with form validation
- ✏️ Edit existing books
- 🗑️ Delete books
- 💅 Modern UI with Material Design Icons
- 📱 Responsive design for desktop and mobile

## Technology Stack

### Frontend
- **Vue.js 3**: Progressive JavaScript framework
- **TypeScript**: Type-safe JavaScript
- **Tailwind CSS**: Utility-first CSS framework
- **Material Design Icons**: High quality icon set
- **Vite**: Next generation frontend tooling

### Backend
- **FastAPI**: Modern, fast (high-performance) web framework for building APIs
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping
- **PostgreSQL**: Advanced open-source relational database
- **Pydantic**: Data validation and settings management
- **Uvicorn**: Lightning-fast ASGI server

## Project Structure

```
├── backend/
│   ├── database.py      # Database connection and session management
│   ├── main.py          # FastAPI application initialization
│   ├── models.py        # SQLAlchemy ORM models
│   ├── routers/         # API endpoints
│   │   └── books.py     # Book-related endpoints (CRUD operations)
│   └── schemas.py       # Pydantic schemas for request/response models
├── frontend/
│   ├── public/          # Static assets
│   ├── src/
│   │   ├── assets/      # CSS and other assets
│   │   ├── components/  # Vue components
│   │   ├── services/    # API services
│   │   └── types/       # TypeScript type definitions
│   ├── vite.config.ts   # Vite configuration
│   └── package.json     # Frontend dependencies
└── README.md            # This documentation
```

## Getting Started

### Prerequisites

- Node.js (v14+)
- Python (v3.8+)
- PostgreSQL

### Installation

1. Clone the repository

2. Set up the backend:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. Set up the frontend:
   ```bash
   cd frontend
   npm install
   ```

4. Configure environment variables:
   Create a `.env` file in the backend directory with:
   ```
   DATABASE_URL=postgresql://username:password@localhost/books_db
   ```

### Running the Application

1. Start the backend server:
   ```bash
   cd backend
   python main.py
   ```

2. Start the frontend development server:
   ```bash
   cd frontend
   npm run dev
   ```

3. Open your browser and navigate to `http://localhost:5173`

## API Endpoints

- `GET /api/books`: Get all books
- `GET /api/books/{id}`: Get a specific book
- `POST /api/books`: Create a new book
- `PUT /api/books/{id}`: Update an existing book
- `DELETE /api/books/{id}`: Delete a book

## Future Enhancements

- User authentication and personal book collections
- Book rating system
- Book cover image uploads
- Export/import book data
- Dark mode support"# BookManagement" 
"# BookManagement" 
