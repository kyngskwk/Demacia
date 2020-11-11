<template>
  <div>
    <v-container>
      <v-row justify="space-around">
        <v-card width="1000">
          <v-card-title class="black--text mt-2">
            <v-avatar size="56">
              <img
                alt="user"
                src="https://cdn.pixabay.com/photo/2020/06/24/19/12/cabbage-5337431_1280.jpg"
              />
            </v-avatar>
            <v-row justify="space-between">
              <div>
                <p class="ml-7 mt-2">John Doe</p>
              </div>
              <div>
                <p class="mr-5 mt-2">영상분석 No.1</p>
              </div>
            </v-row>
          </v-card-title>
          <video
            style="width: 100%; padding: 0; max-width: 1000px"
            controls
            autoplay="true"
            name="media"
            id="vid"
          >
            <v-app-bar flat color="rgba(0, 0, 0, 0)">
              <v-app-bar-nav-icon color="white"></v-app-bar-nav-icon>

              <v-toolbar-title class="title white--text pl-0">
                Messages
              </v-toolbar-title>

              <v-spacer></v-spacer>

              <v-btn color="white" icon>
                <v-icon>mdi-dots-vertical</v-icon>
              </v-btn>
            </v-app-bar>

            <source src="./4659518008_01.mp4" type="video/mp4" />
          </video>
          <v-tabs vertical>
            <v-tab class="pl-0">
              <v-icon left> mdi-clock-time-four-outline </v-icon>
              TIME LINE
            </v-tab>
            <v-tab>
              <v-icon left> mdi-account-group </v-icon>
              Champions
            </v-tab>
            <v-tab class="pl-2">
              <v-icon left> mdi-camera </v-icon>
              Snapshot
            </v-tab>
            <v-tab class="pl-0 pr-5">
              <v-icon left> mdi-chart-areaspline </v-icon>
              Chart
            </v-tab>

            <v-tab-item>
              <v-card flat>
                <v-card-text>
                  <div class="font-weight-bold ml-8 mb-2">TIME LINE</div>

                  <v-timeline align-top dense>
                    <v-timeline-item
                      v-for="message in messages"
                      :key="message.time"
                      :color="message.color"
                      small
                    >
                      <div>
                        <div class="font-weight-normal">
                          <strong>{{ message.from }}</strong> @{{
                            message.time
                          }}
                        </div>
                        <div>{{ message.message }}</div>
                      </div>
                    </v-timeline-item>
                  </v-timeline>
                </v-card-text>
              </v-card>
            </v-tab-item>
            <v-tab-item>
              <v-card flat>
                <v-card-text>
                  <v-layout wrap row>
                    <v-flex xs12 sm6 md6 class="pb-2" v-for="i in 2" :key="i">
                      <v-card>
                        <v-container pa-1>
                          <v-layout row>
                            <v-flex xs5>
                              <v-card-title primary-title> </v-card-title>
                              <img
                                thumbnail
                                width="50"
                                height="50"
                                :src="champ1.imgsrc"
                              />
                            </v-flex>
                            <v-flex xs5>
                              <v-card-title primary-title>
                                <div>
                                  <div class="grey --text">전체 사용자</div>
                                  <h3 class="headline">123</h3>
                                </div>
                              </v-card-title>
                            </v-flex>
                          </v-layout>
                          <v-divider light></v-divider>
                          <v-card-actions class="pa-2">
                            <v-icon small color="primary">update</v-icon>
                            <span class="grey--text caption font-italic"
                              >&nbsp;5분전</span
                            >
                            <v-spacer></v-spacer>
                          </v-card-actions>
                        </v-container>
                      </v-card>
                    </v-flex>
                  </v-layout>
                </v-card-text>
              </v-card>
            </v-tab-item>
            <v-tab-item>
              <v-card flat class="text-center mt-4">
                <h2>AI SNAPSHOT</h2>
                <v-expansion-panels>
                  <v-expansion-panel v-for="panel in panels" :key="panel.id">
                    <v-expansion-panel-header>
                      <v-flex>
                        <h3>Duration Time {{ panel.time }}</h3>
                        <v-img
                          :src="panel.src"
                          width="800"
                          height="400"
                          class="mt-4"
                        />
                      </v-flex>
                    </v-expansion-panel-header>
                    <v-expansion-panel-content>
                      <h3 v-html="panel.content"></h3>
                      <p v-html="panel.info"></p>
                    </v-expansion-panel-content>
                  </v-expansion-panel>
                </v-expansion-panels>
              </v-card>
            </v-tab-item>
            <v-tab-item>
              <v-card flat>
                <v-card-text>
                  <!--line chart-->
                  <v-card class="mx-auto" width="800">
                    <v-card-title>
                      <v-icon
                        :color="checking ? 'red lighten-2' : 'indigo'"
                        class="mr-12"
                        size="64"
                        @click="takePulse"
                      >
                        mdi-heart-half-full
                      </v-icon>
                      <v-row align="start">
                        <div class="caption grey--text text-uppercase">
                          BATTLE STATE
                        </div>
                        <div>
                          <span
                            class="display-2 font-weight-black"
                            v-text="avg || '—'"
                          ></span>
                          <strong v-if="avg">BPM</strong>
                        </div>
                      </v-row>

                      <v-spacer></v-spacer>

                      <v-btn icon class="align-self-start" size="28">
                        <v-icon>mdi-arrow-right-thick</v-icon>
                      </v-btn>
                    </v-card-title>
                    <v-sparkline
                      :value="value"
                      :labels="labels"
                      :gradient="gradient"
                      :smooth="radius || false"
                      :padding="padding"
                      :line-width="width"
                      :stroke-linecap="lineCap"
                      :gradient-direction="gradientDirection"
                      :fill="fill"
                      :type="type"
                      :auto-line-width="autoLineWidth"
                      auto-draw
                    ></v-sparkline>
                  </v-card>
                  <!-- pie chart-->
                  <v-card class="mt-4">
                    <v-layout wrap row>
                      <v-flex xs12 sm6 md6 text-center>
                        <h3>영상이전 승률</h3>
                        <h3>
                          <strong style="color: #646ac8">{{
                            before_bluescore
                          }}</strong>
                          vs
                          <strong style="color: #d71616">{{
                            before_redscore
                          }}</strong>
                        </h3>
                        <pie-chart
                          :donut="true"
                          :data="[
                            ['BLUETEAM', before_bluescore],
                            ['REDTEAM', before_redscore],
                          ]"
                          :colors="['#23285c', '#d71616']"
                          suffix="%"
                        ></pie-chart>
                      </v-flex>
                      <v-flex xs12 sm6 md6 text-center>
                        <h3>영상이후 승률</h3>
                        <h3>
                          <strong style="color: #646ac8">{{
                            after_bluescore
                          }}</strong>
                          vs
                          <strong style="color: #d71616">{{
                            after_redscore
                          }}</strong>
                        </h3>
                        <pie-chart
                          :donut="true"
                          :data="[
                            ['BLUETEAM', after_bluescore],
                            ['REDTEAM', after_redscore],
                          ]"
                          :colors="['#23285c', '#d71616']"
                          suffix="%"
                        ></pie-chart>
                      </v-flex>
                    </v-layout>
                  </v-card>
                  <!--another chart-->
                </v-card-text>
              </v-card>
            </v-tab-item>
          </v-tabs>
        </v-card>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import axios from "axios";
//import "../../assets/css/comment.css";
import Vue from "vue";
import Chartkick from "vue-chartkick";
import Chart from "chart.js";

const gradients = [
  ["#C62828"],
  ["#303F9F"],
  ["#2196F3", "#9575CD", "#F44336"],
  ["purple", "violet"],
  ["#00c6ff", "#F0F", "#FF0"],
  ["#f72047", "#ffd200", "#1feaea"],
];

Vue.use(Chartkick.use(Chart));
export default {
  data() {
    return {
      width: 2,
      radius: 10,
      padding: 8,
      lineCap: "round",
      gradient: gradients[2],
      value: [48.95, 47, 45, 46, 47, 47.85],
      labels: [
        "0 sec",
        "5 sec",
        "15 sec",
        "20 sec",
        "25 sec",
        "30 sec",
        "35 sec",
      ],
      gradientDirection: "top",
      gradients,
      fill: false,
      type: "trend",
      autoLineWidth: false,

      messages: [
        {
          time: "15:43",
          from: "샤코",
          color: "#3F51B5",
          message: "대지 드래곤 KILL",
        },
        {
          time: "15:45",
          from: "노틸러스",
          color: "#F44336",
          message: "스웨인 KILL",
        },
        {
          time: "15:54",
          from: "노틸러스",
          color: "#F44336",
          message: "샤코 KILL",
        },
        {
          time: "16:02",
          from: "아리",
          color: "#3F51B5",
          message: "헤카림 KILL",
        },
        {
          time: "16:05",
          from: "아리",
          color: "#3F51B5",
          message: "노틸러스 KILL",
        },
      ],
      panels: [
        {
          id: 1,
          time: "15:37",
          src: require("@/assets/img/a1.png"),
          content: "샤코, 뽀삐 챔피언이 감지되었습니다",
          info:
            "샤코 TOTAL GOLD: 3750, DAMAGE: 2100 <br> 뽀삐 TOTAL GOLD: 3800, DAMAGE: 1500 ",
        },
        {
          id: 2,
          time: "15:45",
          src: require("@/assets/img/a2.png"),
          content: "노틸러스, 뽀삐, 이즈리얼, 오른 챔피언이 감지되었습니다",
          info:
            "노틸러스 TOTAL GOLD: 3750, DAMAGE: 2100 <br> 뽀삐 TOTAL GOLD: 3800, DAMAGE: 1500  <br> 이즈리얼 TOTAL GOLD: 4000, DAMAGE: 3200   <br> 오른 TOTAL GOLD: 3000, DAMAGE: 500  ",
        },
        {
          id: 3,
          time: "15:53",
          src: require("@/assets/img/a3.png"),
          content:
            "샤코, 노틸러스, 뽀삐, 이즈리얼, 오른 챔피언이 감지되었습니다",
          info:
            "샤코 TOTAL GOLD: 3750, DAMAGE: 2100 <br> 노틸러스 TOTAL GOLD: 3000, DAMAGE: 2500 <br> 뽀삐 TOTAL GOLD: 3800, DAMAGE: 1500 <br> 이즈리얼 TOTAL GOLD: 3900, DAMAGE: 3300 <br> 오른 TOTAL GOLD: 4800, DAMAGE: 2000  ",
        },
        {
          id: 4,
          time: "16:01",
          src: require("@/assets/img/a4.png"),
          content: "아리, 뽀삐, 오른, 헤카림, 카이사 챔피언이 감지되었습니다",
          info:
            "아리 TOTAL GOLD: 3750, DAMAGE: 2100 <br> 뽀삐 TOTAL GOLD: 3000, DAMAGE: 2500 <br> 오른 TOTAL GOLD: 3800, DAMAGE: 1500 <br> 헤카림 TOTAL GOLD: 3900, DAMAGE: 3300 <br> 카이사 TOTAL GOLD: 4800, DAMAGE: 2000  ",
        },
        {
          id: 5,
          time: "16:06",
          src: require("@/assets/img/a5.png"),
          content: "아리, 노틸러스 챔피언이 감지되었습니다",
          info:
            "아리 TOTAL GOLD: 3750, DAMAGE: 2100 <br> 노틸러스 TOTAL GOLD: 3000, DAMAGE: 2500 ",
        },
      ],
      sessionUserNo: "",
      sessionUser: {},
      videoPostNo: this.$route.params.videoNo,
      writePost: {},
      videolink: "",
      state: "",
      videoData: "",
      before_bluescore: "48.95",
      before_redscore: "51.05",
      after_bluescore: "47.85",
      after_redscore: "52.15",
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
      likeStatus: true,
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
          if (
            this.writePost.isPrivate != 0 &&
            this.writePost.userNo != this.sessionUserNo
          ) {
            alert("비밀글입니다.");
            location.href = "/vlist";
          }
          if (this.sessionUserNo) {
            //좋아요 여부 불러오기
            axios
              .post(process.env.VUE_APP_API_URL + "/vlikes/status", {
                videoPostNo: this.videoPostNo,
                userNo: this.sessionUserNo,
              })
              .then((like) => {
                console.log(like);
                if (like.data.object) {
                  this.likeStatus = false;
                } else {
                  this.likeStatus = true;
                }
              });
          }
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
        .replace("_1.jpg", ".png");
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
              videoPostNo: this.videoPostNo,
            },
          })
          .then(() => {
            alert("삭제 완료");
            location.href = "/vlist";
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
    likesup() {
      this.loginCheck() &&
        axios
          .post(process.env.VUE_APP_API_URL + "/vlikes/", {
            videoPostNo: this.videoPostNo,
            userNo: this.sessionUserNo,
          })
          .then(() => {
            this.likeStatus = !this.likeStatus;
            this.writePost.totalLike++;
          });
    },

    likesdown() {
      this.loginCheck() &&
        axios
          .delete(process.env.VUE_APP_API_URL + "/vlikes/", {
            params: {
              videoPostNo: this.videoPostNo,
              userNo: this.sessionUserNo,
            },
          })
          .then(() => {
            this.likeStatus = !this.likeStatus;
            this.writePost.totalLike--;
          });
    },
  },
};
</script>

<style>
</style>