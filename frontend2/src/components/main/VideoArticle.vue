<template>
    <v-card class="mt-5">
      <v-toolbar color="blue-grey" dark class="mb-5">
        <v-toolbar-title>영상 분석</v-toolbar-title>
      </v-toolbar>
      <v-row dense class="pa-3">
        <v-col
          v-for="card in cards"
          :key="card.title"
          :cols="card.flex"
        >
          <v-card>
            <v-img
              :src="card.src"
              class="white--text align-end"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
              height="200px"
            >
              <v-card-title v-text="card.title"></v-card-title>
            </v-img>

            <v-card-actions>
            
    <v-btn
      class="ma-2"
      :loading="loading"
      :disabled="loading"
      color="secondary"
      @click="videodetail1"
    >
      <h2><strong>자세히 보기</strong></h2>  
    </v-btn>

              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-card>
</template>

<script>
export default {
    name: 'VideoAritcle',
    data: () => ({
      cards: [
        { title: 'No.1', src: require('../../assets/img/video1img0.jpg'),  flex: 4 },
        { title: 'Favorite road trips', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex: 4 },
        { title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 4 },
      ],
    }),        
    methods: {
    videodetail1() {
      this.$router.push({ name: "VideoDetail" });
    },
    }
}
</script>

<style>

</style>