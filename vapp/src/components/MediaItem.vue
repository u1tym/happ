<template>
    <div class="item-all">

        <div class="item-line-1">
            <div class="item-line-1-l">

                <!-- 所持マーク -->
                <div class="item-own" @click="clickEdit">
                    <div class="check-mark">
                        {{ checkMark }}
                    </div>
                </div>

                <!-- メディア -->
                <div class="item-media" v-if="mediaCode == ''">
                    [ {{ media }} ]
                </div>

                <!-- タイトル -->
                <div class="item-title">
                    <span>{{ title }}</span>
                </div>
            </div>
        </div>
        <div class="item-line-2" v-if="false">
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
    align-items: center;
}
.item-line-2 {
    display: flex;
    flex-direction: row;
    margin-left: 5px;
}

.item-own input[type="checkbox"]:disabled {
    filter: brightness(0.9) sepia(1) hue-rotate(200deg) saturate(500%);
}

@keyframes scrollText {
    0% { transform: translateX(0); }
    60% { transform: translateX(0); }
    100% { transform: translateX(-100%); }
}
.item-own,
.item-media {
    flex: none;
}
.item-media {
    margin-right: 5px;
}
.item-title {
    flex: 1;
    font-size: larger;
    white-space: nowrap;
    overflow-x: hidden;
    text-overflow: ellipsis;
    position: relative;
}
.item-title span {
    display: inline-block;
    /* animation: scrollText 10s linear 2s infinite; */
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
    record: Object as () => MediaType,
    mediaCode: String,
})
const emits = defineEmits(['edit'])

const person: Ref<string> = ref(props.record ? props.record.person : "")
const media: Ref<string> = ref(props.record ? props.record.media : "")
const title: Ref<string> = ref(props.record ? props.record.title : "")
const own: Ref<boolean> = ref(props.record ? props.record.own : false)

const mediaCode: Ref<string> = ref(props.mediaCode ? props.mediaCode : "")

const clickEdit = () => {
    emits('edit', props.record?.rid)
}

const checkMark = computed(() => {
    return own.value ? "✔" : "　"
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
    watch(
        () => props.mediaCode,
        () => {
            mediaCode.value = props.mediaCode ? props.mediaCode : ""
        }
    )
})
</script>
