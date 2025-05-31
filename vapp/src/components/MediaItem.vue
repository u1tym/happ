<template>
    <div class="item-all">
        <div class="item-line-1">
            <div class="item-line-1-l">
                <div class="item-own">
                    <div class="check-mark">
                        {{ checkMark }}
                    </div>
                </div>
                <div class="item-person">{{ person }} [ {{ media }} ]</div>
            </div>
            <input type="button" value="EDIT" @click="clickEdit"></input>
        </div>
        <div class="item-line-2">
            
            <div class="item-title">{{ title }}</div>
        </div>
    </div>
</template>

<style scoped>
.item-all {
    width: 99%;
    display: flex;
    flex-direction: column;
    border: 1px dotted #000;
    border-radius: 7px;
}
.item-line-1 {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    margin-left: 5px;
    margin-right: 5px;
}
.item-line-1-l {
    display: flex;
    flex-direction: row;
}
.item-line-2 {
    display: flex;
    flex-direction: row;
    margin-left: 5px;
}

.item-own input[type="checkbox"]:disabled {
    filter: brightness(0.9) sepia(1) hue-rotate(200deg) saturate(500%);
}
.item-title {
    font-size: larger;
}
.check-mark {
    display: inline-block;
    width: 20px;
    height: 20px;
    border: 1px solid #000;
    border-radius: 4px; /* 角を少し丸く */
    text-align: center;
    line-height: 20px;
    font-size: 20px;
    color: #000;
    cursor: pointer;
    margin-right: 4px;
}
</style>

<script setup lang="ts">
import { onMounted, watch } from "vue"
import { computed } from "vue"
import { ref, type Ref } from "vue"

import type { MediaType } from "./media-types"

const props = defineProps({
    record: Object as () => MediaType
})
const emits = defineEmits(['edit'])

const person: Ref<string> = ref(props.record ? props.record.person : "")
const media: Ref<string> = ref(props.record ? props.record.media : "")
const title: Ref<string> = ref(props.record ? props.record.title : "")
const own: Ref<boolean> = ref(props.record ? props.record.own : false)

const clickEdit = () => {
    emits('edit', props.record?.rid)
}

const checkMark = computed(() => {
    return own.value ? "✔" : ""
})
onMounted(() => {
    watch(
        () => props.record,
        () => {
            person.value = props.record ? props.record.person : ""
            media.value = props.record ? props.record.media : ""
            title.value = props.record ? props.record.title : ""
            own.value = props.record ? props.record.own : false
        }
    )
})
</script>
