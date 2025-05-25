<template>
    <div class="edit-all">
        <table>
            <tr>
                <td>media</td>
                <td><input type="text" :value="item.media"></input></td>
            </tr>
            <tr>
                <td>person</td>
                <td><input type="text" :value="item.person"></input></td>
            </tr>
            <tr>
                <td>title</td>
                <td><input type="text" :value="item.title"></input></td>
            </tr>
            <tr>
                <td>release</td>
                <td><input type="text" :value="item.release"></input></td>
            </tr>
            <tr>
                <td>own</td>
                <td><input type="checkbox" :checked="item.own"></input></td>
            </tr>
            <tr>
                <td>note</td>
                <td></td>
            </tr>
        </table>
        <div class="edit-buttons">
            <input type="button" value="save"></input>
            <input type="button" value="return" @click="doReturn"></input>
        </div>
    </div>
</template>

<style lang="css" scoped>
.edit-all {
    display: flex;
    flex-direction: column;
}
.edit-buttons {
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
}
</style>

<script setup lang="ts">
import { onMounted, watch } from "vue";
import { type Ref, ref } from "vue"
import type { MediaType } from './components/media-types';

const props = defineProps({
    record: Object as () => MediaType
})

const emits = defineEmits(['fin'])

const makeItem = (v: MediaType | undefined): MediaType => {
    let r: MediaType = {
        "rid": "",
        "media": "",
        "person": "",
        "title": "",
        "release": "",
        "own": false,
        "note": ""
    }
    if (v === undefined) {
        console.log("v is undefined")
    } else {
        r.rid = v.rid
        r.media = v.media
        r.person = v.person
        r.title = v.title
        r.release = v.release
        r.own = r.own
        r.note = r.note
    }
    return r
}
const item: Ref<MediaType> = ref(props.record ? makeItem(props.record) : makeItem(undefined))

const doReturn = () => {
    emits('fin')
}

onMounted(() => {
    watch(
        () => props.record,
        () => {
            item.value = props.record ? makeItem(props.record) : makeItem(undefined)
        }
    )
})
</script>