<template>
  <form @submit.prevent="handleSubmit" class="space-y-6">
    <div>
      <label
        class="block text-gray-700 text-sm font-medium mb-2 flex items-center gap-1"
        for="title"
      >
        <i class="mdi mdi-book text-primary"></i> Title
      </label>
      <input
        id="title"
        v-model="formData.title"
        class="form-input"
        type="text"
        placeholder="Enter book title"
        required
      />
      <p
        v-if="errors.title"
        class="text-red-500 text-xs mt-1 flex items-center gap-1"
      >
        <i class="mdi mdi-alert-circle-outline"></i> {{ errors.title }}
      </p>
    </div>

    <div>
      <label
        class="block text-gray-700 text-sm font-medium mb-2 flex items-center gap-1"
        for="author"
      >
        <i class="mdi mdi-account text-primary"></i> Author
      </label>
      <input
        id="author"
        v-model="formData.author"
        class="form-input"
        type="text"
        placeholder="Enter author name"
        required
      />
      <p
        v-if="errors.author"
        class="text-red-500 text-xs mt-1 flex items-center gap-1"
      >
        <i class="mdi mdi-alert-circle-outline"></i> {{ errors.author }}
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <div>
        <label
          class="block text-gray-700 text-sm font-medium mb-2 flex items-center gap-1"
          for="year"
        >
          <i class="mdi mdi-calendar text-primary"></i> Year Published
        </label>
        <input
          id="year"
          v-model.number="formData.year"
          class="form-input"
          type="number"
          min="1000"
          :max="currentYear"
          placeholder="YYYY"
          required
        />
        <p
          v-if="errors.year"
          class="text-red-500 text-xs mt-1 flex items-center gap-1"
        >
          <i class="mdi mdi-alert-circle-outline"></i> {{ errors.year }}
        </p>
      </div>

      <div>
        <label
          class="block text-gray-700 text-sm font-medium mb-2 flex items-center gap-1"
          for="genre"
        >
          <i class="mdi mdi-tag text-primary"></i> Genre
        </label>
        <select id="genre" v-model="formData.genre" class="form-input" required>
          <option value="" disabled>Select a genre</option>
          <option v-for="genre in genreOptions" :key="genre" :value="genre">
            {{ genre }}
          </option>
        </select>
        <p
          v-if="errors.genre"
          class="text-red-500 text-xs mt-1 flex items-center gap-1"
        >
          <i class="mdi mdi-alert-circle-outline"></i> {{ errors.genre }}
        </p>
      </div>
    </div>

    <div>
      <label
        class="block text-gray-700 text-sm font-medium mb-2 flex items-center gap-1"
        for="description"
      >
        <i class="mdi mdi-text-box text-primary"></i> Description
      </label>
      <textarea
        id="description"
        v-model="formData.description"
        class="form-input"
        rows="4"
        placeholder="Enter book description"
        required
      ></textarea>
      <p
        v-if="errors.description"
        class="text-red-500 text-xs mt-1 flex items-center gap-1"
      >
        <i class="mdi mdi-alert-circle-outline"></i> {{ errors.description }}
      </p>
    </div>

    <div class="flex justify-end space-x-3 pt-2">
      <button
        type="button"
        @click="$emit('cancel')"
        class="btn btn-outline flex items-center"
      >
        <i class="mdi mdi-close mr-1"></i> Cancel
      </button>
      <button type="submit" class="btn btn-primary flex items-center">
        <i
          class="mdi"
          :class="book ? 'mdi-content-save' : 'mdi-plus-circle'"
        ></i>
        <span class="ml-1">{{ book ? 'Update Book' : 'Add Book' }}</span>
      </button>
    </div>
  </form>
</template>

<script lang="ts">
import { defineComponent, reactive, onMounted, PropType } from 'vue';
import { Book } from '../types/Book';

export default defineComponent({
  name: 'BookForm',
  props: {
    book: {
      type: Object as PropType<Book | null>,
      default: null
    }
  },
  emits: ['save', 'cancel'],
  setup(props, { emit }) {
    const currentYear = new Date().getFullYear();

    // Genre options
    const genreOptions = [
      'Fiction',
      'Non-Fiction',
      'Science Fiction',
      'Fantasy',
      'Mystery',
      'Romance',
      'Thriller',
      'Biography',
      'History',
      'Other',
    ];

    // Initialize form data with empty values or provided book
    const formData = reactive<Book>({
      id: 0,
      title: '',
      author: '',
      year: currentYear,
      genre: '',
      description: '',
    });

    // Validation errors
    const errors = reactive({
      title: '',
      author: '',
      year: '',
      genre: '',
      description: '',
    });

    // Initialize the form with book data if editing
    onMounted(() => {
      if (props.book) {
        Object.assign(formData, { ...props.book });
      }
    });

    // Validate form data
    const validateForm = (): boolean => {
      let valid = true;

      // Reset errors
      Object.keys(errors).forEach((key) => {
        errors[key as keyof typeof errors] = '';
      });

      // Title validation
      if (!formData.title.trim()) {
        errors.title = 'Title is required';
        valid = false;
      } else if (formData.title.length > 100) {
        errors.title = 'Title cannot exceed 100 characters';
        valid = false;
      }

      // Author validation
      if (!formData.author.trim()) {
        errors.author = 'Author is required';
        valid = false;
      } else if (formData.author.length > 100) {
        errors.author = 'Author name cannot exceed 100 characters';
        valid = false;
      }

      // Year validation
      if (!formData.year) {
        errors.year = 'Year is required';
        valid = false;
      } else if (formData.year < 1000 || formData.year > currentYear) {
        errors.year = `Year must be between 1000 and ${currentYear}`;
        valid = false;
      }

      // Genre validation
      if (!formData.genre) {
        errors.genre = 'Genre is required';
        valid = false;
      }

      // Description validation
      if (!formData.description.trim()) {
        errors.description = 'Description is required';
        valid = false;
      }

      return valid;
    };

    const handleSubmit = () => {
      if (validateForm()) {
        emit('save', { ...formData });
      }
    };

    return {
      formData,
      errors,
      currentYear,
      genreOptions,
      validateForm,
      handleSubmit
    };
  }
});
</script>