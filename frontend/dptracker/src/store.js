import { createStore } from "vuex"

const store = createStore({
    state: {
        token: "TO_BE_DEFINED"
    },
    mutations: {
        updateToken(state, newToken) {
            state.token = newToken
        }
    }
})

export default store