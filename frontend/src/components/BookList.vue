<template>
  <div>
    <div v-if="books.length > 0" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mt-6">
      <div
        v-for="book in paginatedBooks"
        :key="book.id"
        class="card transition-transform duration-200 hover:-translate-y-1 flex flex-col h-full"
      >
        <div class="p-5 flex-grow">
          <div class="mb-2 text-xs font-medium text-primary-darker bg-primary-bg inline-block px-2 py-0.5 rounded-full flex items-center max-w-fit">
            <i class="mdi mdi-tag-outline mr-1"></i>
            <span class="truncate max-w-[100px]">{{ book.genre }}</span>
          </div>
         
          <h3 class="text-lg font-bold mt-1 break-words">{{ book.title }}</h3>
         
          <p class="text-sm text-gray-600 flex items-center gap-1 mt-1">
            <i class="mdi mdi-account-outline text-primary-darker"></i>
            <span class="truncate max-w-[120px]">{{ book.author }}</span>
            <span class="mx-1 text-gray-300">•</span>
            <i class="mdi mdi-calendar-outline text-primary-darker"></i>
            {{ book.year }}
          </p>
         
          <p class="mt-3 text-sm text-gray-700 break-words line-clamp-3">
            {{ book.description }}
          </p>
        </div>
       
        <div class="mt-auto bg-gray-100 p-2 flex justify-between">
          <button
            @click="$emit('edit', book)"
            class="icon-btn text-primary hover:text-primary-darker flex items-center text-sm"
          >
            <i class="mdi mdi-pencil text-lg mr-1"></i>
            Edit
          </button>
          <button
            @click="$emit('delete', book.id)"
            class="icon-btn text-red-500 hover:text-red-700 flex items-center text-sm"
          >
            <i class="mdi mdi-delete text-lg mr-1"></i>
            Delete
          </button>
        </div>
      </div>
    </div>
   
    <div v-if="books.length > 0" class="flex justify-center items-center gap-2 mt-8">
      <button
        @click="currentPage--"
        :disabled="currentPage === 1"
        class="px-3 py-1 rounded bg-primary-bg text-primary-darker disabled:opacity-50 disabled:cursor-not-allowed"
      >
        <i class="mdi mdi-chevron-left"></i>
      </button>
      <span class="text-sm text-gray-600">
        Page {{ currentPage }} of {{ totalPages }}
      </span>
      <button
        @click="currentPage++"
        :disabled="currentPage === totalPages"
        class="px-3 py-1 rounded bg-primary-bg text-primary-darker disabled:opacity-50 disabled:cursor-not-allowed"
      >
        <i class="mdi mdi-chevron-right"></i>
      </button>
    </div>
   
    <div v-else class="text-center py-12 my-4">
      <i class="mdi mdi-bookshelf text-gray-300 text-6xl"></i>
      <p class="text-gray-500 mt-4">No books found. Add some books to get started!</p>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed, watch, PropType } from 'vue';
import { Book } from '../types/Book';

export default defineComponent({
  name: 'BookList',
  props: {
    books: {
      type: Array as PropType<Book[]>,
      required: true
    }
  },
  emits: ['edit', 'delete'],
  setup(props, { emit }) {
    const currentPage = ref(1);
    const itemsPerPage = 9;
    
    const totalPages = computed(() => Math.ceil(props.books.length / itemsPerPage));
    
    const paginatedBooks = computed(() => {
      const start = (currentPage.value - 1) * itemsPerPage;
      const end = start + itemsPerPage;
      return props.books.slice(start, end);
    });
    
    // Reset to page 1 when books array changes
    watch(() => props.books.length, () => {
      currentPage.value = 1;
    });

    return {
      currentPage,
      totalPages,
      paginatedBooks
    };
  }
});
</script>