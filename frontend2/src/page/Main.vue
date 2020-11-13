<template>
    <div>
        <Carousel />
        <div class="container mt-5 mb-10">
            <v-toolbar
                dark
                style="background:linear-gradient(to right, rgb(247,202,201), rgb(146,168,209))"
            >
                <v-toolbar-title>전적기록 검색하기</v-toolbar-title>
                <v-autocomplete
                v-model="nickname"
                :loading="loading"
                :items="items"
                :search-input.sync="search"
                cache-items
                class="mx-4"
                hide-no-data
                hide-details
                label="소환사명을 입력하세요!"
                solo-inverted
                ></v-autocomplete>
                <v-btn icon @click="gosearch">
                <v-icon left>mdi-magnify</v-icon>
                </v-btn>
            </v-toolbar>
            <v-row class="mt-5">
                <v-col cols="6"><BestArticle/></v-col>
                <v-col cols="6"><VoteArticle/></v-col>
            </v-row>
            <VideoAritcle />
        </div>
        <MessageForm/>
        
    </div>
</template>

<script>
import Carousel from "../components/common/Carousel.vue";
import BestArticle from "../components/main/BestArticle.vue";
import VoteArticle from "../components/main/VoteArticle.vue";
import VideoAritcle from "../components/main/VideoArticle";
import MessageForm from "../components/message/MessageForm.vue";

export default {
    name: 'Main',
    components: {
        Carousel,
        BestArticle,
        VoteArticle,
        VideoAritcle,
        MessageForm,
    },
    data() {
        return {
            nickname: '',
        } 
    },
    methods: {
        gosearch() {
            this.$router.push({name:'UserSearch', params: {nickname: this.nickname}})
        }
    }
}
</script>

<style>
</style>