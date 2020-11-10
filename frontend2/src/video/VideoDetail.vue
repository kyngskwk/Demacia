<template>
  <div>


  <v-container>
    <v-row justify="space-around">
      <v-card width="1000" >
                <v-card-title class="black--text mt-2" >
            <v-avatar size="56">
              <img
                alt="user"
                src="https://cdn.pixabay.com/photo/2020/06/24/19/12/cabbage-5337431_1280.jpg"
              >
            </v-avatar>
            <v-row justify="space-between">
                <div>
                    <p class="ml-7 mt-2">
                        John Doe
                    </p>
                </div>
                <div>
                    <p class="mr-5 mt-2">
                    영상분석 No.1
                    </p>
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
        
       
          <v-app-bar
            flat
            color="rgba(0, 0, 0, 0)"
          >
            <v-app-bar-nav-icon color="white"></v-app-bar-nav-icon>

            <v-toolbar-title class="title white--text pl-0">
              Messages
            </v-toolbar-title>

            <v-spacer></v-spacer>

            <v-btn
              color="white"
              icon
            >
              <v-icon>mdi-dots-vertical</v-icon>
            </v-btn>
          </v-app-bar>


        <source src="./4659518008_01.mp4" type="video/mp4" />
      </video>
    <v-tabs vertical>
      <v-tab class="pl-0">
        <v-icon left>
          mdi-clock-time-four-outline
        </v-icon>
        TIME LINE
      </v-tab>
      <v-tab >
        <v-icon left>
          mdi-account-group
        </v-icon>
        Champions
      </v-tab>
      <v-tab class="pl-2">
        <v-icon left>
          mdi-camera
        </v-icon>
        Snapshot
      </v-tab>
            <v-tab class="pl-2">
        <v-icon left>
          mdi-camera
        </v-icon>
        Chart
      </v-tab>

      <v-tab-item>
        <v-card flat>
         <v-card-text>
          <div class="font-weight-bold ml-8 mb-2">
            TIME LINE
          </div>

          <v-timeline
            align-top
            dense
          >



          
            <v-timeline-item
              v-for="message in messages"
              :key="message.time"
              :color="message.color"
              small
            >
              <div>
                <div class="font-weight-normal">
                  <strong>{{ message.from }}</strong> @{{ message.time }}
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
       
        <v-flex xs12 sm6 md6 class="pb-2" v-for="i in 4" :key="i">
          <v-card>
            <v-container pa-1>
              <v-layout row>
                <v-flex xs5>
                  <v-card-title primary-title>
                    <div>
                      <div class="grey--text">전체 사용자</div>
                      <h3 class="headline">123</h3>
                    </div>
                  </v-card-title>
                </v-flex>

                <v-flex xs5>
                  <v-card-title primary-title>
                    <v-avatar>
                      <v-icon medium color="success">person</v-icon>
                    </v-avatar>
                  </v-card-title>
                </v-flex>
              </v-layout>
                            <v-divider light></v-divider>
              <v-card-actions class="pa-2">
                <v-icon small color="primary">update</v-icon>
                <span class="grey--text caption font-italic">&nbsp;5분전</span>
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
        <v-card flat>
          <v-card-text>
            <p>
              Fusce a quam. Phasellus nec sem in justo pellentesque facilisis. Nam eget dui. Proin viverra, ligula sit amet ultrices semper, ligula arcu tristique sapien, a accumsan nisi mauris ac eros. In dui magna, posuere eget, vestibulum et, tempor auctor, justo.
            </p>

            <p class="mb-0">
              Cras sagittis. Phasellus nec sem in justo pellentesque facilisis. Proin sapien ipsum, porta a, auctor quis, euismod ut, mi. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nam at tortor in tellus interdum sagittis.
            </p>
          </v-card-text>
        </v-card>
      </v-tab-item>
       <v-tab-item>
        <v-card flat>
          <v-card-text>
            <p>
              Fusce a quam. Phasellus nec sem in justo pellentesque facilisis. Nam eget dui. Proin viverra, ligula sit amet ultrices semper, ligula arcu tristique sapien, a accumsan nisi mauris ac eros. In dui magna, posuere eget, vestibulum et, tempor auctor, justo.
            </p>

            <p class="mb-0">
              Cras sagittis. Phasellus nec sem in justo pellentesque facilisis. Proin sapien ipsum, porta a, auctor quis, euismod ut, mi. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nam at tortor in tellus interdum sagittis.
            </p>
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
// import Vue from "vue";
// import Chartkick from "vue-chartkick";
// import Chart from "chart.js";

// Vue.use(Chartkick.use(Chart));
export default {
  data() {
    return {
        messages: [
        { time: '15:43', from:"샤코", color:"#3F51B5",  message: "대지 드래곤 KILL" },
        { time: '15:45', from:"노틸러스", color:"#F44336",  message: "스웨인 KILL" },
        { time: '15:54', from:"노틸러스", color:"#F44336",  message: "샤코 KILL" },
        { time: '16:02', from:"아리", color:"#3F51B5",  message: "헤카림 KILL" },
        { time: '16:05', from:"아리", color:"#3F51B5",  message: "노틸러스 KILL" },

      ],
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