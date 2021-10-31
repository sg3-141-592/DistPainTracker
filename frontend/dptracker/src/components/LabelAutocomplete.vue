<template>
    Select Labels
</template>

<script>
import store from '../store'

export default {
    mounted() {
        let headers = new Headers();
        headers.append('Authorization', `Token ${store.state.token}`)
        fetch(`/api/labels`, {
            method: 'GET',
            headers: headers
        })
            .then(function(response) {
                return response.json()
            })
            .then(data => this.labels = data.results)
    },
    data () {
        return {
            labels: []
        }
    }
}
</script>