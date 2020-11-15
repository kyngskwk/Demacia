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
      <v-list-item link>
        <v-list-item-avatar>
          <v-img :src="userImg"></v-img>
        </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title class="title">
            {{ user.userNickname }}
          </v-list-item-title>
          <v-list-item-subtitle>{{ user.userEmail }}</v-list-item-subtitle>
        </v-list-item-content>
        <v-chip @click="logout">로그아웃</v-chip>
      </v-list-item>
    </v-list>

    <v-divider></v-divider>

    <v-list nav dense>
      <v-list-item link :disabled="!user">
        <v-list-item-icon>
          <v-icon>mdi-account</v-icon>
        </v-list-item-icon>
        <v-list-item-title>마이페이지</v-list-item-title>
      </v-list-item>
      <v-list-item link :disabled="!user">
        <v-list-item-icon>
          <v-icon>mdi-chart-bar</v-icon>
        </v-list-item-icon>
        <v-list-item-title>나의 전적기록</v-list-item-title>
      </v-list-item>
      <v-list-item link disabled @click="goMessage">
        <v-list-item-icon>
          <v-icon>mdi-message-text-outline</v-icon>
        </v-list-item-icon>
        <v-list-item-title>쪽지</v-list-item-title>
      </v-list-item>
      <v-list-item link :disabled="!user">
        <v-list-item-icon>
          <v-icon>mdi-dots-horizontal</v-icon>
        </v-list-item-icon>
        <v-list-item-title>설정</v-list-item-title>
      </v-list-item>
      <v-list-item link @click="openform" :disabled="!user">
        <v-list-item-icon>
          <v-icon> mdi-flash</v-icon>
        </v-list-item-icon>
        <v-list-item-title>채팅창</v-list-item-title>
      </v-list-item>
      <v-list-item link @click="goBoard">
        <v-list-item-icon>
          <v-icon> mdi-account-group</v-icon>
        </v-list-item-icon>
        <v-list-item-title>커뮤니티</v-list-item-title>
      </v-list-item>
    </v-list>
    <ChatModal :dialog="dialog" @close="close" @send="send" />
  </v-navigation-drawer>
</template>

<script>
import axios from "axios";
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
      userImg:
        process.env.VUE_APP_IMGUP_URL +
        (this.user
          ? JSON.parse(sessionStorage.getItem("user")).userImage
          : "noimage.png"),
      snackbar: false,
      errMsg: "",
    };
  },
  methods: {
    goBoard() {
      this.$router.push({ name: "board" });
    },
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
    logout() {
      if (!this.user.accessToken) {
        console.log("not accesstoken");
        sessionStorage.removeItem("user");
        this.$router.push({ path: "/" });
        window.location.reload();
      } else if (this.user.providerName == "GOOGLE") {
        axios
          .get(process.env.VUE_APP_API_URL + "/logout/google", {
            params: {
              token: this.user.accessToken,
            },
          })
          .then(() => {
            sessionStorage.removeItem("user");
            this.$router.push({ path: "/" });
            window.location.reload();
          })
          .catch((err) => {
            this.$root.$children[0].snackbar = true;
            this.$root.$children[0].errMsg =
              "로그아웃 중 서버 오류가 발생했습니다. " + err;
          });
      } else {
        axios
          .get(process.env.VUE_APP_API_URL + "/logout/oauth", {
            params: {
              accesstoken: this.user.accessToken,
            },
          })
          .then(() => {
            sessionStorage.removeItem("user");
            this.$router.push({ path: "/" });
            window.location.reload();
          })
          .catch((err) => {
            this.$root.$children[0].snackbar = true;
            this.$root.$children[0].errMsg =
              "로그아웃 중 서버 오류가 발생했습니다. " + err;
          });
      }
    },
  },
};
</script>

<style>
</style>