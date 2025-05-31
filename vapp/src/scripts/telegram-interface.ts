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

export class Host {
    //static readonly address: string = "ytym.sytes.net"
    static readonly address: string = "localhost"
    static readonly port: number = 8000

    static readonly urlSelectMList: string = "http://" + Host.address + ":" + Host.port.toString() + "/api/media/media_selector"
    static readonly urlSelectPList: string = "http://" + Host.address + ":" + Host.port.toString() + "/api/media/person_selector"
    static readonly urlSelectItem: string = "http://" + Host.address + ":" + Host.port.toString() + "/api/media/select_item"
    
    static readonly urlUpdateItem: string = "http://" + Host.address + ":" + Host.port.toString() + "/api/media/update_item"
}