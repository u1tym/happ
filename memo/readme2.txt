sudo apt install python3-virtualenv


python 3.12 のインストール
sudo apt install -y build-essential zlib1g-dev libssl-dev libffi-dev python3-pip libsqlite3-dev libbz2-dev libreadline-dev libncursesw5-dev libgdbm-dev liblzma-dev libgdbm-compat-dev
cd /usr/src
sudo wget https://www.python.org/ftp/python/3.12.0/Python-3.12.0.tar.xz
sudo tar -xf Python-3.12.0.tar.xz
cd Python-3.12.0

./configure --enable-optimizations
sudo make -j$(nproc)
sudo make altinstall
python3.12 --version

sudo update-alternatives --install /usr/bin/python python /usr/local/bin/python3.12 1
python --version






<template>
  <div class="scroll-container" ref="containerRef">
    <div class="scroll-text" ref="text1Ref">{{ text1 }}</div>
    <div class="scroll-text" ref="text2Ref">{{ text2 }}</div>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue'

const text1 = 'ABCDEFG'
const text2 = 'あいうえおかきくけこ'

const containerRef = ref(null)
const text1Ref = ref(null)
const text2Ref = ref(null)

let animationFrame
let scrollPos = 0

const scrollSpeed = 1

const scrollTexts = () => {
  const container = containerRef.value
  const text1El = text1Ref.value
  const text2El = text2Ref.value

  const maxScroll1 = text1El.scrollWidth - container.clientWidth
  const maxScroll2 = text2El.scrollWidth - container.clientWidth

  const shouldScroll = maxScroll1 > 0 || maxScroll2 > 0

  if (!shouldScroll) return

  scrollPos += scrollSpeed
  if (scrollPos > Math.max(maxScroll1, maxScroll2)) {
    scrollPos = 0
  }

  text1El.style.transform = `translateX(${-scrollPos}px)`
  text2El.style.transform = `translateX(${-scrollPos}px)`

  animationFrame = requestAnimationFrame(scrollTexts)
}

onMounted(async () => {
  await nextTick()
  scrollTexts()
})
</script>

<style scoped>
.scroll-container {
  width: 200px;
  overflow: hidden;
  white-space: nowrap;
  border: 1px solid #ccc;
  padding: 4px;
}

.scroll-text {
  display: inline-block;
  transition: transform 0.1s linear;
  will-change: transform;
}
</style>
