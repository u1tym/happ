export type MediaItem = {
    mid: string
    media: string
}

export type PersonItem = {
    pid: string
    person: string
}

export type SelectorList = {
    media: Array<MediaItem>
    person: Array<PersonItem>
}

export type MediaType = {
    media: string
    person: string
    title: string
    release: string
}

