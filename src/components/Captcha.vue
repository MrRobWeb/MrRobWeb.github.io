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
            class="np-captcha-character"
          >
            <s class="blur">
                {{ c }}
            </s>
          </div>
        </div>
      </div>
  
      <button @click="createCaptcha" class="np-button">Generate new</button>
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
  