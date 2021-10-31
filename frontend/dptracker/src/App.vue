<template>
  <!-- Need to take this out later -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"/>
  
  <section class="hero is-small">
    <div class="hero-body">
      <p class="title">
        <i class="far fa-frown-open"></i> Distributed Pain Tracker
      </p>
    </div>
  </section>
  <div class="tabs is-centered">
    <ul>
      <li><router-link to="/">Home</router-link></li>
      <li><router-link to="/create-pain">Create Pain</router-link></li>
      <li><router-link to="/login">Login</router-link></li>
    </ul>
  </div>
  <section class="section">
    <router-view/>
  </section>
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
  color: #2c3e50;
}
</style>
