<template>
    <div class="field">
        <label class="label">{{ votes }} votes</label>
        <button class="button" @click="VotePressed()" :disabled="!buttonEnabled">
            <span class="icon">
            <i :class="editIcon"></i>
            </span>
            <span>{{ editText }}</span>
    </button>
    </div>
</template>

<script>
import store from '../store'

export default ({
    props: ['votes', 'can_vote', 'pain_id'],
    emits: ['voteChanged'],
    computed: {
        editText: function() {
            if (this.can_vote == -1) {
                return "Upvote"
            } else {
                return "Remove vote"
            }
        },
        editIcon: function() {
            if (this.can_vote == -1) {
                return "fas fa-sort-up"
            } else {
                return "fas fa-eraser"
            }
        }
    },
    methods: {
        VotePressed : function() {
            
            this.buttonEnabled = false

            let headers = new Headers({
                'Accept': 'application/json, text/plain, */*',
                'Content-Type': 'application/json'
            });
            headers.append('Authorization', `Token ${store.state.token}`)

            if (this.can_vote == -1) {
                //"Upvote"
                fetch(`/api/votes/`, {
                    method: 'POST',
                    headers: headers,
                    body: JSON.stringify({
                        pain: this.pain_id
                    })
                })
                    .then(function() {
                        this.$emit('voteChanged')
                    }.bind(this))
            } else {
                //"Remove vote"
                fetch(`/api/votes/${this.can_vote}/`, {
                    method: 'DELETE',
                    headers: headers
                })
                    .then(function() {
                        this.$emit('voteChanged')
                    }.bind(this))
            }
            this.buttonEnabled = true
        }
    },
    data() {
        return {
            buttonEnabled: true
        }
    }
})
</script>
