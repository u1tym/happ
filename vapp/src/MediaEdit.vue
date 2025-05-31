<template>
    <div class="edit-all">
        <table>
            <tbody>

                <tr>
                    <td>media</td>
                    <td><input class="input-field" type="text" v-model="media"></input></td>
                </tr>
                <tr>
                    <td>person</td>
                    <td><input class="input-field" type="text" v-model="person"></input></td>
                </tr>
                <tr>
                    <td>title</td>
                    <td><input class="input-field" type="text" v-model="title"></input></td>
                </tr>
                <tr>
                    <td>release</td>
                    <td><input class="input-field" type="text" v-model="release"></input></td>
                </tr>
                <tr>
                    <td>own</td>
                    <td><input type="checkbox" v-model="own"></input></td>
                </tr>
                <tr>
                    <td>note</td>
                    <td></td>
                </tr>
                </tbody>
            </table>
        <div class="edit-buttons">
            <input type="checkbox" v-model="checkDelete" v-show="rid != ''"></input>
            <input type="button" value="delete" v-show="rid != ''" :disabled="!checkDelete" @click="doDelete"></input>
            <input type="button" value="save" @click="doSave"></input>
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
.input-field {
    width: 95%;
}
</style>

<script setup lang="ts">
import { onMounted, watch } from "vue";
import { type Ref, ref } from "vue"
import type { MediaType } from './components/media-types';
import { Telegram } from "./scripts/telegram-common"
import { Host } from "./scripts/telegram-interface"
import type { IFDelItem, IFUpdItem } from "./scripts/telegram-interface"

const props = defineProps({
    record: Object as () => MediaType
})

const emits = defineEmits(['fin'])

const makeMedia = (v: MediaType | undefined): string => { return v ? v.media : "" }
const makePerson = (v: MediaType | undefined): string => { return v ? v.person : "" }
const makeTitle = (v: MediaType | undefined): string => { return v ? v.title : "" }
const makeOwn = (v: MediaType | undefined) : boolean => { return v ? v.own : false }
const makeRelease = (v: MediaType | undefined): string => { return v ? v.release : "" }

const rid: Ref<string> = ref(props.record ? props.record.rid : "")
const media: Ref<string> = ref(props.record ? makeMedia(props.record) : makeMedia(undefined))
const person: Ref<string> = ref(props.record ? makePerson(props.record) : makePerson(undefined))
const title: Ref<string> = ref(props.record ? makeTitle(props.record) : makeTitle(undefined))
const own: Ref<boolean> = ref(props.record ? makeOwn(props.record) : makeOwn(undefined))
const release: Ref<string> = ref(props.record ? makeRelease(props.record) : makeRelease(undefined))

const checkDelete: Ref<boolean> = ref(false)

const doDelete = () => {
    let prm: IFDelItem = {
        "rid": rid.value,
    }
    console.log(prm)

    Telegram.post(
        Host.urlDeleteItem,
        JSON.stringify(prm),
        reply_DeleteItem, null)    
}

const reply_DeleteItem = (v: string) => {
    emits('fin')
}

const doSave = () => {
    let prm: IFUpdItem = {
        "rid": rid.value,
        "media": media.value,
        "person": person.value,
        "own": own.value,
        "release": release.value ?? "",
        "title": title.value ?? "",
    }

    console.log(prm)

    Telegram.post(
        Host.urlUpdateItem,
        JSON.stringify(prm),
        reply_UpdateItem, null)
}

const reply_UpdateItem = (v: string) => {
    emits('fin')
}

const doReturn = () => {
    emits('fin')
}

onMounted(() => {
    watch(
        () => props.record,
        () => {
            rid.value = props.record ? props.record.rid : ""
            media.value = props.record ? makeMedia(props.record) : makeMedia(undefined)
            person.value = props.record ? makePerson(props.record) : makePerson(undefined)
            title.value = props.record ? makeTitle(props.record) : makeTitle(undefined)
            own.value = props.record ? makeOwn(props.record) : makeOwn(undefined)
            release.value = props.record ? makeRelease(props.record) : makeRelease(undefined)
        }
    )

    watch(title, () => { console.log("更新 title " + title.value) })

})
</script>