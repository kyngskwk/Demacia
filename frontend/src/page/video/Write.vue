<template>
  <div style="height: 100%; font-family: Tmon">
    <b-row class="justify-content-center">
      <b-col cols="10" md="6" lg="4" style="margin-top: 5%">
        <div class="box">
          <h2 style="font-weight: bold">영상 등록</h2>
          <div class="row">
            <div class="col-md-12 text-center">
              {{ popoverStr[isVideoUploaded] }}
            </div>
            <div class="col-md-12 text-center">
              <b-icon-caret-right-square-fill
                font-scale="13"
                type="button"
                @click="openUploadWindows"
                v-if="isVideoUploaded == 0"
                v-b-popover.hover.left="'동영상 업로드'"
              />
              <b-icon
                icon="gear-fill"
                animation="spin"
                font-scale="13"
                type="button"
                @click="cancelUpload"
                v-else-if="isVideoUploaded == 1"
              />
              <b-icon
                icon="file-check"
                font-scale="13"
                type="button"
                @click="dataCheck"
                v-else-if="isVideoUploaded == 2"
              />
              <h2 class="m-4">
                {{ uploadMSG }}
              </h2>
              <!---->
              <input
                type="file"
                id="videoURL"
                ref="uploadvideoURL"
                @change="onSaveVideo"
                accept="video/*"
                aria-describedby="addon-right addon-left"
                placeholder="영상 업로드"
                hidden
              />
            </div>
            <div class="col-md-12">
              <b-form-checkbox
                id="checkbox-private"
                v-model="isPrivate"
                name="checkbox-private"
                :value="1"
                :unchecked-value="0"
                >나만 보기</b-form-checkbox
              >
            </div>
            <div class="col-md-12">
              내 Sol 포인트 :
              <Strong>{{ userMileage }}</Strong>
              <p style="color: red">※ 50 Sol차감</p>
            </div>
          </div>
          <!---->
        </div>
      </b-col>
    </b-row>
  </div>
</template>


<script>
import axios from "axios";

export default {
  name: "Write",

  data: function () {
    return {
      no: JSON.parse(sessionStorage.getItem("user")).userNo,
      isVideoUploaded: 0,
      popoverStr: ["동영상 업로드", "업로드 취소", "영상 게시"],
      mileage: 50,
      thumbnail: "0",
      data: "0",
      video: "0",
      userMileage: "",
      uploadMSG: "　",
      isPrivate: 0,
    };
  }, //data
  created() {
    window.scrollTo(0, 0);
    this.getUserMileage();
  },
  methods: {
    cancelUpload() {
      this.isVideoUploaded = 0;
    },
    openUploadWindows() {
      document.getElementById("videoURL").click();
      this.isVideoUploaded = 1;
    },
    getUserMileage() {
      axios
        .get(process.env.VUE_APP_API_URL + "/user/mileage", {
          params: {
            userNo: this.no,
          },
        })
        .then((res) => {
          this.userMileage = res.data.object;
        });
    },
    onSaveVideo() {
      let fileURL = this.$refs.uploadvideoURL.files[0];
      this.video = this.$refs.uploadvideoURL.files[0].name;
      console.log(this.video);
      let fdv = new FormData();
      fdv.append("upLoadVideo2", fileURL, this.video);
      this.uploadMSG = "업로드 중...";
      axios
        .post(process.env.VUE_APP_IMGUP_URL + "/uploadvideo2", fdv, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then(() => {
          console.log("video upload success");
          this.uploadMSG = "업로드 성공. 영상 분석API는 이단계에서 불러옴";
          // DATA APIAPI
          axios
            .get(/* 데이터 분석하는 API */)
            .then((res) => {
              this.data = res.object.data;
              // 썸네일 이미지를 file로 받으면 imgup으로 등록
              let thumbnailFile = res.object.thumbnail;
              this.thumbnail = thumbnailFile.name;
              this.uploadMSG = "썸네일이미지 추출중...";
              axios
                .post(
                  process.env.VUE_APP_IMGUP_URL + "/uploadvideo2",
                  new FormData().append(
                    "upLoadThum2",
                    thumbnailFile,
                    this.thumbnail
                  ),
                  {
                    headers: {
                      "Content-Type": "multipart/form-data",
                    },
                  }
                )
                .then(() => {
                  this.uploadMSG = "영상 업로드 및 분석 성공";
                  this.isVideoUploaded = 2;
                });
            })
            .catch(() => {
              console.log("data fail");
              this.uploadMSG = "분석 실패";
              this.isVideoUploaded = 2;
            });
        })
        .catch(() => {
          console.log("video upload fail");
          this.uploadMSG = "업로드 실패";
          this.isVideoUploaded = 0;
        });
    },

    dataCheck() {
      let err = false;
      let msg = "";
      this.userMileage - this.mileage < 0 &&
        ((msg = "마일리지가 부족합니다."), (err = true));
      if (err) alert(msg);
      else this.dataSend();
    }, //dataCheck

    dataSend() {
      axios
        .post(process.env.VUE_APP_API_URL + "/video/", {
          userNo: this.no,
          video: this.video,
          thumbnail: this.thumbnail,
          data: this.data,
          isPrivate: this.isPrivate,
        })
        .then(() => {
          alert("등록이 완료되었습니다.");
          location.href = "/vlist";
        })
        .catch(() => {
          location.href = "/error/영상 업로드에 실패했습니다.";
        });
    },
  },
};
</script>

<style>
.button1 {
  display: inline-block;
  outline: none;
  cursor: pointer;
  text-align: center;
  text-decoration: none;
  font: 14px/100% Arial, Helvetica, sans-serif;
  padding: 0.5em 2em 0.55em;
  text-shadow: 0 1px 1px rgba(0, 0, 0, 0.3);
  -webkit-border-radius: 0.5em;
  -moz-border-radius: 0.5em;
  border-radius: 0.5em;
  -webkit-box-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
  -moz-box-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
}
.button1:hover {
  text-decoration: none;
}
.button1:active {
  position: relative;
  top: 1px;
}
.blue {
  color: #d9eef7;
  border: solid 1px #0076a3;
  background: #0095cd;
  background: -webkit-gradient(
    linear,
    left top,
    left bottom,
    from(#00adee),
    to(#0078a5)
  );
}
.blue:hover {
  background: #8bc1ee;
  background: -webkit-gradient(
    linear,
    left top,
    left bottom,
    from(#9acaf1),
    to(#6bafe7)
  );
}
.blue:active {
  color: #8bc1ee;
  background: -webkit-gradient(
    linear,
    left top,
    left bottom,
    from(#9acaf1),
    to(#6bafe7)
  );
}
.box {
  border-style: ridge;
  border: #fcd000 4px ridge;
  opacity: 0.8;
  background: linear-gradient(
    180deg,
    rgba(14, 36, 56, 1) 0%,
    rgba(32, 17, 95, 1) 100%
  );
  margin: 1rem;
  width: 100%;
  background-color: white;
  box-shadow: 5px 5px 5px;
  color: #e3d19e;
}
</style>
