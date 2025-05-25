<template>
    <div class="selector-all">
        <div>
            <select name="media">
                <option v-for="r in mediaList" :key="r.mid" value="r.pid">{{ r.media }}</option>
            </select>
        </div>
        <div>
            <select name="person">
                <option v-for="r in personList" :key="r.pid" value="r.pid">{{ r.person }}</option>
            </select>
        </div>
    </div>
</template>

<style lang="css" scoped>
.selector-all {
    display: flex;
    flex-direction: row;
}
</style>

<script setup lang="ts">
import { onMounted, watch } from "vue"
import { type Ref, ref } from "vue"

import type { MediaItem, PersonItem } from "./media-types";
import type { SelectorList } from './media-types';

const props = defineProps({
    media: Object as () => Array<MediaItem>,
    person: Object as () => Array<PersonItem>
})

const makeMediaList = (f: Array<MediaItem>): Array<MediaItem> => {
    let ml: Array<MediaItem> = []
    ml.push({"mid": "", "media": "---"})
    if(f === undefined) {
        console.log("f is undefined")
    }else{
        f.forEach((one) => {
            ml.push({"mid": one["mid"], "media": one["media"]})
        })
    }
    return ml
}

const makePersonList = (f: Array<PersonItem>): Array<PersonItem> => {
    let ml: Array<PersonItem> = []
    ml.push({"pid": "", "person": "---"})
    if(f === undefined){
        console.log("f is undefined")
    }
    else{
        f.forEach((one) => {
            ml.push({"pid": one["pid"], "person": one["person"]})
        })
    }
    return ml
}
const mediaList: Ref<Array<MediaItem>> = ref(props.media ? makeMediaList(props.media) : [])
const personList: Ref<Array<PersonItem>> = ref(props.person ? makePersonList(props.person) : [])

console.log("setup MediaSelector")
onMounted(() => {
    console.log("onMounted MediaSelector")
    watch(
        () => props.media,
        () => {
            console.log("watch MediaSelector")
            mediaList.value = props.media ? makeMediaList(props.media) : []
        }
    )
    watch(
        () => props.person,
        () => {
            console.log("watch MediaSelector")
            personList.value = props.person ? makePersonList(props.person) : []
        }
    )
})
</script>
