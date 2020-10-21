<template>
    <div>
        <Carousel />
        <div class="container mt-5">
            <v-toolbar
                dark
                color="blue-grey"
            >
                <v-toolbar-title>전적기록 검색하기</v-toolbar-title>
                <v-autocomplete
                v-model="select"
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
                <v-btn icon>
                <v-icon left>mdi-magnify</v-icon>
                </v-btn>
            </v-toolbar>
            <v-row class="mt-5">
                <v-col cols="6"><BestArticle/></v-col>
                <v-col cols="6"><VoteArticle/></v-col>
            </v-row>
            <VideoAritcle />
        </div>
    </div>
</template>

<script>
import Carousel from "../components/common/Carousel.vue";
import BestArticle from "../components/main/BestArticle.vue";
import VoteArticle from "../components/main/VoteArticle.vue";
import VideoAritcle from "../components/main/VideoArticle";

export default {
    name: 'Main',
    components: {
        Carousel,
        BestArticle,
        VoteArticle,
        VideoAritcle,
    },
}
</script>

<style>
</style>