<template>
  <v-navigation-drawer absolute permanent right expand-on-hover>
    <v-list v-if="!user">
      <v-list-item link @click="goLogin">
        <v-list-item-content>
          <v-list-item-icon>
            <v-icon>mdi-login</v-icon>
          </v-list-item-icon>
        </v-list-item-content>
        <v-list-item-title class="title">
          <v-icon>mdi-login</v-icon> 로그인 하세요
        </v-list-item-title>
      </v-list-item>
    </v-list>
    <v-list v-else>
      <v-list-item class="px-2">
        <v-list-item-avatar>
          <!-- <v-img :src="window.location.pathname + '/' + user.userImage"></v-img> -->
        </v-list-item-avatar>
      </v-list-item>

      <v-list-item link>
        <v-list-item-content>
          <v-list-item-title class="title">
            {{ user.userNickname }}
          </v-list-item-title>
          <v-list-item-subtitle>{{ user.userEmail }}</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </v-list>

    <v-divider></v-divider>

    <v-list nav dense>
      <v-list-item>
        <v-list-item-icon>
          <v-icon>mdi-account</v-icon>
        </v-list-item-icon>
        <v-list-item-title>마이페이지</v-list-item-title>
      </v-list-item>
      <v-list-item disabled>
        <v-list-item-icon>
          <v-icon>mdi-chart-bar</v-icon>
        </v-list-item-icon>
        <v-list-item-title>나의 전적기록</v-list-item-title>
      </v-list-item>
      <v-list-item disabled>
        <v-list-item-icon>
          <v-icon>mdi-message-text-outline</v-icon>
        </v-list-item-icon>
        <v-list-item-title>쪽지</v-list-item-title>
      </v-list-item>
      <v-list-item link>
        <v-list-item-icon>
          <v-icon>mdi-dots-horizontal</v-icon>
        </v-list-item-icon>
        <v-list-item-title>설정</v-list-item-title>
      </v-list-item>
      <v-list-item link @click="openform">
        <v-list-item-icon>
          <v-icon> mdi-flash</v-icon>
        </v-list-item-icon>
        <v-list-item-title>채팅창</v-list-item-title>
      </v-list-item>
    </v-list>
    <ChatModal :dialog="dialog" @close="close" @send="send" />
  </v-navigation-drawer>
</template>

<script>
import ChatModal from "../chat/ChatModal.vue";

export default {
  name: "SideNavi",
  components: {
    ChatModal,
  },
  data() {
    return {
      dialog: false,
      user: JSON.parse(sessionStorage.getItem("user")),
    };
  },
  methods: {
    goLogin() {
      this.$router.push({ name: "Login" });
    },
    goMessage() {
      this.$router.push({ name: "Message" });
    },
    openform() {
      this.dialog = true;
    },
    close() {
      this.dialog = false;
    },
    send() {
      this.dialog = false;
    },
  },
};
</script>

<style>
</style>