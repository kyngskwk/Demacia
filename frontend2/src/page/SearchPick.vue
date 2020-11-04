<template>
  <div class="container text-center">
    <h1 class="mb-5">대기실 전적기록 검색</h1>

    <v-textarea 
        label="대기실 전적기록 검색하기"
        placeholder="대기실의 입장 안내 문구를 붙여넣기 해주세요!"
        outlined
        v-model="realtxt"
    ></v-textarea>
    <p v-if="infoerror">{{ userinfo }}</p>
    <v-btn class="searchbtn blue-grey" @click="gosearch">검색하기</v-btn>
    <!-- 결과 안내창 -->
    <v-card class="mt-5">
      <img v-if="infoshow" src="../assets/img/pickinfo.png" alt="" class="pt-5 pb-3">
      <UserInfoList v-if="!infoshow" :userinfo="userinfo"/>
    </v-card>
  </div>
</template>

<script>
import axios from 'axios'
import UserInfoList from '../components/pick/UserInfoList.vue'

export default {
    name: 'SearchPick',
    components: {
      UserInfoList
    },
    data() {
      return {
        realtxt: '',
        infoshow: true,
        inputtxt: '',
        userinfo: '',
        infoerror: false,
      }
    },
    methods: {
      gosearch() {
        this.inputtxt=this.realtxt.split('\n')
        console.log(this.inputtxt)
        axios.post(`http://127.0.0.1:8000/django/api/usersinfo/`, {
          inputtxt: this.inputtxt
        }).then(response => {
          this.userinfo = response.data
          if (typeof this.userinfo == 'string') {
            this.infoerror = true
            this.infoshow = true
          } else {
            this.infoerror = false
            this.infoshow = false
          }
        })
      }
    }
}
</script>

<style scoped>
.searchbtn {
    display: inline-block;
    width: 100%;
    color: white;
}
</style>