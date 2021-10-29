<template>
  <div class="tabs is-centered">
    <ul>
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/about">About</router-link></li>
      <li><router-link to="/profile">Profile</router-link></li>
    </ul>
  </div>
  <router-view/>
</template>

<script>
import { provide } from 'vue'

export default {
  setup() {
    provide('apiURL', 'https://8000-copper-cat-xkqw0zjh.ws-eu18.gitpod.io/api/')
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
