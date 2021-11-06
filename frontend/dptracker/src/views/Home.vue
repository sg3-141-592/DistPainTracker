<template>
  <div class="home">
    Do any of these resonate with you?
    <ul v-if="recentPain !== null">
      <li v-for="result in recentPain.results" :key="result.id">
        <router-link :to="{ name: 'view-pain', params: { id: result.id }}">
          {{ result.title }} - {{ result.vote_count }} <!-- <i class="far fa-heart"></i> -->
        </router-link>
      </li>
    </ul>
    <br>
  </div>
</template>

<script>
import { inject } from 'vue'
import store from '../store'
import router from '../router/index.js' 

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
    let headers = new Headers();
    headers.append('Authorization', `Token ${store.state.token}`)
    fetch(`/api/pains/`, {
      method: 'GET',
      headers: headers
    })
      .then(function(response) {
        if (response.status === 401) {
          console.log("Unauthorized, redirecting ...");
          router.push({name: 'login'})
        }
        return response.json()
      })
      .then(data => this.recentPain = data)
  },
  data() {
    return {
      recentPain: null
    }
  }
}
</script>
