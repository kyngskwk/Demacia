<template>
  <div class="block1 d-flex">
    <div class="main" style="width:100%;">
      <div class="col-xl-4 col-lg-4 col-md-8 col-sm-12 m-auto">
        <div class="login-form border rounded" style="padding:50px;background-color: white;">
          <img
            :src="logologin"
            alt="logo2"
            style="width:90%; margin-bottom:3em; margin-left:15px"
            draggable="false"
          />
          <div class="form-group">
            <b-form-input
              type="text"
              placeholder="이메일"
              id="email"
              size="lg"
              style="width:80%;margin-right:auto; margin-left:auto; margin-bottom:5%;"
              v-model="email"
              :state="emailValid"
            />
          </div>
          <div class="form-group">
            <b-form-input
              type="password"
              placeholder="비밀번호"
              id="password"
              v-model="password"
              size="lg"
              style="width:80%;margin-right:auto; margin-left:auto;margin-bottom:5%;"
              :state="pwValid"
              @keydown.enter="loginCheck"
            />
          </div>
          <div
            @click="loginCheck"
            class="btn btn-primary btn-lg"
            style="width:80%; margin-bottom:5%"
          >로그인</div>
          <div
            @click="signuppage"
            class="btn btn-secondary btn-lg"
            style="width:80%;margin-bottom:2%;"
          >회원가입</div>
          <a
            href="https://kauth.kakao.com/oauth/authorize?client_id=b38bb5991f9f2b1b516e239a8791f302&redirect_uri=http://i3a602.p.ssafy.io/login&response_type=code"
          >
            <img :src="kakaologo" class="btn" style="width:87%;" alt="kakaologo" draggable="false" />
          </a>
          <img
            :src="naverlogo"
            class="btn"
            style="width:86%;"
            alt="naverlogo"
            @click="naver"
            draggable="false"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import "../../assets/css/user.css";
import axios from "axios";
import * as EmailValidator from "email-validator";

export default {
  name: "LoginView",

  data() {
    return {
      email: "",
      password: "",
      emailValid: null,
      pwValid: null,
      kakaologo: process.env.VUE_APP_IMGUP_URL + "/images/login/kakaologo.PNG",
      naverlogo: process.env.VUE_APP_IMGUP_URL + "/images/login/naverlogo.png",
      logologin: process.env.VUE_APP_IMGUP_URL + "/images/login/loginlogo.PNG",
    };
  },

  created() {
    window.scrollTo(0, 0);
    if (this.$route.query.code) {
      console.log(this.$route.query.code);
      axios
        .get(process.env.VUE_APP_API_URL + "/login/oauth", {
          params: {
            code: this.$route.query.code,
          },
        })
        .then((res) => {
          if (res.data.status) {
            res.data.object.userPw = "";
            this.$store.commit("addUserInfo", res.data.object);
            console.log(this.$store.state.userInfo);
            // 세션에 로그인 정보 추가
            sessionStorage.setItem("user", JSON.stringify(res.data.object));
            location.href = "/list";
          } else {
            this.emailValid = this.pwValid = false;
            this.errToast("아이디 또는 비밀번호를 확인해주세요");
          }
        })
        .catch((err) => {
          location.href = "/error/로그인 중 서버 오류가 발생했습니다. " + err;
        });
    }
  },

  methods: {
    naver() {
      this.errToast("네이버와 계약에 실패해서 서비스를 제공할 수 없었습니다..");
    },
    loginCheck() {
      let err = false;
      this.emailValid = !(
        (!this.email &&
          (this.errToast("이메일을 입력해주세요"), (err = true))) ||
        (this.email &&
          !EmailValidator.validate(this.email) &&
          (this.errToast("메일 형식을 맞춰주세요"), (err = true)))
      );
      this.pwValid = !(
        !this.password &&
        (this.errToast("비밀번호를 입력해주세요"), (err = true))
      );
      if (!err) this.dataSend();
    },

    signuppage() {
      location.href = "/join";
    },
    errToast(msg) {
      this.$bvToast.toast(msg, {
        title: "로그인 오류",
        toaster: "b-toaster-top-center",
        solid: true,
        appendToast: false,
        variant: "primary",
      });
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
            this.$store.commit("addUserInfo", res.data.object);
            console.log(this.$store.state.userInfo);
            // 세션에 로그인 정보 추가
            sessionStorage.setItem("user", JSON.stringify(res.data.object));
            location.href = "/list";
          } else {
            this.emailValid = this.pwValid = false;
            this.errToast("아이디 또는 비밀번호를 확인해주세요");
          }
        })
        .catch((err) => {
          location.href = "/error/로그인 중 서버 오류가 발생했습니다. " + err;
          window.location.reload();
        });
    },
  },
};
</script>