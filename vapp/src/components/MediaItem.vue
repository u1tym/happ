<template>
    <div class="item-all">
        <div class="item-line-1">
            <div class="item-person">{{ person }}</div>
        </div>
        <div class="item-line-2">
            <div class="item-title">{{ title }}</div>
        </div>
    </div>
</template>

<style scoped>
.item-all {
    width: 100%;
    display: flex;
    flex-direction: column;
}
.item-line-1 {
    display: flex;
    flex-direction: row;
}
.item-line-2 {
    display: flex;
    flex-direction: row;
}
</style>

<script setup lang="ts">
import { onMounted, watch } from "vue"
import { ref, type Ref } from "vue"

import type { MediaType } from "./media-types"

const props = defineProps({
    record: Object as () => MediaType
})

const person: Ref<string> = ref(props.record ? props.record.person : "")
const title: Ref<string> = ref(props.record ? props.record.title : "")

onMounted(() => {
    watch(
        () => props.record,
        () => {
            person.value = props.record ? props.record.person : ""
            title.value = props.record ? props.record.title : ""
        }
    )
})
</script>
