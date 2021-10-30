<template>
    <div class="container" v-if="labelData !== null">
        <h1 class="is-size-3">{{ labelData.name }}</h1>
        <ul>
            <li v-for="pain in labelData.pain" :key="pain.id">
                <router-link :to="{ name: 'view-pain', params: { id: pain.id }}">
                    {{ pain.title }}
                </router-link>
            </li>
        </ul>
    </div>
</template>

<script>
import store from '../store'

export default {
    mounted() {
        let headers = new Headers();
        headers.append('Authorization', `Token ${store.state.token}`)
        fetch(`/api/labels/${ this.$route.params.id }`, {
            method: 'GET',
            headers: headers
        })
            .then(response => response.json())
            .then(data => this.labelData = data);
    },
    data() {
        return {
            labelData: null
        }
    }
}
</script>
