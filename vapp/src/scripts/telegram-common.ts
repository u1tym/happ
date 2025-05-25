export class Telegram {

    static get = async (
        url: string,
        request: {[k: string]: string | number | boolean} | null,
        success: ((reply: string) => void) | null,
        error: ((reply: string) => void) | null,
    ) => {

        const opt = {
            method: 'GET',
            mode: 'cors' as RequestMode,
            Credentials: 'include' as RequestCredentials,
            headers: new Headers({
                'Content-Type': 'application/json;charset=UTF-8',
            })
        }

        let sendUrl = url
        if (request != null) {
            Object.keys(request).map((k, i) => {
                sendUrl += i == 0 ? '?' : '&'
                sendUrl += k + '=' + request[k]
            })
        }

        const res = await fetch(sendUrl, opt)
        const status = Math.floor(res.status / 100)
        if (status == 2) {
            if (success != null) {
                const reply = JSON.stringify(await res.json())
                success(reply)
            }
        } else {
            if (error != null) {
                const reply = await res.text()
                error(reply)
            }
        }
    }

    static post = async (
        url: string,
        request: string,

        success: ((reply: string) => void) | null,
        error: ((reply: string) => void) | null,
    ) => {

        const opt = {
            method: 'POST',
            mode: 'cors' as RequestMode,
            Credentials: 'include' as RequestCredentials,
            body: request,
            headers: new Headers({
                'Content-Type': 'application/json;charset=UTF-8',
            })
        }

        let sendUrl = url

        const res = await fetch(sendUrl, opt)
        const status = Math.floor(res.status / 100)
        if (status == 2) {
            if (success != null) {
                const reply = JSON.stringify(await res.json())
                success(reply)
            }
        } else {
            if (error != null) {
                const reply = await res.text()
                error(reply)
            }
        }
    }
}
