<template>
  <div class="container text-center">
    <h1 class="mb-5">유저 전적기록 검색</h1>

    <v-textarea 
        label="유저 전적기록 검색하기"
        placeholder="검색하고 싶은 유저의 소환사를 입력해주세요!
ex) Hide on Bush"
        outlined
        v-model="nickname"
    ></v-textarea>
    <!-- <p v-if="infoerror">{{ userinfo }}</p> -->
    <v-btn class="searchbtn blue-grey" @click="gosearch">검색하기</v-btn>
    <!-- 결과 안내창 -->
    <div class="loading-container" v-if="isloading">
      <div class="loading"></div>
      <div id="loading-text">loading</div>
    </div>

    <v-card class="mt-5">
    </v-card>

  </div>
</template>

<script>
export default {
    name: 'UserSearch',
    data() {
        return {
            nickname: '',
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