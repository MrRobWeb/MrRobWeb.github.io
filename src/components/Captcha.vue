<template>

    
    <div id="captcha">
      <h2></h2>
      <div class="np-captcha-container">
        <div class="np-captcha" v-if="captcha && captcha.length">
          <div
            v-for="(c, i) in captcha"
            :key="i"
            :style="{
              fontSize: getFontSize() + 'px',
              fontWeight: 800,
              transform: 'rotate(' + getRotationAngle() + 'deg)',
            }"
            class="np-captcha-character rounded"
          >
            <s class="blur">
                {{ c }}
            </s>
          </div>
        </div>
      </div>
  
      <button 
        @click="createCaptcha" class="inline-block  bg-neutral-50 px-6 pb-2 pt-2.5 text-xs font-medium uppercase leading-normal text-neutral-800 shadow-[0_4px_9px_-4px_#cbcbcb] transition duration-150 ease-in-out hover:bg-neutral-100 hover:shadow-[0_8px_9px_-4px_rgba(203,203,203,0.3),0_4px_18px_0_rgba(203,203,203,0.2)] focus:bg-neutral-100 focus:shadow-[0_8px_9px_-4px_rgba(203,203,203,0.3),0_4px_18px_0_rgba(203,203,203,0.2)] focus:outline-none focus:ring-0 active:bg-neutral-200 active:shadow-[0_8px_9px_-4px_rgba(203,203,203,0.3),0_4px_18px_0_rgba(203,203,203,0.2)] dark:shadow-[0_4px_9px_-4px_rgba(251,251,251,0.3)] dark:hover:shadow-[0_8px_9px_-4px_rgba(251,251,251,0.1),0_4px_18px_0_rgba(251,251,251,0.05)] dark:focus:shadow-[0_8px_9px_-4px_rgba(251,251,251,0.1),0_4px_18px_0_rgba(251,251,251,0.05)] dark:active:shadow-[0_8px_9px_-4px_rgba(251,251,251,0.1),0_4px_18px_0_rgba(251,251,251,0.05)]"
      >Generate new
    </button>
    </div>
  </template>
  
  <script setup>
import { onMounted, ref } from 'vue';
// data
const captchaLength = ref(5);
const captcha = ref([]);


const emit = defineEmits(['captcha'])
// methods

const createCaptcha = () => {
    let tempCaptcha = "";
    for (let i = 0; i < captchaLength.value; i++) {
        tempCaptcha += getRandomCharacter();
    }
    captcha.value = tempCaptcha.split("");
    emit('captcha', captcha.value);
    
};

const getRandomCharacter = () => {
    const symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    const randomNumber = Math.floor(Math.random() * 36);
    return symbols[randomNumber];
};
const getFontSize = () => {
    const fontVariations = [20, 30, 36, 40];
    return fontVariations[Math.floor(Math.random() * 5)];
};
const getRotationAngle = () => {
    const rotationVariations = [5, 10, 20, 25, -5, -10, -20, -25];
    return rotationVariations[Math.floor(Math.random() * 8)];
};

onMounted(()=>{
    createCaptcha();
});

  </script>
  
  <style>
  #captcha {
    font-family: "Avenir", Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #000000;
  }

  .blur {
    filter: blur(1.5px);
    -webkit-filter: blur(1.5px);
    }
  .np-captcha-container {
    background: #eee;
    margin: 0 auto;
    margin-bottom: 20px;
  }
  .np-captcha {
    font-size: 24px;
  }
  .np-button {
    padding: 6px 10px;
    background: #fff;
    border: 1px solid #eee;
    border-radius: 6px;
    font-size: 16px;
  }
  .np-captcha-character {
    display: inline-block;
    letter-spacing: 14px;
  }
  </style>
  