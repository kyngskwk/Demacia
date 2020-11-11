<template>
  <v-row justify="end">
    <v-dialog v-model="dialog" persistent max-width="600px">
      <template v-slot:activator="{ on, attrs }">
        <v-btn small color="secondary" v-bind="attrs" v-on="on">
          비밀번호찾기
        </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="headline">비밀번호 찾기</span>
        </v-card-title>
        <v-window v-model="step">
          <v-window-item :value="1">
            <v-card-text>
              <v-container>
                <small>가입했던 이메일을 입력해 주세요</small>
                <v-row>
                  <v-col cols="12">
                    <v-form @submit.prevent="checkEmail" v-model="valid">
                      <v-text-field
                        label="Email"
                        v-model="email"
                        required
                        :rules="[rules.required, rules.email]"
                      />
                    </v-form>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDialog">
                취소
              </v-btn>
              <v-btn
                color="blue darken-1"
                text
                @click="checkEmail"
                :disabled="!valid"
              >
                확인
              </v-btn>
            </v-card-actions>
          </v-window-item>
          <v-window-item :value="2">
            <v-card-text>
              <v-container>
                <small
                  >작성하신 이메일로 인증코드를 발송했습니다. 인증코드를
                  입력해주세요.</small
                >
                <v-row>
                  <v-col cols="12">
                    <v-form @submit.prevent="checkCode" v-model="valid">
                      <v-text-field
                        label="인증코드"
                        v-model="code"
                        required
                        :rules="[rules.required]"
                      />
                    </v-form>
                  </v-col>
                  <v-col cols="12" class="text-right" style="color: red">
                    {{ time }}
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDialog">
                취소
              </v-btn>
              <v-btn
                color="blue darken-1"
                text
                @click="checkCode"
                :disabled="!valid"
              >
                다음
              </v-btn>
            </v-card-actions>
          </v-window-item>
          <v-window-item :value="3">
            <v-card-text>
              <v-container>
                <small>변경하실 비밀번호를 입력해주세요</small>
                <v-row>
                  <v-col cols="12">
                    <v-form @submit.prevent="updatePassword" v-model="valid">
                      <v-text-field
                        label="비밀번호"
                        v-model="password"
                        required
                        hint="영문+숫자 혼합 8자 이상"
                        :rules="[rules.required, rules.password]"
                        :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                        @click:append="show1 = !show1"
                        :type="show1 ? 'text' : 'password'"
                        counter
                      />
                      <v-text-field
                        label="비밀번호 확인"
                        v-model="passwordConfirm"
                        required
                        hint="비밀번호를 한 번 더 입력하세요"
                        :rules="[
                          rules.required,
                          rules.passwordMatch(passwordConfirm, password),
                        ]"
                        :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
                        @click:append="show2 = !show2"
                        :type="show2 ? 'text' : 'password'"
                        counter
                      />
                    </v-form>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDialog">
                취소
              </v-btn>
              <v-btn
                color="blue darken-1"
                text
                @click="updatePassword"
                :disabled="!valid"
              >
                변경
              </v-btn>
            </v-card-actions>
          </v-window-item>
          <v-window-item :value="4">
            <v-card-text>
              <v-container>
                비밀번호가 변경되었습니다. 변경된 비밀번호로 로그인하세요!
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDialog">
                확인
              </v-btn>
            </v-card-actions>
          </v-window-item>
        </v-window>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import * as EmailValidator from "email-validator";
import PV from "password-validator";
import axios from "axios";
let sc = "";
let passwordSchema = new PV()
  .is()
  .min(8)
  .is()
  .max(100)
  .has()
  .digits()
  .has()
  .letters();
export default {
  data: () => ({
    userNo: 0,
    email: "",
    code: "",
    password: "",
    passwordConfirm: "",
    dialog: false,
    valid: true,
    step: 1,
    time: "",
    timerID: "",
    show1: false,
    show2: false,
    rules: {
      required: (value) => !!value || "내용을 입력해주세요",
      email: (value) =>
        EmailValidator.validate(value) || "이메일 형식을 지켜주세요",
      password: (value) =>
        passwordSchema.validate(value) ||
        "영문+숫자 혼합 8자 이상으로 작성해주세요",
      passwordMatch: (value, pwd) => value === pwd || "일치하지 않습니다.",
    },
  }),
  methods: {
    closeDialog() {
      this.valid = !(this.dialog = false);
      this.step = 1;
      this.email = this.code = this.password = this.passwordConfirm = "";
    },
    checkEmail() {
      axios
        .get(process.env.VUE_APP_API_URL + "/account/checkEmail", {
          params: {
            userEmail: this.email,
          },
        })
        .then((res) => {
          if (res.data.status) {
            // 존재하지 않음
            this.$root.$children[0].snackbar = true;
            this.$root.$children[0].errMsg =
              "이 주소로 가입한 회원이 없습니다.";
          } else {
            // 아이디가 있음
            let provider;
            [this.userNo, provider] = res.data.object.split(" ");
            if (provider === "KAKAO" || provider === "GOOGLE") {
              this.$root.$children[0].snackbar = true;
              this.$root.$children[0].errMsg =
                "소셜 회원입니다. 카카오 또는 구글 계정으로 로그인 하세요.";
            } else {
              sc = Math.random().toString(36).substr(2, 11);
              axios
                .post(process.env.VUE_APP_API_URL + "/email", {
                  email: this.email,
                  code: sc,
                })
                .then(() => {});
              this.step++;
              this.setTimer();
            }
          }
        });
    },
    setTimer() {
      this.time = "남은시간 03:00";
      let t = 180;
      this.timerID = setInterval(() => {
        t--;
        this.time =
          "남은시간 " +
          (parseInt(t / 60) < 10 ? "0" : "") +
          parseInt(t / 60) +
          ":" +
          (t % 60 < 10 ? "0" : "") +
          (t % 60);
        if (t == 0) {
          clearInterval(this.timerID);
          this.time = "시간 만료";
        }
      }, 1000);
    },
    checkCode() {
      if (sc === this.code) {
        if (this.time != "시간 만료") {
          clearInterval(this.timerID);
          this.step++;
        } else {
          this.$root.$children[0].snackbar = true;
          this.$root.$children[0].errMsg =
            "인증코드가 만료되었습니다. 인증번호를 다시 발급받으세요";
        }
      } else {
        this.$root.$children[0].snackbar = true;
        this.$root.$children[0].errMsg = "인증번호가 일치하지 않습니다";
      }
    },
    updatePassword() {
      if (!this.valid) {
        this.$root.$children[0].snackbar = true;
        this.$root.$children[0].errMsg = "비밀번호를 다시 확인해 주세요";
      } else {
        axios
          .get(process.env.VUE_APP_API_URL + "/account/user", {
            params: {
              userNo: this.userNo,
            },
          })
          .then((res) => {
            res.data.object.userPw = this.password;
            axios
              .put(process.env.VUE_APP_API_URL + "/account/", res.data.object)
              .then(() => {
                this.step++;
              });
          })
          .catch(() => {
            this.$root.$children[0].snackbar = true;
            this.$root.$children[0].errMsg =
              "비밀번호 변경 중 서버에서 문제가 발생했습니다. 다시 시도해주세요";
          });
      }
    },
  },
};
</script>

<style>
</style>