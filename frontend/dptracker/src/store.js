import { createStore } from "vuex"
import { VuexPersistence } from 'vuex-persist'

const store = createStore({
    state: {
        token: "TO_BE_DEFINED"
    },
    mutations: {
        updateToken(state, newToken) {
            state.token = newToken
        }
    },
    plugins: [new VuexPersistence().plugin]
})

export default store