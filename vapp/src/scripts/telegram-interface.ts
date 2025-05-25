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