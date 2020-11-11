<template>
  <v-app>
    <v-app-bar app color="blue-grey" dark>
      <router-link
        class="navbar-brand mx-0"
        to="/"
        style="padding-top: 5px; font-size: 2em"
      >
        <img src="./assets/img/damacia.png" alt="" style="width: 200px" />
      </router-link>

      <v-spacer></v-spacer>
      <a style="color: white" href="/searchpick">대기실 전적검색</a>
      <v-divider vertical class="mx-4" />
      <v-icon @click="darkmode">
        {{
          $vuetify.theme.dark ? "mdi-weather-night" : "mdi-white-balance-sunny"
        }}
      </v-icon>
    </v-app-bar>

    <v-main>
      <SideNavi style="z-index: 6; position: fixed; margin: 64px 0 0 0" />
      <router-view></router-view>
      <v-snackbar v-model="snackbar">{{ errMsg }}</v-snackbar>
    </v-main>
  </v-app>
</template>

<script>
import SideNavi from "./components/common/SideNavi.vue";
// import HelloWorld from './components/HelloWorld';

export default {
  name: "App",

  components: {
    SideNavi,
    // HelloWorld,
  },
  data: () => ({
    snackbar: false,
    errMsg: "",
    theme: localStorage.getItem("dark") == "on" ? true : false,
  }),
  methods: {
    darkmode() {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
      this.$vuetify.theme.dark
        ? localStorage.setItem("dark", "on")
        : localStorage.setItem("dark", "off");
    },
  },
  created() {
    this.$vuetify.theme.dark = this.theme;
  },
};
</script>

<style>
a {
  text-decoration: none;
}
</style>