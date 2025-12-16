import { defineStore } from 'pinia'


function dateAgo(date) {
    var startDate = new Date(date);
    var diffDate = new Date(new Date() - startDate);
    return (
        (diffDate.toISOString().slice(0, 4) - 1970) + " Years " 
        + diffDate.getMonth() + " Months " 
        // + (diffDate.getDate()-1) + "D"
    );
}

export const useAppStore = defineStore('app', {
    state: () => ({
        theme: localStorage.theme,
        heightHeader: 0,
        workAge: dateAgo('2014/08/01'),
    }),
    getters: {
    },
    actions: {
    },
})