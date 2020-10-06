<template>
  <div
    class="pb-2"
    style="
      background: rgba(0, 0, 0, 0.5);
      width: 96%;
      margin-left: auto;
      margin-right: auto;
      font-family: Tmon;
      color: white;
    "
  >
    <div
      class="d-flex justify-content-between"
      style="margin-right: 1%; margin-left: 1%; margin-top: 1%"
    >
      <b-container class="bv-example-row" style="padding: 0; margin-top: 3%">
        <b-row
          style="
            max-height: 475px;
            width: 100%;
            border-top: solid;
            border-bottom: solid;
            margin: 0;
          "
        >
          <b-col
            cols="3"
            lg="3"
            xl="3"
            style="text-align: left; padding-top: 2%; padding-left: 1%"
            class="d-flex"
          >
            <p id="hide3" style="font-size: 3vh; padding-left: 7%">의뢰번호</p>
            <p style="font-weight: bold; font-size: 3.5vh; padding-left: 5px">
              NO.{{ videoPostNo }}
            </p>
          </b-col>
          <b-col
            cols="9"
            lg="5"
            xl="6"
            class="d-flex justify-content-center"
            style="padding-top: 3%"
          >
            <p
              style="
                font-weight: bold;
                font-size: 3.5vh;
                max-width: 100%;
                display: -webkit-box;
                overflow: hidden;
                width: 100%;
                text-overflow: ellipsis;
                -webkit-line-clamp: 1;
                -webkit-box-orient: vertical;
                word-wrap: break-word;
                line-height: 4vh;
                height: 4vh;
              "
            >
              {{ writePost.title }}
            </p>
          </b-col>
          <b-col id="hide2" cols="4" lg="3" xl="3" style="">
            <h4
              style="
                font-size: 5vh;
                font-weight: bold;
                color: red;
                margin-top: 10%;
              "
            >
              분석 완료
            </h4>
          </b-col>
        </b-row>
      </b-container>
    </div>
    <div class="container" style="width: 100%; padding: 0; margin-top: 2%">
      <video
        style="width: 100%; padding: 0; max-width: 900px"
        controls
        autoplay="true"
        name="media"
        id="vid"
      >
        <source :src="videolink" type="video/mp4" />
      </video>
    </div>

    <div
      id="mainBody"
      class="container"
      style="
        padding-left: 5px;
        padding-right: 5px;
        padding-bottom: 5px;
        margin-top: -7%;
        padding-top: 6%;
        margin-bottom: 5%;
      "
    >
      <hr style="margin-left: 2%; margin-right: 2%" />
      <div class="row">
        <div class="col-7 col-xl-8" style="padding: 0">
          <!-- 글쓴이 -->
          <div class="d-flex justify-content-between">
            <div class="d-flex" style="margin-left: 2%">
              <b-avatar
                variant="secondary"
                :src="writePost.userImage"
                class="ml-3 mr-3"
              ></b-avatar>
              <div>
                <h4
                  style="
                    margin-bottom: 0;
                    text-align: center;
                    font-size: 2.5vh;
                    margin-top: 12%;
                  "
                >
                  {{ writePost.userNickname }}
                </h4>
                <h4
                  style="margin-bottom: 0; text-align: center; font-size: 1.2vh"
                >
                  <p>{{ writePost.userRank }}</p>
                  <p>{{ writePost.gameRank }}</p>
                </h4>
              </div>
            </div>
          </div>
        </div>
        <div class="col-5 col-xl-4">
          <!-- 조회수 -->
          <div class="d-flex justify-content-end" style="margin-right: 5%">
            <div class="d-flex">
              <p style="font-size: 2.5vh">좋아요: {{ writePost.totalLike }}</p>
              <b-icon-caret-right-square-fill
                class="h4"
                style="margin-right: 10px; padding-top: 3%"
              />
              <p style="font-size: 2.5vh">{{ writePost.view }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <hr style="margin: 2%" />
    <div
      class="container"
      style="
        margin-top: 2%;
        margin-left: 2%;
        margin-right: 2%;
        text-align: center;
        border: solid 5px gray;
        border-radius: 10px;
      "
    >
      <div class="row row-cols-12">
        <div class="col">
          <h3>영상이전 승률</h3>
          <pie-chart
            :data="[
              ['BLUETEAM', before_bluescore],
              ['REDTEAM', before_redscore],
            ]"
            :colors="['#23285c', '#d71616']"
            suffix="%"
          ></pie-chart>
        </div>
        <div class="col">
          <h3>영상이후 승률</h3>
          <pie-chart
            :data="[
              ['BLUETEAM', after_bluescore],
              ['REDTEAM', after_redscore],
            ]"
          ></pie-chart>
        </div>
      </div>

      <div class="container">
        <div class="row justify-content-around listbox mt-3">
          <div class="col-5 chambox1">
            <div class="d-flex ">
              <img class="imgrelative" src="../../assets/img/3badge.png" />
              <div class="mt-3 ml-3">
                <h2>챔피언 킬 +1</h2>
                <h2>와드 파괴 +2</h2>
              </div>
            </div>
          </div>
          <div class="col-5 chambox1">
            <div class="d-flex ">
              <img class="imgrelative" src="../../assets/img/3badge.png" />
              <div class="mt-3 ml-3">
                <h2>챔피언 킬 +1</h2>
                <h2>와드 파괴 +2</h2>
              </div>
            </div>
          </div>
        </div>
        <div class="row justify-content-around listbox mt-3">
          <div class="col-5 chambox1">
            <div class="d-flex ">
              <img class="imgrelative" src="../../assets/img/3badge.png" />
              <div class="mt-3 ml-3">
                <h2>챔피언 킬 +1</h2>
                <h2>와드 파괴 +2</h2>
              </div>
            </div>
          </div>
          <div class="col-5 chambox1">
            <div class="d-flex ">
              <img class="imgrelative" src="../../assets/img/3badge.png" />
              <div class="mt-3 ml-3">
                <h2>챔피언 킬 +1</h2>
                <h2>와드 파괴 +2</h2>
              </div>
            </div>
          </div>
        </div>

        <div class="row justify-content-around listbox mt-3">
          <div class="col-5 chambox1">
            <div class="d-flex ">
              <img class="imgrelative" src="../../assets/img/3badge.png" />
              <div class="mt-3 ml-3">
                <h2>챔피언 킬 +1</h2>
                <h2>와드 파괴 +2</h2>
              </div>
            </div>
          </div>
          <div class="col-5 chambox1">
            <div class="d-flex ">
              <img class="imgrelative" src="../../assets/img/3badge.png" />
              <div class="mt-3 ml-3">
                <h2>챔피언 킬 +1</h2>
                <h2>와드 파괴 +2</h2>
              </div>
            </div>
          </div>
        </div>
        <div class="row justify-content-around listbox mt-3">
          <div class="col-5 chambox1">
            <div class="d-flex ">
              <img class="imgrelative" src="../../assets/img/3badge.png" />
              <div class="mt-3 ml-3">
                <h2>챔피언 킬 +1</h2>
                <h2>와드 파괴 +2</h2>
              </div>
            </div>
          </div>
          <div class="col-5 chambox1">
            <div class="d-flex ">
              <img class="imgrelative" src="../../assets/img/3badge.png" />
              <div class="mt-3 ml-3">
                <h2>챔피언 킬 +1</h2>
                <h2>와드 파괴 +2</h2>
              </div>
            </div>
          </div>
        </div>
        <div class="row justify-content-around listbox mt-3">
          <div class="col-5 chambox1">
            <div class="d-flex ">
              <img class="imgrelative" src="../../assets/img/3badge.png" />
              <div class="mt-3 ml-3">
                <h2>챔피언 킬 +1</h2>
                <h2>와드 파괴 +2</h2>
              </div>
            </div>
          </div>
          <div class="col-5 chambox1">
            <div class="d-flex ">
              <img class="imgrelative" src="../../assets/img/3badge.png" />
              <div class="mt-3 ml-3">
                <h2>챔피언 킬 +1</h2>
                <h2>와드 파괴 +2</h2>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <br />

    <!-- 로그인 확인하는 모달 -->
    <b-modal ref="loginChkModal" centered title="로그인 필요">
      로그인이 필요한 서비스입니다.
      <br />로그인 하시겠습니까?
      <template v-slot:modal-footer="{ cancel }">
        <b-button size="sm" variant="primary" @click="toLogin">확인</b-button>
        <b-button size="sm" variant="danger" @click="cancel()">취소</b-button>
      </template>
    </b-modal>
    <!-- 빙글빙글 모달 -->
    <b-modal ref="binggleModal" centered title="분석중..">
      <b-icon icon="arrow-clockwise" animation="spin" font-scale="4"></b-icon>
    </b-modal>
    <!-- 수정 삭제 -->
    <div style="margin-top: 5%">
      <div
        @click="edit"
        class="btn btn-primary"
        style="width: 15%; margin-right: 5%; position: relative; bottom: 5%"
        v-if="checkaccess"
      >
        수정
      </div>

      <div
        @click="delt"
        class="btn btn-secondary"
        style="width: 15%; margin-left: 5%"
        v-if="checkaccess"
      >
        삭제
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import "../../assets/css/comment.css";
import Vue from "vue";
import Chartkick from "vue-chartkick";
import Chart from "chart.js";

Vue.use(Chartkick.use(Chart));
export default {
  data() {
    return {
      sessionUserNo: "",
      sessionUser: {},
      videoPostNo: this.$route.params.videoNo,
      writePost: {},
      videolink: "",
      state: "",
      videoData: "",
      before_bluescore: "",
      before_redscore: "",
      after_bluescore: "",
      after_redscore: "",
      champ1: "",
      champ2: "",
      champ3: "",
      champ4: "",
      champ5: "",
      champ6: "",
      champ7: "",
      champ8: "",
      champ9: "",
      champ10: "",
      champion: "",
    };
  },

  created() {
    window.scrollTo(0, 0);
    // 세션 유저정보 저장. 없으면 ""
    this.sessionUserNo = JSON.parse(sessionStorage.getItem("user"))
      ? JSON.parse(sessionStorage.getItem("user")).userNo
      : "";
    //처음 데이터 불러오기
    console.log(this.$route.params);
    console.log(this.videoPostNo);
    axios.get(process.env.VUE_APP_DAPI_URL + "/champions/").then((res) => {
      this.champion = res.data;
      axios
        .get(process.env.VUE_APP_API_URL + "/video/detail", {
          params: {
            videoPostNo: this.videoPostNo,
          },
        })
        .then(({ data }) => {
          console.log(data.object);
          this.writePost = data.object;
          this.data = JSON.parse(data.object.data.replaceAll("'", '"'));
          this.before_bluescore = this.data.before_bluescore;
          this.before_redscore = this.data.before_redscore;
          this.after_bluescore = this.data.after_bluescore;
          this.after_redscore = this.data.after_redscore;
          this.champ1 = this.data["1"];
          this.champ2 = this.data["2"];
          this.champ3 = this.data["3"];
          this.champ4 = this.data["4"];
          this.champ5 = this.data["5"];
          this.champ6 = this.data["6"];
          this.champ7 = this.data["7"];
          this.champ8 = this.data["8"];
          this.champ9 = this.data["9"];
          this.champ10 = this.data["10"];
          this.champ1 = this.add(this.champ1);
          this.champ2 = this.add(this.champ2);
          this.champ3 = this.add(this.champ3);
          this.champ4 = this.add(this.champ4);
          this.champ5 = this.add(this.champ5);
          this.champ6 = this.add(this.champ6);
          this.champ7 = this.add(this.champ7);
          this.champ8 = this.add(this.champ8);
          this.champ9 = this.add(this.champ9);
          this.champ10 = this.add(this.champ10);
          console.log(this.champ5);
          this.videolink =
            process.env.VUE_APP_IMGUP_URL + "/videos/" + this.writePost.video;
          let vd = document.querySelector("#vid");
          vd.load();
        });
    });
  },

  computed: {
    checkadmin() {
      return this.sessionUserNo == 3;
    },

    checkaccess() {
      return (
        this.sessionUserNo == this.writePost.userNo || this.sessionUserNo == 3
      );
    },
  },

  methods: {
    add(champ) {
      champ = Object.assign(
        champ,
        this.champion.find((o) => o.chamname == champ.name)
      );
      champ.imgsrc = champ.imgsrc
        .replace("@/assets/img", "")
        .replace("_1.", "_0.");
      return champ;
    },
    toLogin() {
      this.$router.push("/login/");
    },
    edit() {
      this.$router.push("/vedit/" + this.videoNo);
    },
    delt() {
      if (confirm("글을 삭제하시겠습니까?")) {
        axios
          .delete(process.env.VUE_APP_API_URL + "/video/", {
            params: {
              videoNo: this.videoNo,
            },
          })
          .then(() => {
            alert("삭제 완료");
            location.href = "/";
          })
          .catch(() => {
            location.href = "/error/글 삭제 중 서버에서 문제가 발생했습니다.";
          });
      }
    },

    analize() {
      this.$refs["binggleModal"].show();
    },

    loginCheck() {
      return this.sessionUserNo
        ? true
        : this.$refs["loginChkModal"].show() && false;
    },
  },
};
</script>

<style>
.border1 {
  border-left-width: 50px !important;
}
@media screen and (max-width: 580px) {
  #hide1 {
    display: none;
  }
}
@media screen and (max-width: 990px) {
  #hide2 {
    display: none;
  }
}
@media screen and (max-width: 760px) {
  #hide3 {
    display: none;
  }
}
.s {
  background-color: rgb(76, 202, 240);
}
.text_comment {
  font-size: 2vh;
}
.popover {
  position: relative !important;
  max-width: 90% !important;
  width: 90% !important;
}
.listbox {
  height: 130px;
}
.imgrelative {
  position: relative;
  top: 10px;
  border-style: ridge;
  border: #fcd000 3px ridge;
  height: 100px;
}
.chambox1 {
  padding-left: 10px;
  background: linear-gradient(
    180deg,
    rgba(14, 36, 56, 1) 0%,
    rgba(32, 17, 95, 1) 100%
  );
  border-style: ridge;
  border: #fcd000 3px ridge;
}
</style>
