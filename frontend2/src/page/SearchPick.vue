<template>
  <div class="container text-center">
    <h1 class="mb-5">대기실 전적기록 검색</h1>

    <v-textarea 
        label="대기실 전적기록 검색하기"
        placeholder="대기실의 입장 안내 문구를 붙여넣기 해주세요!"
        outlined>
    </v-textarea>
    <v-btn class="searchbtn blue-grey">검색하기</v-btn>
    <v-card class="mt-5">
        결과나옴
    </v-card>
  </div>
</template>

<script>
export default {
    name: 'SearchPick'
}
</script>

<style scoped>
.searchbtn {
    display: inline-block;
    width: 100%;
    color: white;
}
</style>