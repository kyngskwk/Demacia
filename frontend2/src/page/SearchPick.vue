<template>
  <div class="container text-center">
    <h1 class="mb-5">대기실 전적기록 검색</h1>

    <v-textarea 
        label="대기실 전적기록 검색하기"
        placeholder="대기실의 입장 안내 문구를 붙여넣기 해주세요!"
        outlined
        v-model="realtxt"
    ></v-textarea>
    <v-btn class="searchbtn blue-grey" @click="gosearch">검색하기</v-btn>
    <!-- 결과 안내창 -->
    <v-card class="mt-5">
      <img v-if="infoshow" src="../assets/img/pickinfo.png" alt="" class="pt-5 pb-3">
    </v-card>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'SearchPick',
    data() {
      return {
        realtxt:'',
        infoshow:true,
        inputtxt:'',
      }
    },
    methods: {
      gosearch() {
        this.infoshow=false
        this.inputtxt=this.realtxt.split('\n')
        console.log(this.inputtxt)
        axios.post(`localhost:8000/django/api/usersinfo/`)
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