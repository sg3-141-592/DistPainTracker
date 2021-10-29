<template>
  <div class="home">
    Recent Pain

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
    fetch(`${this.apiURL}pains`)
      .then(response => response.json())
      .then(data => console.log(data));
  }
}
</script>
