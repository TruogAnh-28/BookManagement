from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import books
from database import engine, Base
import uvicorn
# Create tables in the database
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="Book Management API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(books.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Book Management API"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
