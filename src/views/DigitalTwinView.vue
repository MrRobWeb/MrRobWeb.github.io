<template>
  <div class="py-4 md:py-6">
    <div class="container-corporate">
      <div class="max-w-3xl mx-auto">
        <!-- Header -->
        <div class="text-center mb-4">
          <img
            src="../assets/imgs/profile.jpg"
            alt="Robert Weber"
            :class="[
              'mx-auto rounded-full border-4 border-corporate-light-gray dark:border-mckinsey-navy-light mb-3 transition-all duration-300',
              messages.length === 0 ? 'w-24 h-24 md:w-32 md:h-32' : 'w-12 h-12 md:w-16 md:h-16'
            ]"
          >
          <h1 class="text-heading-2 text-mckinsey-navy dark:text-white mb-1">
            Digital Twin
          </h1>
          <p class="text-small text-corporate-mid-gray">
            Ask me anything about my experience, projects, or expertise.
          </p>
        </div>

        <!-- Chat Container -->
        <div class="chat-container">
          <!-- Messages -->
          <div ref="messagesContainer" class="messages-container">
            <!-- Welcome Message -->
            <div v-if="messages.length === 0" class="welcome-message">
              <div class="welcome-icon">
                <font-awesome-icon :icon="['fas', 'robot']" />
              </div>
              <h3 class="text-heading-3 text-mckinsey-navy dark:text-white mb-1">
                Hello! I'm Robert's Digital Twin
              </h3>
              <p class="text-small text-corporate-mid-gray mb-4">
                I can answer questions about Robert's professional experience, projects, and technical expertise.
              </p>
              <div class="suggestions">
                <button
                  v-for="suggestion in suggestions"
                  :key="suggestion"
                  @click="askQuestion(suggestion)"
                  class="suggestion-chip"
                >
                  {{ suggestion }}
                </button>
              </div>
            </div>

            <!-- Chat Messages -->
            <div
              v-for="(message, index) in messages"
              :key="index"
              :class="['message', message.role]"
            >
              <div class="message-avatar">
                <img
                  v-if="message.role === 'assistant'"
                  src="../assets/imgs/profile.jpg"
                  alt="Robert"
                  class="avatar-img"
                >
                <font-awesome-icon
                  v-else
                  :icon="['fas', 'user-secret']"
                  class="avatar-icon"
                />
              </div>
              <div class="message-content">
                <div class="message-bubble">
                  <p v-if="message.role === 'assistant' && isTyping && index === messages.length - 1">
                    <span class="typing-cursor">{{ displayedText }}</span>
                  </p>
                  <p v-else>{{ message.content }}</p>
                </div>
                <span class="message-time">{{ formatTime(message.timestamp) }}</span>
              </div>
            </div>

            <!-- Loading indicator -->
            <div v-if="isLoading" class="message assistant">
              <div class="message-avatar">
                <img
                  src="../assets/imgs/profile.jpg"
                  alt="Robert"
                  class="avatar-img"
                >
              </div>
              <div class="message-content">
                <div class="message-bubble">
                  <div class="typing-indicator">
                    <span></span>
                    <span></span>
                    <span></span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Input Area -->
          <div class="input-area">
            <div class="input-wrapper">
              <input
                v-model="userInput"
                @keyup.enter="sendMessage"
                type="text"
                placeholder="Ask about my experience..."
                class="chat-input"
                :disabled="isLoading"
              >
              <button
                @click="sendMessage"
                :disabled="!userInput.trim() || isLoading"
                class="send-button"
              >
                <font-awesome-icon :icon="['fas', 'arrow-right']" />
              </button>
            </div>
            <p class="input-hint">
              Powered by RAG with Jina embeddings + OpenAI
            </p>
          </div>
        </div>

        <!-- API Key Notice -->
        <div v-if="!hasApiKey" class="api-notice">
          <font-awesome-icon :icon="['fas', 'gears']" class="mr-2" />
          <span>Configure your OpenAI API key in the environment to enable chat.</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick, watch } from 'vue'

// State
const messages = ref([])
const userInput = ref('')
const isLoading = ref(false)
const isTyping = ref(false)
const displayedText = ref('')
const messagesContainer = ref(null)
const hasApiKey = ref(true) // Will be checked on mount

// Embeddings data (loaded from JSON)
const embeddingsData = ref(null)

// Suggested questions
const suggestions = [
  "What AI projects have you worked on?",
  "Tell me about your cloud experience",
  "What leadership roles have you held?",
  "Which industries have you worked in?"
]

// Load embeddings data
onMounted(async () => {
  try {
    const response = await fetch('/src/data/embeddings.json')
    if (response.ok) {
      embeddingsData.value = await response.json()
    }
  } catch (error) {
    console.log('Embeddings not loaded - run generate_embeddings.py first')
  }
})

// Scroll to bottom when messages change
watch(messages, async () => {
  await nextTick()
  scrollToBottom()
}, { deep: true })

const scrollToBottom = () => {
  if (messagesContainer.value) {
    messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
  }
}

const formatTime = (timestamp) => {
  return new Date(timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
}

const askQuestion = (question) => {
  userInput.value = question
  sendMessage()
}

// Cosine similarity calculation
const cosineSimilarity = (a, b) => {
  let dotProduct = 0
  let normA = 0
  let normB = 0
  for (let i = 0; i < a.length; i++) {
    dotProduct += a[i] * b[i]
    normA += a[i] * a[i]
    normB += b[i] * b[i]
  }
  return dotProduct / (Math.sqrt(normA) * Math.sqrt(normB))
}

// Find relevant context using similarity search
const findRelevantContext = async (query) => {
  if (!embeddingsData.value) {
    return getStaticContext()
  }

  try {
    // Get query embedding from Jina AI (free embeddings)
    const response = await fetch('https://api.jina.ai/v1/embeddings', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${import.meta.env.VITE_JINA_API_KEY}`
      },
      body: JSON.stringify({
        model: 'jina-embeddings-v3',
        task: 'retrieval.query',
        input: [query]
      })
    })

    if (!response.ok) {
      console.warn('Jina API error, falling back to static context')
      return getStaticContext()
    }

    const data = await response.json()
    const queryEmbedding = data.data[0].embedding

    // Calculate similarities and sort
    const similarities = embeddingsData.value.data.map(item => ({
      ...item,
      similarity: cosineSimilarity(queryEmbedding, item.embedding)
    }))

    similarities.sort((a, b) => b.similarity - a.similarity)

    // Get top 3 most relevant chunks
    const topChunks = similarities.slice(0, 3)
    return topChunks.map(chunk => chunk.content).join('\n\n')
  } catch (error) {
    console.error('Error finding context:', error)
    return getStaticContext()
  }
}

// Static context fallback
const getStaticContext = () => {
  return `Robert Weber is a Data Engineering Manager with expertise in agentic AI, cloud architecture,
  data platform development, and engineering team leadership. He has over 10 years of consulting experience.
  Recent projects include an Agentic AI Platform for Travel, Enterprise Cloud Framework Development,
  and Scalable CI/CD Infrastructure. He has expertise in Consulting/Advisory, Leadership, AI/GenAI,
  Cloud Development, Fullstack Engineering, and Data Analytics.`
}

// Send message
const sendMessage = async () => {
  const question = userInput.value.trim()
  if (!question) return

  // Add user message
  messages.value.push({
    role: 'user',
    content: question,
    timestamp: new Date()
  })

  userInput.value = ''
  isLoading.value = true

  try {
    // Find relevant context
    const context = await findRelevantContext(question)

    // Generate response using OpenAI
    const response = await fetch('https://api.openai.com/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${import.meta.env.VITE_OPENAI_API_KEY}`
      },
      body: JSON.stringify({
        model: 'gpt-4o-mini',
        messages: [
          {
            role: 'system',
            content: `You are Robert Weber's digital twin - an AI assistant that answers questions about Robert's professional experience, projects, and expertise.

Answer in first person as if you are Robert. Be friendly, professional, and concise. Base your answers on the following context about Robert:

${context}

If asked about something not covered in the context, politely say you'd be happy to discuss it in person.`
          },
          {
            role: 'user',
            content: question
          }
        ],
        max_tokens: 500,
        temperature: 0.7
      })
    })

    if (!response.ok) {
      throw new Error('API request failed')
    }

    const data = await response.json()
    const assistantMessage = data.choices[0].message.content

    // Add assistant message with typing effect
    messages.value.push({
      role: 'assistant',
      content: assistantMessage,
      timestamp: new Date()
    })

    // Typing effect
    isTyping.value = true
    displayedText.value = ''
    for (let i = 0; i < assistantMessage.length; i++) {
      displayedText.value += assistantMessage[i]
      await new Promise(resolve => setTimeout(resolve, 15))
    }
    isTyping.value = false

  } catch (error) {
    console.error('Error:', error)
    messages.value.push({
      role: 'assistant',
      content: "I apologize, but I'm having trouble connecting right now. Please try again or reach out to Robert directly via the Contact page.",
      timestamp: new Date()
    })
  } finally {
    isLoading.value = false
  }
}
</script>

<style scoped>
.chat-container {
  @apply bg-white dark:bg-mckinsey-navy-dark rounded-lg shadow-lg overflow-hidden;
  @apply border border-corporate-light-gray dark:border-mckinsey-navy-light;
  height: 450px;
  display: flex;
  flex-direction: column;
}

.messages-container {
  @apply flex-1 overflow-y-auto p-6;
}

/* Welcome Message */
.welcome-message {
  @apply text-center py-6;
}

.welcome-icon {
  @apply w-12 h-12 mx-auto mb-3 rounded-full;
  @apply bg-mckinsey-teal/10 flex items-center justify-center;
  @apply text-mckinsey-teal text-xl;
}

.suggestions {
  @apply flex flex-wrap justify-center gap-2;
}

.suggestion-chip {
  @apply px-4 py-2 text-sm rounded-full;
  @apply bg-corporate-off-white dark:bg-mckinsey-navy;
  @apply text-corporate-dark-gray dark:text-corporate-light-gray;
  @apply border border-corporate-light-gray dark:border-mckinsey-navy-light;
  @apply hover:border-mckinsey-teal hover:text-mckinsey-teal;
  @apply transition-all duration-200;
}

/* Messages */
.message {
  @apply flex gap-3 mb-4;
}

.message.user {
  @apply flex-row-reverse;
}

.message-avatar {
  @apply flex-shrink-0;
}

.avatar-img {
  @apply w-8 h-8 rounded-full;
}

.avatar-icon {
  @apply w-8 h-8 rounded-full p-2;
  @apply bg-corporate-light-gray dark:bg-mckinsey-navy-light;
  @apply text-corporate-mid-gray;
}

.message-content {
  @apply max-w-[80%];
}

.message.user .message-content {
  @apply text-right;
}

.message-bubble {
  @apply inline-block px-4 py-3 rounded-2xl;
  @apply text-sm leading-relaxed;
}

.message.assistant .message-bubble {
  @apply bg-corporate-off-white dark:bg-mckinsey-navy;
  @apply text-corporate-dark-gray dark:text-corporate-light-gray;
  @apply rounded-tl-sm;
}

.message.user .message-bubble {
  @apply bg-mckinsey-teal text-white;
  @apply rounded-tr-sm;
}

.message-time {
  @apply block text-xs text-corporate-mid-gray mt-1;
}

/* Typing Indicator */
.typing-indicator {
  @apply flex gap-1;
}

.typing-indicator span {
  @apply w-2 h-2 rounded-full bg-corporate-mid-gray;
  animation: typing 1.4s infinite ease-in-out;
}

.typing-indicator span:nth-child(2) {
  animation-delay: 0.2s;
}

.typing-indicator span:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes typing {
  0%, 60%, 100% {
    transform: translateY(0);
  }
  30% {
    transform: translateY(-4px);
  }
}

.typing-cursor::after {
  content: '|';
  animation: blink 1s infinite;
}

@keyframes blink {
  0%, 50% { opacity: 1; }
  51%, 100% { opacity: 0; }
}

/* Input Area */
.input-area {
  @apply p-4 border-t border-corporate-light-gray dark:border-mckinsey-navy-light;
  @apply bg-corporate-off-white dark:bg-mckinsey-navy;
}

.input-wrapper {
  @apply flex gap-2;
}

.chat-input {
  @apply flex-1 px-4 py-3 rounded-full;
  @apply bg-white dark:bg-mckinsey-navy-dark;
  @apply border border-corporate-light-gray dark:border-mckinsey-navy-light;
  @apply text-corporate-dark-gray dark:text-white;
  @apply placeholder-corporate-mid-gray;
  @apply focus:outline-none focus:border-mckinsey-teal;
  @apply transition-colors duration-200;
}

.send-button {
  @apply w-12 h-12 rounded-full;
  @apply bg-mckinsey-teal text-white;
  @apply hover:bg-mckinsey-navy dark:hover:bg-mckinsey-teal-light;
  @apply disabled:opacity-50 disabled:cursor-not-allowed;
  @apply transition-all duration-200;
}

.input-hint {
  @apply text-xs text-corporate-mid-gray text-center mt-2;
}

/* API Notice */
.api-notice {
  @apply mt-4 p-4 rounded-lg;
  @apply bg-corporate-off-white dark:bg-mckinsey-navy;
  @apply text-sm text-corporate-mid-gray text-center;
}
</style>
