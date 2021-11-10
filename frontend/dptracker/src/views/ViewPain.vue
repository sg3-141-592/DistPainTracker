<template>
    <div class="viewpain">
        <!-- -->
        <div class="container" v-if="painData !== null">
            <upvote :votes="painData.vote_count" :can_vote="painData.can_vote"
                :pain_id="painData.id" @voteChanged="reloadPage()"></upvote>
            <div class="field">
                <h3 class="title is-3">{{ painData.title }}</h3>
            </div>

            <div class="field">
                <div v-html="painData.description" class="content"></div>
            </div>

            <div class="field">
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

        <br>
        <div class="field">
            <label class="label">New Comment</label>
            <div class="control">
                <QuillEditor contentType="html" v-model:content="newComment" theme="snow"/>
            </div>
        </div>
        <div class="field">
            <div class="control">
                <button class="button is-link" v-on:click="createComment">Create</button>
            </div>
        </div>

        <!-- -->
        <div class="container" v-if="commentData !== null">
            <div v-for="result in commentData.results" :key="result.id">
                <div v-html="result.text" class="content"></div>
                {{ result.user }} - {{ result.created }}
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
    methods : {
        reloadPage() {
            let headers = new Headers()
            headers.append('Authorization', `Token ${store.state.token}`)

            // Get pain data
            fetch(`/api/pains/${ this.$route.params.id }/`, {
                method: 'GET',
                headers: headers
            })
                .then(response => response.json())
                .then(data => this.painData = data);
            
            // Get comments data for current pain /api/comments/?pain=1
            fetch(`/api/comments/?pain=${ this.$route.params.id }`, {
                method: 'GET',
                headers: headers
            })
                .then(response => response.json())
                .then(data => this.commentData = data);
        },
        createComment() {
            let headers = new Headers({
                    'Accept': 'application/json, text/plain, */*',
                    'Content-Type': 'application/json'
                });
            headers.append('Authorization', `Token ${store.state.token}`)

            fetch(`/api/comments/`, {
                method: 'POST',
                headers: headers,
                body: JSON.stringify({
                    pain: this.$route.params.id,
                    text: this.newComment,
                })
            })
                .then(response => response.json())
                .then(() => {
                    this.reloadPage()
                })
        }
    },
    mounted() {
        this.reloadPage()
    },
    data() {
        return {
            painData: null,
            commentData: null,
            editEnabled: false,
            newComment: null,
        }
    }
}
</script>
