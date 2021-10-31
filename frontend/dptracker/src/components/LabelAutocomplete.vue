<template>
    <div class="field">
        <label class="label">Labels</label>
        <div class="dropdown is-active">
            <div class="dropdown-trigger">
                <div class="field">
                    <p class="control is-expanded has-icons-right">
                        <input class="input" type="search" @focus="labelDropdownVisible = true"
                            @blur="labelDropdownVisible = false" placeholder="Add label..."/>
                        <span class="icon is-small is-right"><i class="fas fa-tag"></i></span>
                    </p>
                </div>
            </div>
            <div v-if="labelDropdownVisible" class="dropdown-menu" role="menu">
                <div class="dropdown-content">
                    <a v-for="label in labels" :key="`label-${label}`"
                        @mousedown="addLabel(label)" class="dropdown-item">
                        {{ label.name }}
                    </a>
                </div>
            </div>
        </div>
    </div>
    <div class="field">
        <div class="tags are-medium">
            <span v-for="label in selectedLabels" :key="label.id" class="tag">
                {{ label.name }}&nbsp;
                <button @click="deleteLabel(label)" class="delete is-small"></button>
            </span>
        </div>
    </div>
</template>

<script>
import store from '../store'

export default {
    mounted() {
        let headers = new Headers();
        headers.append('Authorization', `Token ${store.state.token}`)
        fetch(`/api/labels/`, {
            method: 'GET',
            headers: headers
        })
            .then(function(response) {
                return response.json()
            })
            .then(data => this.labels = data.results)
    },
    emits: ['changedLabels'],
    methods: {
        addLabel: function(label) {
            this.selectedLabels.push(label)
            // Convert array of structs to array of labels
            let arrayLabels = []
            this.selectedLabels.forEach(element => {
                arrayLabels.push(element.id)
            });
            this.$emit('changedLabels', arrayLabels)
        },
        deleteLabel: function(label) {
            var index = this.selectedLabels.indexOf(label);
            if (index !== -1) {
                this.selectedLabels.splice(index, 1);
            }
            // Convert array of structs to array of labels
            let arrayLabels = []
            this.selectedLabels.forEach(element => {
                arrayLabels.push(element.id)
            });
            this.$emit('changedLabels', arrayLabels)
        }
    },
    data () {
        return {
            labelDropdownVisible: false,
            labels: [],
            selectedLabels: []
        }
    }
}
</script>