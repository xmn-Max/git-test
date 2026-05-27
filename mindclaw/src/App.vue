<template>
  <div class="app">

    <h1>MindClaw AI</h1>

    <div class="chat-box">

      <div
        v-for="(msg, index) in messages"
        :key="index"
        :class="msg.role"
      >
        {{ msg.text }}
      </div>

    </div>

    <div class="input-area">

      <input
        v-model="inputText"
        placeholder="请输入内容..."
        @keyup.enter="sendMessage"
      />

      <button @click="sendMessage">
        发送
      </button>

    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue'

const inputText = ref('')

const messages = ref([
  {
    role: 'ai',
    text: '你好，我是 MindClaw AI'
  }
])

async function sendMessage() {

  if (!inputText.value) return

  const userText = inputText.value

  // 用户消息
  messages.value.push({
    role: 'user',
    text: userText
  })

  // 清空输入框
  inputText.value = ''

  // 请求 Flask API
  const res = await fetch(
    'http://127.0.0.1:5000/chat?msg=' + userText
  )

  const data = await res.json()

  // AI消息
  messages.value.push({
    role: 'ai',
    text: data.reply
  })

}
</script>

<style>

body {
  margin: 0;
  background: #111;
  font-family: Arial;
}

.app {
  color: white;
  max-width: 900px;
  margin: auto;
  padding-top: 50px;
}

h1 {
  text-align: center;
  font-size: 60px;
}

.chat-box {
  height: 500px;
  background: #1e1e1e;
  border-radius: 20px;
  padding: 20px;
  overflow-y: auto;
}

.user {
  background: #42b883;
  padding: 15px;
  border-radius: 12px;
  margin: 10px 0;
  text-align: right;
}

.ai {
  background: #333;
  padding: 15px;
  border-radius: 12px;
  margin: 10px 0;
}

.input-area {
  display: flex;
  margin-top: 20px;
  gap: 10px;
}

input {
  flex: 1;
  padding: 15px;
  border-radius: 12px;
  border: none;
  font-size: 18px;
}

button {
  width: 120px;
  border: none;
  border-radius: 12px;
  background: #42b883;
  color: white;
  font-size: 18px;
  cursor: pointer;
}

</style>