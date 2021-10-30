<template>
    <div class="viewpain">
        Viewing Pain {{ $route.params.id }}
        {{ painData }}
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
