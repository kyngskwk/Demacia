<template>
  <v-container fill-height>
    <v-card max-width="85%" class="mx-auto">
      <v-tabs background-color="blue-grey" dark grow>
        <v-tab> 로그인 </v-tab>
        <v-tab> 회원가입 </v-tab>
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