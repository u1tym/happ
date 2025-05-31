<template>
    <div class="selector-all">
        <div class="selector-person">
            <select name="person" v-model="personValue" class="select-common">
                <option v-for="r in personList" :key="r.pid" :value="r.pid">{{ r.person }}</option>
            </select>
        </div>
        <div class="selector-media">
            <select name="media" v-model="mediaValue" class="select-common">
                <option v-for="r in mediaList" :key="r.mid" :value="r.mid">{{ r.media }}</option>
            </select>
        </div>
    </div>
</template>

<style lang="css" scoped>
.selector-all {
    display: flex;
    flex-direction: row;
    width: 100%;
}
.selector-media {
    width: 40%;
}
.selector-person {
    width: 60%;
}
.select-common {
    width: 100%;
    height: 60px;
}
</style>

<script setup lang="ts">
import { onMounted, watch } from "vue"
import { type Ref, ref } from "vue"

import type { MediaItem, PersonItem } from "./media-types";

const props = defineProps({
    media: Object as () => Array<MediaItem>,
    person: Object as () => Array<PersonItem>
})

const emits = defineEmits(['select_media', 'select_person'])

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
const mediaValue: Ref<string> = ref("")
const personValue: Ref<string> = ref("")

onMounted(() => {
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

    watch(
        mediaValue,
        () => {
            //console.log("Media変更 [" + mediaValue.value + "]")
            emits('select_media', mediaValue.value)
        }
    )

    watch(
        personValue,
        () => {
            //console.log("Person変更 [" + personValue.value + "]")
            emits('select_person', personValue.value)
        }
    )

})
</script>
