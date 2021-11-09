import store from '../store'

export async function getRequest(url) {
    let headers = new Headers();
    headers.append('Authorization', `Token ${store.state.token}`)
    return fetch(url, {
        method: 'GET',
        headers: headers
    })
}

export function checkLoggedIn() {
    
}