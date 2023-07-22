import { defineStore } from 'pinia'

export const useAppStore = defineStore('app', {
    state: () => ({ 
        theme: localStorage.theme,
        heightHeader: 0,
    getters: {
    },
    actions: {
    },
  })})