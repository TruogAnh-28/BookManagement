/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: 'hsl(215, 100%, 50%)',
          variant: 'hsl(215, 100%, 60%)',
          darker: 'hsl(215, 100%, 40%)',
          light: 'hsl(215, 100%, 85%)',
          bg: 'hsl(215, 100%, 95%)',
        },
        secondary: 'hsl(263, 70%, 50%)',
        accent: 'hsl(45, 100%, 50%)',
      },
      backgroundImage: {
        'gradient-header':
          'linear-gradient(to right, rgba(59, 130, 246, 0.05), transparent)',
      },
    },
  },
  plugins: [],
};
