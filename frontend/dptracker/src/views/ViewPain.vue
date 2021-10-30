<template>
    <div class="viewpain">
        <div class="container" v-if="painData !== null">
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
                    <div v-for="label in painData.labels" :key="label.id">
                        <span class="tag">{{ label.name }} <button v-if="editEnabled" class="delete is-small">abc</button></span>
                        &nbsp;
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    mounted() {
        fetch(`/api/pains/${ this.$route.params.id }`)
        .then(response => response.json())
        .then(data => this.painData = data);
    },
    data() {
        return {
            painData: null,
            editEnabled: false,
        }
    }
}
</script>
