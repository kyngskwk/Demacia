<template>
  <v-container fill-height>
    <v-card max-width="85%" class="mx-auto">
      <v-tabs background-color="blue-grey" dark grow>
        <v-tab> 로그인 </v-tab>
        <v-tab> 회원가입 </v-tab>
        <v-tab-item>
          <login></login>
        </v-tab-item>
        <v-tab-item>
          <join></join>
        </v-tab-item>
      </v-tabs>
    </v-card>
  </v-container>
</template>

<script>
import login from "@/components/user/Login";
import join from "@/components/user/Join";
export default {
  components: {
    login,
    join,
  },
};
</script>

<style>
</style>