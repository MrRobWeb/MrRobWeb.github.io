/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class',
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily:{
        'ubuntu': ['Ubuntu', 'sans-serif'],
      },
      animation: {
        type: 'type 1.5s ease-out .8s infinite alternate both',
        fade: 'fadeIn 0.7s ease-in-out',
      },
      keyframes: {
        type: {
          '0%': { transform: 'translateX(0%)' },
          '5%, 10%': { transform: 'translateX(10%)' },
          '15%, 20%': { transform: 'translateX(20%)' },
          '25%, 30%': { transform: 'translateX(30%)' },
          '35%, 40%': { transform: 'translateX(40%)' },
          '45%, 50%': { transform: 'translateX(50%)' },
          '55%, 60%': { transform: 'translateX(60%)' },
          '65%, 70%': { transform: 'translateX(70%)' },
          '75%, 80%': { transform: 'translateX(80%)' },
          '85%, 90%': { transform: 'translateX(90%)' },
          '95%, 100%': { transform: 'translateX(100%)' },
        },
        fadeIn: {
          '0%': { opacity: 0},
          '100%': { opacity: 1 },
        },
      }
    },
  },
  plugins: [],
}

/** infinite alternate **/