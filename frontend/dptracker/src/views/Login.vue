<template>
    <div class="login">
        <div class="field">
            <label class="label">E-mail</label>
            <div class="control">
                <input v-model="email" class="input" type="text">
            </div>
        </div>

        <div class="field">
            <label class="label">Password</label>
            <div class="control">
                <input v-model="password" class="input" type="password">
            </div>
        </div>

        <div class="field">
            <div class="control">
                <button class="button" v-on:click="submitPassword">Submit</button>
            </div>
        </div>
    </div>
</template>

<script>
import store from '../store'

export default {
    methods: {
        submitPassword: function () {
            fetch('/api/api-token-auth/', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json, text/plain, */*',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    username: this.email,
                    password: this.password
                })
            })
                .then(response => response.json()) 
                .then(function(json) {
                    store.commit('updateToken', {
                        'token': json.token,
                        'email': this.email
                    })
                }.bind(this));
        }
    },
    data() {
        return {
            email: null,
            password: null,
        }
    }
}
</script>
