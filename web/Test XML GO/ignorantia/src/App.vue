<template>
  <v-app>
    <v-content>
  <div id="app">

    <router-view/>
  </div>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Courier', Courier, Arial, serif;
  font-size:1.2em;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  background-color: #ADD8E6;

 }
</style>
