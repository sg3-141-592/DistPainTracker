<template>
    <div class="field">
        <label class="label">Labels</label>
        <div class="dropdown is-active">
            <div class="dropdown-trigger">
                <div class="field">
                    <p class="control is-expanded has-icons-right">
                        <input class="input" type="search" @focus="labelDropdownVisible = true"
                            @blur="labelDropdownVisible = false" v-model="labelSearchTerm" placeholder="Add label..."/>
                        <span class="icon is-small is-right"><i class="fas fa-tag"></i></span>
                    </p>
                </div>
            </div>
            <div v-if="labelDropdownVisible" class="dropdown-menu" role="menu">
                <div class="dropdown-content">
                    <!-- Optional create new label feature -->

                    <div v-if="createNewLabel">
                        <a class="dropdown-item" @mousedown="createLabel">Create label: {{ labelSearchTerm }}</a>
                        <hr class="dropdown-divider">
                    </div>
                    <a v-for="label in visibleLabelList" :key="`label-${label}`"
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
        this.loadLabels()
        this.labelSearchTerm = ""
    },
    emits: ['changedLabels'],
    computed: {
        createNewLabel() {
            if(this.labelSearchTerm.length < 3) {
                return false
            }
            let match = false
            this.labels.forEach(function(element) {
                if(this.labelSearchTerm.toUpperCase()
                    === element.name.toUpperCase()){
                    match = true
                }
            }.bind(this))
            return !match
        },
        visibleLabelList() {
            // Filter any labels that have already been used
            let filteredLabels = []
            this.labels.forEach(function(element) {
                var index = this.selectedLabels.indexOf(element); 
                if (index == -1) {
                    filteredLabels.push(element)
                } 
            }.bind(this))
            
            if(this.labelSearchTerm.length > 0) {
                let newLabels = []
                filteredLabels.forEach(function(element) {
                    // If the label matches the search term
                    if (element.name.match(new RegExp(this.labelSearchTerm, 'i')) != null) {
                        newLabels.push(element);
                    }
                }.bind(this))
                return newLabels
            }
            else
            {
                return filteredLabels
            }
        }
    },
    methods: {
        loadLabels: function() {
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
        addLabel: function(label) {
            // Check if label is already in the list
            if (!this.selectedLabels.includes(label)) {
                this.selectedLabels.push(label)
                // Convert array of structs to array of labels
                let arrayLabels = []
                this.selectedLabels.forEach(element => {
                    arrayLabels.push(element.id)
                });
                this.$emit('changedLabels', arrayLabels)   
            }
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
        },
        createLabel: function() {
            let headers = new Headers({
                'Accept': 'application/json, text/plain, */*',
                'Content-Type': 'application/json'
            });
            headers.append('Authorization', `Token ${store.state.token}`)

            fetch(`/api/labels/`, {
                method: 'POST',
                headers: headers,
                body: JSON.stringify({
                    name: this.labelSearchTerm
                })
            })
                .then(response => response.json())
                .then(function(data) {
                    console.log(data.id)
                    this.loadLabels()
                    this.addLabel({
                        id:data.id,
                        name: this.labelSearchTerm
                    })
                }.bind(this))
        }
    },
    data () {
        return {
            labelDropdownVisible: false,
            labels: [],
            selectedLabels: [],
            labelSearchTerm: "",
        }
    }
}
</script>