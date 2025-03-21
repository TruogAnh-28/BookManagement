<template>
  <div class="min-h-screen bg-gray-50">
    <header class="bg-primary text-white shadow-md">
      <div class="container mx-auto py-4">
        <h1 class="text-2xl font-bold flex items-center">
          <i class="mdi mdi-book-open-page-variant mr-2 text-3xl"></i>
          Books Management
        </h1>
      </div>
    </header>
    
    <main class="container mx-auto py-8">
      <!-- Modal Form -->
      <div v-if="showForm" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
        <div class="bg-white rounded-lg shadow-xl w-full max-w-md overflow-hidden">
          <div class="modal-header flex justify-between items-center">
            <h2 class="text-xl font-bold text-gray-800">
              <i class="mdi" :class="editingBook ? 'mdi-pencil' : 'mdi-plus-circle'"></i>
              {{ editingBook ? 'Edit Book' : 'Add New Book' }}
            </h2>
            <button @click="cancelForm" class="icon-btn text-gray-500">
              <i class="mdi mdi-close"></i>
            </button>
          </div>
          <div class="p-6">
            <BookForm 
              :book="editingBook" 
              @save="saveBook" 
              @cancel="cancelForm" 
            />
          </div>
        </div>
      </div>
      
      <div class="card p-6">
        <BookSearch 
          v-model:search="searchQuery" 
          v-model:sortField="sortField" 
          v-model:sortDirection="sortDirection" 
        />
        <div class="flex justify-between items-center my-6">
          <h2 class="text-2xl font-semibold text-gray-800">Book List</h2>
          <button 
            @click="showAddForm" 
            class="btn btn-primary flex items-center"
          >
            <i class="mdi mdi-plus mr-1"></i> Add Book
          </button>
        </div>
        <div v-if="loading" class="text-center py-8">
          <i class="mdi mdi-loading mdi-spin text-primary text-4xl"></i>
          <div class="text-gray-500 mt-2">Loading books...</div>
        </div>
        
        <div v-else-if="error" class="text-center py-8">
          <i class="mdi mdi-alert-circle text-red-500 text-4xl"></i>
          <div class="text-red-500 mt-2">{{ error }}</div>
          <button 
            @click="fetchBooks" 
            class="btn btn-primary mt-4"
          >
            <i class="mdi mdi-refresh mr-1"></i> Retry
          </button>
        </div>
        
        <BookList
          :books="filteredAndSortedBooks" 
          @edit="editBook" 
          @delete="deleteBook" 
        />
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, watch } from 'vue'
import { Book } from './types/Book'
import { getBooks, createBook, updateBook, deleteBook as apiDeleteBook } from './services/api'
import BookForm from './components/BookForm.vue'
import BookSearch from './components/BookSearch.vue'
import BookList from './components/BookList.vue'
// State
const books = ref<Book[]>([])
const loading = ref(false)
const error = ref<string | null>(null)
const showForm = ref(false)
const editingBook = ref<Book | null>(null)
const searchQuery = ref('')
const sortField = ref<keyof Book>('title')
const sortDirection = ref<'asc' | 'desc'>('asc')

// Computed
const filteredAndSortedBooks = computed(() => {
  // Filter books by search query
  let filtered = books.value.filter(book => {
    const query = searchQuery.value.toLowerCase()
    return (
      book.title.toLowerCase().includes(query) ||
      book.author.toLowerCase().includes(query) ||
      book.genre.toLowerCase().includes(query) ||
      book.description.toLowerCase().includes(query)
    )
  })
  
  // Sort books
  filtered = [...filtered].sort((a, b) => {
    const aValue = a[sortField.value]
    const bValue = b[sortField.value]
    
    if (typeof aValue === 'string' && typeof bValue === 'string') {
      return sortDirection.value === 'asc' 
        ? aValue.localeCompare(bValue) 
        : bValue.localeCompare(aValue)
    } else {
      const comparison = aValue < bValue ? -1 : aValue > bValue ? 1 : 0
      return sortDirection.value === 'asc' ? comparison : -comparison
    }
  })
  
  return filtered
})

// Methods
const fetchBooks = async () => {
  loading.value = true
  error.value = null
  
  try {
    books.value = await getBooks()
  } catch (err) {
    error.value = 'Failed to load books. Please try again.'
    console.error(err)
  } finally {
    loading.value = false
  }
}

const showAddForm = () => {
  editingBook.value = null
  showForm.value = true
}

const editBook = (book: Book) => {
  editingBook.value = { ...book }
  showForm.value = true
}

const cancelForm = () => {
  showForm.value = false
  editingBook.value = null
}

const saveBook = async (book: Book) => {
  loading.value = true
  error.value = null
  
  try {
    if (book.id) {
      // Update existing book
      const updatedBook = await updateBook(book)
      const index = books.value.findIndex(b => b.id === book.id)
      if (index !== -1) {
        books.value[index] = updatedBook
      }
    } else {
      // Create new book
      const newBook = await createBook(book)
      books.value.push(newBook)
    }
    showForm.value = false
    editingBook.value = null
  } catch (err) {
    error.value = book.id ? 'Failed to update book' : 'Failed to create book'
    console.error(err)
  } finally {
    loading.value = false
  }
}

const deleteBook = async (id: number) => {
  if (!confirm('Are you sure you want to delete this book?')) return
  
  loading.value = true
  error.value = null
  
  try {
    await apiDeleteBook(id)
    books.value = books.value.filter(book => book.id !== id)
  } catch (err) {
    error.value = 'Failed to delete book'
    console.error(err)
  } finally {
    loading.value = false
  }
}

// Lifecycle
onMounted(fetchBooks)

// Watch for changes in search/sort to refetch if needed
watch([sortField, sortDirection], () => {
  // If we were doing server-side sorting, we would refetch here
  // For now, the sorting is client-side in the computed property
})
</script>
