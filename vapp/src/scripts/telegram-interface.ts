export type IFMediaItem = {
    mid: string
    mname: string
}

export type IFPersonItem = {
    pid: string
    pname: string
}

export type IFMediaSelectList = {
    media: Array<IFMediaItem>
}

export type IFPersonSelectList = {
    person: Array<IFPersonItem>
}

export type IFItemItem = {
    rid: string
    media: IFMediaItem
    person: IFPersonItem
    title: string
    release: string
    own: boolean
}
export type IFItem = {
    item: Array<IFItemItem>
}

export type IFUpdItem = {
    rid: string
    media: string
    person: string
    title: string
    release: string
    own: boolean
}
