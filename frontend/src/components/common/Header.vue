<template>
  <div id="a" style="font-family:Tmon">
    <nav
      class="navbar navbar-expand-lg navbar-dark fixed-top"
      id="mainNav"
      style="background-color: black;"
    >
      <div class="container">
        <a class="navbar-brand mx-auto" href="/list" style="padding-top:5px; font-size:2em">DEMACIA</a>
        <button
          class="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target=".dual-collapse2"
          style="margin-left:50px; border:none;"
        >
          <b-icon icon="three-dots" animation="cylon" font-scale="2.5"></b-icon>
        </button>
        <div class="navbar-collapse collapse w-100 order-3 dual-collapse2">
          <ul class="navbar-nav ml-auto" style="font-size:2.5hv" v-if="isLogin">
            <li class="nav-item">
              <a @click="logout" class="nav-link">로그아웃</a>
            </li>
            <li class="nav-item">
              <router-link v-bind:to="{name:constants.URL_TYPE.POST.WRITE}" class="nav-link">글쓰기</router-link>
            </li>
            <li class="nav-item">
              <router-link v-bind:to="{name:constants.URL_TYPE.USER.MYPROFILE}" class="nav-link">프로필</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/" class="nav-link">소개</router-link>
            </li>
          </ul>
          <ul class="navbar-nav ml-auto" style="font-size:2.5hv" v-else>
            <li class="nav-item">
              <router-link v-bind:to="{name:constants.URL_TYPE.USER.LOGIN}" class="nav-link">로그인</router-link>
            </li>
            <li class="nav-item">
              <router-link v-bind:to="{name:constants.URL_TYPE.USER.JOIN}" class="nav-link">회원가입</router-link>
            </li>
            <li class="nav-item">
              <router-link to="/" class="nav-link">소개</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <div style="height:74px">.</div>
  </div>
</template>

<script>
import constants from "../../lib/constants";
import axios from "axios";

export default {
  name: "Header",
  data() {
    return {
      constants,
      keyword: "",
    };
  },
  computed: {
    isLogin() {
      return sessionStorage.getItem("user");
    },
  },
  created() {},
  methods: {
    logout() {
      if (JSON.parse(sessionStorage.getItem("user")).accesstoken == null) {
        sessionStorage.removeItem("user");
        location.href = "/";
      } else {
        axios
          .get(process.env.VUE_APP_API_URL + "/logout/oauth", {
            params: {
              accesstoken: JSON.parse(sessionStorage.getItem("user"))
                .accesstoken,
            },
          })
          .then(() => {
            sessionStorage.removeItem("user");
            location.href = "/";
          })
          .catch((err) => {
            location.href =
              "/error/로그아웃 중 서버 오류가 발생했습니다. " + err;
            window.location.reload();
          });
      }
    },
  },
};
</script>
<style >
@font-face {
  font-family: "Tmon";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-07@1.0/TmoneyRoundWindExtraBold.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: "digital";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-07@1.0/LAB디지털.woff")
    format("woff");
  font-weight: normal;
  font-style: normal;
}
</style>