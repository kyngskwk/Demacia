<template>
  <v-container fill-height>
    <v-card max-width="85%" class="mx-auto">
      <v-tabs dark grow hide-slider>
        <v-tabs-slider></v-tabs-slider>
        <v-tab style="background:rgb(247,202,201)"> 로그인 </v-tab>
        <v-tab style="background:rgb(146,168,209)"> 회원가입 </v-tab>
        <v-tab-item>
          <Login />
        </v-tab-item>
        <v-tab-item>
          <Join />
        </v-tab-item>
      </v-tabs>
    </v-card>
  </v-container>
</template>

<script>
import Login from "@/components/user/Login";
import Join from "@/components/user/Join";
export default {
  components: {
    Login,
    Join,
  },
};
</script>

<style>
</style>