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
    rid: string
    media: string
    person: string
    title: string
    release: string
    own: boolean
    note: string
}

