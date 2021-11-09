<template>
  <!-- Need to take this out later -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"/>
  
  <section class="hero is-small is-link">
    <div class="hero-body">
      <p class="title">
        <i class="far fa-frown-open"></i> Distributed Pain Tracker
      </p>
    </div>
    <div class="tabs is-centered">
      <ul>
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/create-pain">Create Pain</router-link></li>
        <li><router-link to="/login">
          <span class="icon-text">
            <span class="icon">
              <i :class="loginIcon"></i>
            </span>
            <span>{{ loginText }}</span>
          </span>
        </router-link></li>
      </ul>
    </div>
  </section>
  <section class="section pt-4">
    <div class="container">
      <router-view/>
    </div>
  </section>
</template>

<script>
import store from '../src/store'

export default {
  computed: {
    loginText() {
      if (store.state.token == "TO_BE_DEFINED") {
        return "Login"
      } else {
        return store.state.email
      }
    },
    loginIcon() {
      if (store.state.token == "TO_BE_DEFINED") {
        return "fas fa-sign-in-alt"
      } else {
        return "fas fa-user"
      }
    }
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
