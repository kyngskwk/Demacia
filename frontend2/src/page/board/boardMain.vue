<template>
  <v-container>
    <v-card>
      <v-toolbar flat>
        <v-toolbar-title> 커뮤니티 </v-toolbar-title>
        <v-spacer />
        <v-btn @click="write">글쓰기</v-btn>
      </v-toolbar>
      <v-tabs vertical>
        <v-tab> 공지사항 </v-tab>
        <v-divider />
        <v-tab> 자유게시판 </v-tab>
        <v-tab> 유머게시판 </v-tab>
        <v-divider />
        <v-tab> 투표게시판 </v-tab>
        <v-tab> 영상분석 </v-tab>

        <!-- 공지 -->
        <v-tab-item><Notice /></v-tab-item>
        <!-- 자게 -->
        <v-tab-item><Free /></v-tab-item>
        <!-- 유게 -->
        <v-tab-item><Humor /></v-tab-item>
        <!-- 투표게 -->
        <v-tab-item><Vote /></v-tab-item>
        <!-- 영분 -->
        <v-tab-item><Video /></v-tab-item>
      </v-tabs>
    </v-card>
  </v-container>
</template>

<script>
import Notice from "@/components/board/list/Notice";
import Free from "@/components/board/list/Free";
import Humor from "@/components/board/list/Humor";
import Vote from "@/components/board/list/Vote";
import Video from "@/components/board/list/Video";
export default {
  components: {
    Notice,
    Free,
    Humor,
    Vote,
    Video,
  },
  methods: {
    write() {
      alert("글을 쓸 것임");
      this.$route.push({ name: "postWrite" });
    },
  },
};
</script>

<style>
</style>