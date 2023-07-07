import { defineStore } from 'pinia'

export const useAppStore = defineStore('app', {
    state: () => ({ 
        theme: localStorage.theme,
    getters: {
      doubleCount: (state) => state.count * 2,
    },
    actions: {
      increment() {
        this.count++
      },
    },
  })})