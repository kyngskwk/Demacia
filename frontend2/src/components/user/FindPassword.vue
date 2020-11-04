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
                    <v-form v-model="valid">
                      <v-text-field
                        label="Email"
                        v-model="email"
                        required
                        :rules="[rules.required, rules.email]"
                      ></v-text-field>
                    </v-form>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>
          </v-window-item>
          <v-window-item :value="2"> , </v-window-item>
        </v-window>
        <v-card-actions v-show="step == 1">
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialog = false">
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
        <v-card-actions v-show="step == 2">
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="step--"> 이전 </v-btn>
          <v-btn color="blue darken-1" text @click="checkCode"> 다음 </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
//import axios from "axios";
import * as EmailValidator from "email-validator";
import axios from "axios";

export default {
  data: () => ({
    email: "",
    dialog: false,
    valid: true,
    step: 1,
    rules: {
      required: (value) => !!value || "내용을 입력해주세요",
      email: (value) =>
        EmailValidator.validate(value) || "이메일 형식을 지켜주세요",
    },
  }),
  methods: {
    checkEmail() {
      axios
        .get(process.env.VUE_APP_API_URL + "/account/checkEmail", {
          params: {
            email: this.email,
          },
        })
        .then((res) => {
          console.log(res);
          //            if(res.status){}
        });
      this.step++;
      //var code = Math.random().toString(36).substr(2, 11);
    },
    checkCode() {},
  },
};
</script>

<style>
</style>