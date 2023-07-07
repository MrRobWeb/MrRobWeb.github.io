<template>
    <div class="bg-[#ffffff]  dark:bg-[#0F172A] duration-500 transition-all ease-in-out">
        <div class="max-w-sm sm:w-8/12 
        flex flex-row justify-between mx-auto my-4">
            <RouterLink to="/" class="nav">
                Home
            </RouterLink>
            <RouterLink to="/about" class="nav">
                About
            </RouterLink>
            <RouterLink to="/project" class="nav">
                Projects
            </RouterLink>
            <RouterLink to="/contact" class="nav">
                Contact
            </RouterLink>
        </div>


        <div>
            <hr class="border-1 my-8 border-gray-400 sm:w-8/12 mx-auto">
        </div>
    </div>
</template>
<script setup>
import router from '../router';

const route = router.currentRoute.value.path;
</script>

<style type="text/tailwindcss">

</style>