<template>
  <div class="mb-8">
    <div class="flex flex-col lg:flex-row gap-4">
      <div class="flex-grow">
        <div class="relative">
          <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
            <i class="mdi mdi-magnify text-xl text-gray-400"></i>
          </div>
          <input
            id="search"
            v-model="searchValue"
            type="text"
            placeholder="Search books by title, author or genre..."
            class="form-input pl-10"
            @input="updateSearch"
          />
        </div>
      </div>
      
      <div class="flex flex-col sm:flex-row items-start sm:items-center gap-3">
        <div class="flex items-center gap-2">
          <i class="mdi mdi-sort text-lg text-primary"></i>
          <label for="sort-field" class="text-sm font-medium text-gray-600 whitespace-nowrap">Sort by:</label>
        </div>
        
        <div class="flex gap-2">
          <select
            id="sort-field"
            v-model="sortFieldValue"
            class="form-input py-2 text-sm"
            @change="updateSort"
          >
            <option value="title">Title</option>
            <option value="author">Author</option>
            <option value="year">Year</option>
            <option value="genre">Genre</option>
          </select>
        
          <select
            id="sort-direction"
            v-model="sortDirectionValue"
            class="form-input py-2 text-sm"
            @change="updateSort"
          >
            <option value="asc">
             Asc
            </option>
            <option value="desc">
              Desc
            </option>
          </select>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, watch, PropType } from 'vue';
import { Book } from '../types/Book';

export default defineComponent({
  name: 'SearchAndSortBar',
  props: {
    search: {
      type: String,
      required: true
    },
    sortField: {
      type: String as PropType<keyof Book>,
      required: true
    },
    sortDirection: {
      type: String as PropType<'asc' | 'desc'>,
      required: true,
      validator: (value: string) => ['asc', 'desc'].includes(value)
    }
  },
  emits: ['update:search', 'update:sortField', 'update:sortDirection'],
  setup(props, { emit }) {
    // Internal state
    const searchValue = ref(props.search);
    const sortFieldValue = ref<keyof Book>(props.sortField);
    const sortDirectionValue = ref<'asc' | 'desc'>(props.sortDirection);

    watch(() => props.search, (newVal) => {
      searchValue.value = newVal;
    });

    watch(() => props.sortField, (newVal) => {
      sortFieldValue.value = newVal;
    });

    watch(() => props.sortDirection, (newVal) => {
      sortDirectionValue.value = newVal;
    });

    // Update methods
    const updateSearch = () => {
      emit('update:search', searchValue.value);
    };

    const updateSort = () => {
      emit('update:sortField', sortFieldValue.value);
      emit('update:sortDirection', sortDirectionValue.value);
    };

    return {
      searchValue,
      sortFieldValue,
      sortDirectionValue,
      updateSearch,
      updateSort
    };
  }
});
</script>