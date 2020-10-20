<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        데마시아
      </div>

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
