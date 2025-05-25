<template>
    <div class="item-all">
        <div class="item-line-1">
            <div class="item-person">{{ person }}</div>
            <input type="button" value="EDIT" @click="clickEdit"></input>
        </div>
        <div class="item-line-2">
            <div class="item-own">
                <input type="checkbox" :checked="own" disabled class="item-own"></input>
            </div>
            <div class="item-title">{{ title }}</div>
        </div>
    </div>
</template>

<style scoped>
.item-all {
    width: 99%;
    display: flex;
    flex-direction: column;
    border: 1px solid #000;
}
.item-line-1 {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
}
.item-line-2 {
    display: flex;
    flex-direction: row;
}

.item-own input[type="checkbox"]:disabled {
    filter: brightness(0.9) sepia(1) hue-rotate(200deg) saturate(500%);
}

</style>

<script setup lang="ts">
import { onMounted, watch } from "vue"
import { ref, type Ref } from "vue"

import type { MediaType } from "./media-types"

const props = defineProps({
    record: Object as () => MediaType
})
const emits = defineEmits(['edit'])

const person: Ref<string> = ref(props.record ? props.record.person : "")
const title: Ref<string> = ref(props.record ? props.record.title : "")
const own: Ref<boolean> = ref(props.record ? props.record.own : false)

const clickEdit = () => {
    emits('edit', props.record?.rid)
}

onMounted(() => {
    watch(
        () => props.record,
        () => {
            person.value = props.record ? props.record.person : ""
            title.value = props.record ? props.record.title : ""
            own.value = props.record ? props.record.own : false
        }
    )
})
</script>
