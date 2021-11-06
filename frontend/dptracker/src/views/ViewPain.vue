<template>
    <div class="viewpain">
        <div class="container" v-if="painData !== null">
            <upvote :votes="painData.vote_count" :can_vote="painData.can_vote"
                :pain_id="painData.id" @voteChanged="reloadPage()"></upvote>
            <div class="field">
                <label class="label">Title</label>
                <div class="control">
                    <input class="input" type="text" :value="painData.title" :disabled="!editEnabled">
                </div>
            </div>

            <div class="field">
                <label class="label">Description</label>
                <div class="control">
                    <textarea class="textarea" :value="painData.description" :disabled="!editEnabled"></textarea>
                </div>
            </div>

            <div class="field">
                <label class="label">Labels</label>
                <div class="tags are-medium">
                    <span v-for="label in painData.labels" :key="label.id" class="tag">
                        <router-link :to="{ name: 'view-label', params: { id: label.id }}">
                        {{ label.name }}
                        </router-link>
                        <button v-if="editEnabled" class="delete is-small"></button>
                    </span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import store from '../store'
import Upvote from '../components/Upvote.vue'

export default {
    components: {
        Upvote
    },
    methods: {
        reloadPage : function() {
            let headers = new Headers();
            headers.append('Authorization', `Token ${store.state.token}`)

            fetch(`/api/pains/${ this.$route.params.id }/`, {
                method: 'GET',
                headers: headers
            })
                .then(response => response.json())
                .then(data => this.painData = data);
        }
    },
    mounted() {
        this.reloadPage()
    },
    data() {
        return {
            painData: null,
            editEnabled: false,
        }
    }
}
</script>
