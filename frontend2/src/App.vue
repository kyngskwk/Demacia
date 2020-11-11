<template>
  <v-app>
    <v-app-bar app style="background:linear-gradient(to right, rgb(247,202,201), rgb(146,168,209))" dark>
      <a
        class="navbar-brand mx-0"
        href="/"
        style="padding-top: 5px; font-size: 2em"
      >
        <img src="./assets/img/damacia.png" alt="" style="width: 200px" />
      </a>

      <v-spacer></v-spacer>
      <v-menu transition="slide-y-transition" bottom>
        <template v-slot:activator="{ on, attrs }">
          <v-chip
            class="purple"
            style="background:linear-gradient(to right, rgb(247,202,201), rgb(146,168,209))"
            dark
            v-bind="attrs"
            v-on="on"
          >
            전적 검색
          </v-chip>
        </template>
        <v-list>
          <v-list-item>
            <a style="color: #607d8b" href="">유저 검색</a>
          </v-list-item>
          <v-list-item @click="gopick">
            <a style="color: #607d8b" href="/searchpick">대기실 검색</a>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>

    <v-main>
      <SideNavi style="z-index: 6; position: fixed; margin: 64px 0 0 0" />
      <router-view></router-view>
      <v-snackbar v-model="snackbar">{{ errMsg }}</v-snackbar>
      <Chatbot />
    </v-main>
  </v-app>
</template>

<script>
import SideNavi from "./components/common/SideNavi.vue";
import Chatbot from "./components/chatbot/Chatbot.vue";

// import HelloWorld from './components/HelloWorld';

export default {
  name: "App",

  components: {
    SideNavi,
    // HelloWorld,
    Chatbot,
  },
  data: () => ({
    snackbar: false,
    errMsg: "",
  }),
};
</script>

<style>
a {
  text-decoration: none;
}
</style>