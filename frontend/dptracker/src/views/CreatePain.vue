<template>
    <div class="create-pain">
        <div class="container">
            <div class="field">
                <label class="label">Title</label>
                <div class="control">
                    <input v-model="title" class="input" type="text">
                </div>
            </div>

            <div class="field">
                <label class="label">Description</label>
                <div class="control">
                    <QuillEditor contentType="html" v-model:content="description" theme="snow"/>
                </div>
            </div>

            <label-autocomplete @changedLabels="selectedLabels = $event"></label-autocomplete>

            <div class="field">
                <div class="control">
                    <button class="button" v-on:click="submitPain">Create</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import store from '../store'
import router from '../router/index.js'
import LabelAutocomplete from '../components/LabelAutocomplete.vue'

export default {
    components: {
        LabelAutocomplete,
    },
    methods: {
        submitPain: function () {
            let headers = new Headers({
                    'Accept': 'application/json, text/plain, */*',
                    'Content-Type': 'application/json'
                });
            headers.append('Authorization', `Token ${store.state.token}`)

            fetch(`/api/pains/`, {
                method: 'POST',
                headers: headers,
                body: JSON.stringify({
                    title: this.title,
                    description: this.description,
                    labels: this.selectedLabels
                })
            })
                .then(response => response.json())
                .then(data => router.push({name: 'view-pain', params: {id: data.id} }));
        }
    },
    data () {
        return {
            title: "",
            description: "",
            selectedLabels: [],
        }
    }
}
</script>
