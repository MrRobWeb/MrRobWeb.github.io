<script setup>
import { ref, watch, nextTick } from 'vue';
import Captcha from './Captcha.vue';

const props = defineProps({
  show: Boolean
})

const isCaptchaSuccess = ref(false);
const captcha = ref('');
const inputText = ref('');
const isSubmitting = ref(false);
const submitError = ref('');
const submitSuccess = ref(false);

// Form fields
const formName = ref('');
const formEmail = ref('');
const formMessage = ref('');
const formErrors = ref({});

// Focus management refs
const captchaInput = ref(null);
const nameInput = ref(null);
const modalContainer = ref(null);

const emit = defineEmits(['close'])

const setCaptchaValue = (value) => {
  captcha.value = value;
}

const validateCaptcha = () => {
  isCaptchaSuccess.value = inputText.value === captcha.value.join('');
  inputText.value = '';
  if (isCaptchaSuccess.value) {
    nextTick(() => {
      nameInput.value?.focus();
    });
  }
}

const validateForm = () => {
  formErrors.value = {};

  if (!formName.value.trim()) {
    formErrors.value.name = 'Name is required';
  }

  if (!formEmail.value.trim()) {
    formErrors.value.email = 'Email is required';
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formEmail.value)) {
    formErrors.value.email = 'Please enter a valid email address';
  }

  if (!formMessage.value.trim()) {
    formErrors.value.message = 'Message is required';
  } else if (formMessage.value.trim().length < 10) {
    formErrors.value.message = 'Message must be at least 10 characters';
  }

  return Object.keys(formErrors.value).length === 0;
}

const submitForm = async () => {
  if (!validateForm()) return;

  isSubmitting.value = true;
  submitError.value = '';

  try {
    const response = await fetch('https://api.web3forms.com/submit', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify({
        access_key: import.meta.env.VITE_WEB3FORMS_ACCESS_KEY,
        name: formName.value,
        email: formEmail.value,
        message: formMessage.value
      })
    });

    const result = await response.json();

    if (result.success) {
      submitSuccess.value = true;
      formName.value = '';
      formEmail.value = '';
      formMessage.value = '';
    } else {
      submitError.value = result.message || 'Failed to send message. Please try again.';
    }
  } catch (error) {
    submitError.value = 'Network error. Please check your connection and try again.';
  } finally {
    isSubmitting.value = false;
  }
}

const closeMessage = () => {
  isCaptchaSuccess.value = false;
  inputText.value = '';
  submitSuccess.value = false;
  submitError.value = '';
  formErrors.value = {};
  formName.value = '';
  formEmail.value = '';
  formMessage.value = '';
  emit('close');
}

// Focus management - trap focus within modal
const handleKeydown = (e) => {
  if (e.key === 'Escape') {
    closeMessage();
  }

  if (e.key === 'Tab' && modalContainer.value) {
    const focusableElements = modalContainer.value.querySelectorAll(
      'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    );
    const firstElement = focusableElements[0];
    const lastElement = focusableElements[focusableElements.length - 1];

    if (e.shiftKey && document.activeElement === firstElement) {
      e.preventDefault();
      lastElement.focus();
    } else if (!e.shiftKey && document.activeElement === lastElement) {
      e.preventDefault();
      firstElement.focus();
    }
  }
}

// Focus first input when modal opens
watch(() => props.show, (newVal) => {
  if (newVal) {
    nextTick(() => {
      captchaInput.value?.focus();
    });
  }
});
</script>

<template>
  <Transition name="modal">
    <div
      v-if="show"
      class="modal-mask"
      role="dialog"
      aria-modal="true"
      aria-labelledby="modal-title"
      @keydown="handleKeydown"
    >
      <div v-if="!isCaptchaSuccess" ref="modalContainer" class="modal-container">
        <div class="modal-header">
          <h3 id="modal-title">
            <slot name="header"></slot>
          </h3>
        </div>

        <div class="modal-body">
          <slot name="body"></slot>
          <div class="mb-4">
            <h2 class="block text-gray-700 font-bold mb-2">
              Are you a robot?
            </h2>

            <label class="block text-gray-700 text-sm font-bold mb-2" for="captcha-input">
              Before you can send me a message you need to solve the captcha:
            </label>
            <input
              ref="captchaInput"
              v-model="inputText"
              id="captcha-input"
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline focus:ring-2 focus:ring-blue-500"
              type="text"
              name="captcha"
              required
              placeholder="Enter the text below"
              autocomplete="off"
              aria-describedby="captcha-hint"
            >
            <p id="captcha-hint" class="text-xs text-gray-500 mt-1">Type the characters shown in the image</p>
          </div>
          <Captcha @captcha="setCaptchaValue" aria-label="CAPTCHA verification image"></Captcha>
        </div>

        <div class="modal-footer flex flex-row justify-between">
          <slot name="footer">
            <button
              class="inline-block rounded bg-neutral-50 px-6 pb-2 pt-2.5 text-xs font-medium uppercase leading-normal text-neutral-800 shadow-[0_4px_9px_-4px_#cbcbcb] transition duration-150 ease-in-out hover:bg-neutral-100 hover:shadow-[0_8px_9px_-4px_rgba(203,203,203,0.3),0_4px_18px_0_rgba(203,203,203,0.2)] focus:bg-neutral-100 focus:shadow-[0_8px_9px_-4px_rgba(203,203,203,0.3),0_4px_18px_0_rgba(203,203,203,0.2)] focus:outline-none focus:ring-2 focus:ring-blue-500 active:bg-neutral-200"
              @click="closeMessage"
              type="button"
            >
              Cancel
            </button>
            <button
              class="inline-block rounded bg-neutral-800 px-6 pb-2 pt-2.5 text-xs font-medium uppercase leading-normal text-neutral-50 shadow-[0_4px_9px_-4px_rgba(51,45,45,0.7)] transition duration-150 ease-in-out hover:bg-neutral-700 focus:bg-neutral-700 focus:outline-none focus:ring-2 focus:ring-blue-500 active:bg-neutral-900 dark:bg-neutral-900 dark:hover:bg-neutral-800"
              @click="validateCaptcha"
              type="button"
            >
              Check
            </button>
          </slot>
        </div>
      </div>

      <div v-if="isCaptchaSuccess && !submitSuccess" ref="modalContainer" class="modal-container">
        <div class="modal-header">
          <h3 id="modal-title">
            <slot name="header"></slot>
          </h3>
        </div>

        <div class="modal-body">
          <slot name="body"></slot>

          <div v-if="submitError" class="mb-4 p-3 bg-red-100 border border-red-400 text-red-700 rounded" role="alert">
            {{ submitError }}
          </div>

          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="contact-name">
              Name <span class="text-red-500">*</span>
            </label>
            <input
              ref="nameInput"
              v-model="formName"
              id="contact-name"
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline focus:ring-2 focus:ring-blue-500"
              :class="{ 'border-red-500': formErrors.name }"
              type="text"
              name="name"
              required
              placeholder="Your Name"
              aria-required="true"
              :aria-invalid="!!formErrors.name"
              :aria-describedby="formErrors.name ? 'name-error' : undefined"
            >
            <p v-if="formErrors.name" id="name-error" class="text-red-500 text-xs mt-1">{{ formErrors.name }}</p>
          </div>
          <div class="mb-4">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="contact-email">
              E-mail <span class="text-red-500">*</span>
            </label>
            <input
              v-model="formEmail"
              id="contact-email"
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline focus:ring-2 focus:ring-blue-500"
              :class="{ 'border-red-500': formErrors.email }"
              type="email"
              name="email"
              required
              placeholder="Your E-mail"
              aria-required="true"
              :aria-invalid="!!formErrors.email"
              :aria-describedby="formErrors.email ? 'email-error' : undefined"
            >
            <p v-if="formErrors.email" id="email-error" class="text-red-500 text-xs mt-1">{{ formErrors.email }}</p>
          </div>
          <div class="relative mb-3">
            <label class="block text-gray-700 text-sm font-bold mb-2" for="contact-message">
              Message <span class="text-red-500">*</span>
            </label>
            <textarea
              v-model="formMessage"
              id="contact-message"
              name="message"
              required
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline focus:ring-2 focus:ring-blue-500 min-h-[100px]"
              :class="{ 'border-red-500': formErrors.message }"
              placeholder="Your message..."
              aria-required="true"
              :aria-invalid="!!formErrors.message"
              :aria-describedby="formErrors.message ? 'message-error' : undefined"
            ></textarea>
            <p v-if="formErrors.message" id="message-error" class="text-red-500 text-xs mt-1">{{ formErrors.message }}</p>
          </div>
        </div>

        <div class="modal-footer flex flex-row justify-between">
          <slot name="footer">
            <button
              class="inline-block rounded bg-neutral-50 px-6 pb-2 pt-2.5 text-xs font-medium uppercase leading-normal text-neutral-800 shadow-[0_4px_9px_-4px_#cbcbcb] transition duration-150 ease-in-out hover:bg-neutral-100 focus:bg-neutral-100 focus:outline-none focus:ring-2 focus:ring-blue-500 active:bg-neutral-200"
              @click="closeMessage"
              type="button"
              :disabled="isSubmitting"
            >
              Cancel
            </button>
            <button
              type="button"
              class="inline-block rounded bg-neutral-800 px-6 pb-2 pt-2.5 text-xs font-medium uppercase leading-normal text-neutral-50 shadow-[0_4px_9px_-4px_rgba(51,45,45,0.7)] transition duration-150 ease-in-out hover:bg-neutral-700 focus:bg-neutral-700 focus:outline-none focus:ring-2 focus:ring-blue-500 active:bg-neutral-900 dark:bg-neutral-900 dark:hover:bg-neutral-800 disabled:opacity-50 disabled:cursor-not-allowed"
              @click="submitForm"
              :disabled="isSubmitting"
            >
              {{ isSubmitting ? 'Sending...' : 'Send' }}
            </button>
          </slot>
        </div>
      </div>

      <div v-if="submitSuccess" ref="modalContainer" class="modal-container">
        <div class="modal-header">
          <h3 id="modal-title" class="text-green-600 font-bold">Message Sent!</h3>
        </div>
        <div class="modal-body text-center">
          <div class="text-green-500 text-5xl mb-4">&#10003;</div>
          <p class="text-gray-700">Thank you for your message! I'll get back to you soon.</p>
        </div>
        <div class="modal-footer flex justify-center">
          <button
            class="inline-block rounded bg-neutral-800 px-6 pb-2 pt-2.5 text-xs font-medium uppercase leading-normal text-neutral-50 shadow-[0_4px_9px_-4px_rgba(51,45,45,0.7)] transition duration-150 ease-in-out hover:bg-neutral-700 focus:bg-neutral-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
            @click="closeMessage"
            type="button"
          >
            Close
          </button>
        </div>
      </div>

    </div>
  </Transition>
</template>

<style>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  transition: opacity 0.3s ease;
}

.modal-container {
  width: 300px;
  margin: auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
}

.modal-header h3 {
  margin-top: 0;
  color: #000000;
}

.modal-body {
  margin: 20px 0;
}

.modal-default-button {
  float: right;
}

.modal-enter-from {
  opacity: 0;
}

.modal-leave-to {
  opacity: 0;
}

.modal-enter-from .modal-container,
.modal-leave-to .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>
