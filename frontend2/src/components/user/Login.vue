<template>
  <v-row align="center" class="ma-3">
    <v-col cols="12" md="6">
      <v-card-title class="my-3"
        ><v-img src="../../assets/img/damacia.png"
      /></v-card-title>
      <v-card-text>
        <v-text-field
          v-model="email"
          label="E-mail"
          :rules="[rules.required, rules.email]"
          outlined
        />
        <v-text-field
          label="Password"
          v-model="password"
          :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
          :rules="[rules.required]"
          :type="show1 ? 'text' : 'password'"
          hint="영문+숫자 혼합 8자 이상"
          counter
          @click:append="show1 = !show1"
          outlined
          @keydown.enter="loginCheck"
        />
        <v-row class="text-right my-n7" align="center">
          <v-col>
            <v-checkbox v-model="saveEmail" label="이메일 저장" />
          </v-col>
          <v-col>
            <v-btn small color="secondary"> 비밀번호찾기</v-btn>
          </v-col>
        </v-row>
      </v-card-text>
    </v-col>
    <v-col cols="12" md="6" class="text-center">
      <v-btn width="300" height="45" @click="loginCheck">로그인 </v-btn>
      <v-divider class="my-7" />
      <v-btn height="45" width="300" @click="kakao">
        <v-img src="../../assets/img/kakao2.png" draggable="false" />
      </v-btn>
      <v-btn height="45" width="300" class="my-3" @click="google">
        <v-img src="../../assets/img/google2.png" draggable="false" />
      </v-btn>
    </v-col>
    <v-snackbar v-model="snackbar">{{ errMsg }}</v-snackbar>
  </v-row>
</template>

<script>
import axios from "axios";
import * as EmailValidator from "email-validator";

export default {
  name: "Login",
  components: {},
  data() {
    return {
      show1: false,
      baseURL: window.location.hostname,
      email: "",
      password: "",
      rules: {
        required: (value) => !!value || "내용을 입력해주세요",
        email: (value) =>
          EmailValidator.validate(value) || "이메일 형식을 지켜주세요",
        emailMatch: () => "아이디 또는 비밀번호를 확인해주세요",
      },
      saveEmail: false,
      snackbar: false,
      errMsg: "",
    };
  },
  created() {
    window.scrollTo(0, 0);
    if (this.$route.query.scope) {
      console.log("goolelogin:" + this.$route.query.code);
      axios
        .get(process.env.VUE_APP_API_URL + "/login/google", {
          params: {
            code: this.$route.query.code,
            redirectUrl: process.env.VUE_APP_BASE_URL + "/login",
          },
        })
        .then((res) => {
          if (res.data.status) {
            res.data.object.userPw = "";
            // 세션에 로그인 정보 추가
            sessionStorage.setItem("user", JSON.stringify(res.data.object));
            this.$router.push({ path: "/" });
          } else {
            this.snackbar = true;
            this.errMsg = "구글 아이디 또는 비밀번호를 확인해주세요";
          }
        })
        .catch((err) => {
          this.snackbar = true;
          this.errMsg =
            "로그인 중 서버 오류가 발생했습니다. " +
            err +
            ": 다시 시도해 주세요";
        });
    } else if (this.$route.query.code) {
      console.log(this.$route.query.code);
      axios
        .get(process.env.VUE_APP_API_URL + "/login/oauth", {
          params: {
            code: this.$route.query.code,
            redirectUrl: process.env.VUE_APP_BASE_URL,
          },
        })
        .then((res) => {
          if (res.data.status) {
            res.data.object.userPw = "";
            sessionStorage.setItem("user", JSON.stringify(res.data.object));
            this.$router.push({ path: "/" });
          } else {
            this.snackbar = true;
            this.errMsg = "아이디 또는 비밀번호를 확인해주세요";
          }
        })
        .catch((err) => {
          this.snackbar = true;
          this.errMsg =
            "로그인 중 서버 오류가 발생했습니다. " +
            err +
            ": 다시 시도해 주세요";
        });
    }
  },
  methods: {
    kakao() {
      location.href =
        "https://kauth.kakao.com/oauth/authorize?client_id=" +
        "121c6ba38cce9dba0c6843a59450b6fd" +
        "&redirect_uri=" +
        process.env.VUE_APP_BASE_URL +
        "/login&response_type=code";
    },

    google() {
      location.href =
        "https://accounts.google.com/o/oauth2/v2/auth?" +
        "scope=https://www.googleapis.com/auth/userinfo.email&https://www.googleapis.com/auth/userinfo.profile&openid" +
        "include_granted_scopes=true&" +
        "response_type=code&" +
        "state=state_parameter_passthrough_value&" +
        "redirect_uri=" +
        process.env.VUE_APP_BASE_URL +
        "/login&" +
        "client_id=1023963510057-bijvog3gfp162178b7iqu978ruruqkq2.apps.googleusercontent.com";
    },

    loginCheck() {
      let err = false;
      this.emailValid = !(
        (!this.email &&
          ((this.snackbar = true),
          (this.errMsg = "이메일을 입력해주세요"),
          (err = true))) ||
        (this.email &&
          !EmailValidator.validate(this.email) &&
          ((this.snackbar = true),
          (this.errMsg = "메일 형식을 맞춰주세요"),
          (err = true)))
      );
      this.pwValid = !(
        !this.password &&
        ((this.snackbar = true),
        (this.errMsg = "비밀번호를 입력해주세요"),
        (err = true))
      );
      if (!err) this.dataSend();
    },
    dataSend() {
      axios
        .get(process.env.VUE_APP_API_URL + "/account/login", {
          params: {
            userEmail: this.email,
            userPw: this.password,
          },
        })
        .then((res) => {
          if (res.data.status) {
            res.data.object.userPw = "";
            // 세션에 로그인 정보 추가
            sessionStorage.setItem("user", JSON.stringify(res.data.object));
            console.log(res.data.object);
            this.$router.push({ path: "/" });
          } else {
            this.snackbar = true;
            this.errMsg = "아이디 또는 비밀번호를 확인해주세요";
          }
        })
        .catch((err) => {
          this.snackbar = true;
          this.errMsg =
            "로그인 중 서버 오류가 발생했습니다. " +
            err +
            ": 다시 시도해 주세요";
        });
    },
  },
};
</script>

<style>
</style>