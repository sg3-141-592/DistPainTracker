import { createStore } from "vuex"
import { VuexPersistence } from 'vuex-persist'

const store = createStore({
    state: {
        token: "TO_BE_DEFINED",
        email: "TO_BE_DEFINED"
    },
    mutations: {
        updateToken(state, payload) {
            state.token = payload.token
            state.email = payload.email
        }
    },
    plugins: [new VuexPersistence().plugin]
})

export default store