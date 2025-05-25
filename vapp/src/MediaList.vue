<template>
    <div class="all">
        <div class="selector" v-show='mode == "list"'>
            <MediaSelector
                :media="mediaList"
                :person="personList"
                @select_media="selectMedia"
                @select_person="selectPerson"
            ></MediaSelector>
        </div>
        <div class="list" v-show='mode == "list"'>
            <div v-show='selectMid != "" && selectPid != ""'>
                <input
                    type="button"
                    value="ADD NEW RECORD"
                    @click="doAdd"
                ></input>
                <Item
                    v-for="r in items"
                    :key="r.rid"
                    :record="r"
                    @edit="doEdit"></Item>
            </div>
        </div>

        <!-- EDIT -->
        <div v-show='mode == "edit"'>
            <MediaEdit :record="editItem" @fin="doEditFin"></MediaEdit>
        </div>
    </div>
</template>

<style lang="css" scoped>
.all {
    width: 100%;
    height: 100vh;
}
.selector {
    width: 100%;
    height: 5%;
}
.list {
    width: 100%;
    height: 95%;
    overflow-x: hidden;
    overflow-y: scroll;
}
</style>

<script setup lang="ts">
import { ref, type Ref } from "vue"
import { onMounted } from "vue"

import MediaSelector from './components/MediaSelector.vue'
import Item from './components/MediaItem.vue'
import MediaEdit from './MediaEdit.vue'

import type { IFMediaSelectList, IFPersonSelectList, IFItem } from "./scripts/telegram-interface"
import { Telegram } from "./scripts/telegram-common"

import type { MediaItem, PersonItem } from "./components/media-types"
import type { MediaType } from './components/media-types'

const mode: Ref<"list" | "edit"> = ref("list")

// Media一覧
const mediaList: Ref<Array<MediaItem>> = ref([])
// Person一覧
const personList: Ref<Array<PersonItem>> = ref([])

// Item
const items: Ref<Array<MediaType>> = ref([])

// 選択 Media
let selectMid: string = ""
// 選択 Person
let selectPid: string = ""

const editItem: Ref<MediaType> = ref({} as MediaType)

/**
 * 要求送信 Media一覧取得
 * @param pid 
 */
const reqMediaSelectList = (pid: string) => {
    let prm = {
        "pid": pid
    }
    Telegram.post(
        "http://127.0.0.1:8000/api/media/media_selector",
        JSON.stringify(prm),
        replyreqMediaSelectList, null)
}

/**
 * 応答受信時処理 Media一覧
 * @param v 
 */
const replyreqMediaSelectList = (v: string) => {
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

/**
 * 要求送信 Person一覧取得
 * @param pid 
 */
const reqPersonSelectList = (mid: string) => {
    let prm = {
        "mid": mid
    }
    Telegram.post("http://127.0.0.1:8000/api/media/person_selector",
        JSON.stringify(prm),
        replyPersonSelectList, null)
}

/**
 * 応答受信時処理 Person一覧
 * @param v 
 */
const replyPersonSelectList = (v: string) => {
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

const reqMediaItem = (mid: string, pid: string) => {
    let prm = {
        "mid": mid,
        "pid": pid,
    }
    Telegram.post(
        "http://127.0.0.1:8000/api/media/media_item",
        JSON.stringify(prm),
        replyMediaItem, null)
}

const replyMediaItem = (v: string) => {
    try {
        console.log(v)
        let rep: IFItem = JSON.parse(v)
        let lst: Array<MediaType> = []

        rep["item"].forEach((one) => {
            lst.push({
                "rid": one["rid"],
                "media": one["media"]["mname"],
                "person": one["person"]["pname"],
                "release": one["release"],
                "title": one["title"],
                "own": one["own"],
                "note": "",
            })
        })
        items.value = lst
    } catch (e) {
        console.log(e)
    }
}

/**
 * 選択時処理 Media
 * @param mid 
 */
const selectMedia = (mid: string) => {
    console.log(mid)
    selectMid = mid
    if(selectMid == "") {
        reqMediaSelectList("")
    }
    if(selectPid == "") {
        reqPersonSelectList(mid)
    }
    if(selectMid != "" && selectPid != "") {
        reqMediaItem(selectMid, selectPid)
    }
    if(selectMid == "" || selectPid == "") {
        items.value = []
    }
}

/**
 * 選択時処理 Person
 * @param pid 
 */
const selectPerson = (pid: string) => {
    console.log(pid)
    selectPid = pid
    if(selectPid == "") {
        reqPersonSelectList("")
    }
    if(selectMid == "") {
        reqMediaSelectList(pid)
    }
    if(selectMid != "" && selectPid != "") {
        reqMediaItem(selectMid, selectPid)
    }
    if(selectMid == "" || selectPid == "") {
        items.value = []
    }
}

const doAdd = () => {
    console.log("ADD")
}

const doEdit = (rid: string) => {
    console.log("EDIT [" + rid + "]")
    let idx = 0;
    for(; idx < items.value.length; ++idx) {
        let one = items.value[idx]
        if (one.rid == rid) {
            break;
        }
    }
    if(idx >= items.value.length){
        return
    }

    let mi: MediaType = {
        "rid": rid,
        "media": items.value[idx].media,
        "person": items.value[idx].person,
        "title": items.value[idx].title,
        "release": items.value[idx].release,
        "note": items.value[idx].note,
        "own": items.value[idx].own
    }
    editItem.value = mi
    mode.value = "edit"
}

const doEditFin = () => {
    mode.value = "list"
}

onMounted(() => {
    reqMediaSelectList("")
    reqPersonSelectList("")
})

</script>
