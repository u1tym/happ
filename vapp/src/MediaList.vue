<template>
    <div>
        <MediaSelector :media="mediaList" :person="personList"></MediaSelector>
        <Item :record="a" />

    </div>
</template>

<style lang="css" scoped>
</style>

<script setup lang="ts">
import { ref, type Ref } from "vue"
import { onMounted } from "vue"

import MediaSelector from './components/MediaSelector.vue'
import Item from './components/MediaItem.vue'

import type { IFMediaSelectList, IFPersonSelectList } from "./scripts/telegram-interface"
import { Telegram } from "./scripts/telegram-common"

import type { MediaItem, PersonItem } from "./components/media-types"
import type { MediaType } from './components/media-types'

const mediaList: Ref<Array<MediaItem>> = ref([])
const personList: Ref<Array<PersonItem>> = ref([])

const reqMediaSelectList = () => {
    let prm = {
        "pid": ""
    }
    Telegram.post("http://127.0.0.1:8000/api/media/media_selector", JSON.stringify(prm), replyreqMediaSelectList, null)
}

const replyreqMediaSelectList = (v: string) => {
    console.log(v)
    try {
        let rep: IFMediaSelectList = JSON.parse(v)
        let lst: Array<MediaItem> = [] 

        rep["media"].forEach((one) => {
            lst.push({
                "mid": one["mid"],
                "media": one["mname"]
            })
        })
        mediaList.value = lst
    } catch (e){
        console.log(e)
    }
}

const reqPersonSelectList = () => {
    let prm = {
        "mid": ""
    }
    Telegram.post("http://127.0.0.1:8000/api/media/person_selector", JSON.stringify(prm), replyPersonSelectList, null)
}

const replyPersonSelectList = (v: string) => {
    console.log(v)
    try {
        let rep: IFPersonSelectList = JSON.parse(v)
        let lst: Array<PersonItem> = [] 

        rep["person"].forEach((one) => {
            lst.push({
                "pid": one["pid"],
                "person": one["pname"]
            })
        })
        personList.value = lst
    } catch (e){
        console.log(e)
    }
}

onMounted(() => {
    reqMediaSelectList()
    reqPersonSelectList()
    //reqSelectList()
})

const a: Ref<MediaType> = ref({
    "media": "CD",
    "person": "太郎",
    "release": "",
    "title": "あいうえお",
})
</script>
