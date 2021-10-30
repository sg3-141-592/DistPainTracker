<template>
  <div class="home">
    Do any of these resonate with you?
    <ul v-if="recentPain !== null">
      <li v-for="result in recentPain.results" :key="result.id">
        <router-link :to="{ name: 'view-pain', params: { id: result.id }}">
          {{ result.title }} <!-- <i class="far fa-heart"></i> -->
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import { inject } from 'vue'

export default {
  name: 'Home',
  components: { },
  setup() {
    const apiURL = inject('apiURL');

    return {
      apiURL
    }
  },
  mounted() {
    fetch(`/api/pains`)
      .then(response => response.json())
      .then(data => this.recentPain = data);
  },
  data() {
    return {
      recentPain: null
    }
  }
}
</script>
