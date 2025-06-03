export class General {

    static get_random_string = (l: number): string => {
        const S = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return Array.from(Array(l))
            .map(() => S[Math.floor(Math.random() * S.length)])
            .join()
    }
}
