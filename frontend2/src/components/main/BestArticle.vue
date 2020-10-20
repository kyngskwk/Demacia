<template>
  <v-card
    class="mx-auto"
    tile
  >
    <v-list dense class="pt-0">
      <v-toolbar color="blue-grey" dark class="mb-5">
        <v-toolbar-title>금주의 인기 게시글</v-toolbar-title>
      </v-toolbar>
      <v-list-item-group
        v-model="item"
        color="primary"
      >
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
        >
          <v-list-item-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title v-text="item.text"></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </v-card>
</template>

<script>
  export default {
    name: 'BestArticle',
    data: () => ({
      item: 1,
      items: [
        { text: '임시로 넣었습니다.'},
        { text: '임시로 넣었습니다.'},
        { text: '임시로 넣었습니다.'},
        { text: '임시로 넣었습니다.'},
        { text: '임시로 넣었습니다.'},
        { text: '임시로 넣었습니다.'},
      ],
    }),
  }
</script>

<style>

</style>