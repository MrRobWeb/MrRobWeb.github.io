<template>
    <div class="">
        <img src="../assets/imgs/IMG_7440_1.jpeg"
            alt="Robert Weber profile photo"
            loading="lazy"
            class="w-[180px] h-[180px] sm:w-[200px] sm:h-[200px] mx-auto rounded-full shadow-md animate-fade">
        <h1 class="mt-8 mb-4 text-center text-3xl sm:text-4xl uppercase font-bold dark:text-white animate-fade">Robert Weber
        </h1>
        <hr class="border-1 my-4 border-gray-400 w-14 mx-auto animate-fade">
        <h1 class="mb-2 text-center font-mono lg:text-4xl dark:text-white text-2xl animate-fade">
            Hi, I&apos;m a
            <br class="block" />
            <span v-show="isTypeWrite == 1" class="relative font-bold">
                <span class="h-20 pt-2 overflow-x-hidden whitespace-nowrap text-brand-accent">
                    Data Engineer
                </span>
                <span
                    class="text-left absolute -bottom-0 left-0 -top-1 inline-block bg-[#ffffff] dark:bg-[#0F172A] duration-500 transition-all ease-in-out w-full animate-type will-change">|</span>
            </span>
            <span v-show="isTypeWrite == 2" class="relative font-bold">
                <span class="h-20 pt-2 overflow-x-hidden whitespace-nowrap text-brand-accent">
                    LLM Fullstack Developer
                </span>
                <span
                    class="{`${styles.cursor} text-left  absolute -bottom-0 left-0 -top-1 inline-block bg-[#ffffff]  dark:bg-[#0F172A] duration-500 transition-all ease-in-out w-full animate-type will-change`}">|</span>
            </span>
            <span v-show="isTypeWrite == 3" class="relative font-bold">
                <span class="h-20 pt-2 overflow-x-hidden whitespace-nowrap text-brand-accent">
                    DevOps Engineer
                </span>
                <span
                    class="{`${styles.cursor} text-left  absolute -bottom-0 left-0 -top-1 inline-block bg-[#ffffff]  dark:bg-[#0F172A] duration-500 transition-all ease-in-out w-full animate-type will-change`}">|</span>
            </span>
            <span v-show="isTypeWrite == 4" class="relative font-bold">
                <span class="h-20 pt-2 overflow-x-hidden whitespace-nowrap text-brand-accent">
                    Project Manager
                </span>
                <span
                    class="{`${styles.cursor} text-left  absolute -bottom-0 left-0 -top-1 inline-block bg-[#ffffff]  dark:bg-[#0F172A] duration-500 transition-all ease-in-out w-full animate-type will-change`}">|</span>
            </span>
        </h1>
    </div>
</template>

<script setup>

import { ref, onMounted, onUnmounted } from 'vue';

const isTypeWrite = ref(1);
let intervalId = null;

onMounted(() => {
    window.scrollTo({
        top: 0
    });

    intervalId = setInterval(function () {
        if (isTypeWrite.value == 4) {
            isTypeWrite.value = 1;
        } else {
            isTypeWrite.value++;
        }
    }, 3800);
});

onUnmounted(() => {
    if (intervalId) {
        clearInterval(intervalId);
        intervalId = null;
    }
});

</script>
