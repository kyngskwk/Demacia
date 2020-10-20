<template>
  <v-app>
    <v-app-bar
      app
      color="indigo darken-1"
      dark
    >
      <a
        class="navbar-brand mx-0"
        href="/"
        style="padding-top: 5px; font-size: 2em"
      >
        <img src="./assets/img/damacia.png" alt="" style="width: 200px" />
      </a>

      <v-spacer></v-spacer>
    </v-app-bar>

    <v-main> 
      <SideNavi style="z-index:6"/>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
import SideNavi from './components/common/SideNavi.vue'
// import HelloWorld from './components/HelloWorld';

export default {
  name: 'App',

  components: {
    SideNavi,
    // HelloWorld,
  },
  data: () => ({
    //
  }),
};
</script>
