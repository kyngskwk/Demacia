<template>
  <div>
    <div class="d-flex" v-if="listshow">
        <v-checkbox :input-value="active"></v-checkbox>
        <v-list-item :key="msg.title" @click="godetail">
          <template>
            <v-list-item-content>
              <v-list-item-title v-text="msg.title"></v-list-item-title>

              <v-list-item-subtitle
                class="text--primary"
                v-text="msg.headline"
              ></v-list-item-subtitle>

              <v-list-item-subtitle v-text="msg.subtitle"></v-list-item-subtitle>
            </v-list-item-content>
          </template>
        </v-list-item>
        <v-divider></v-divider>
    </div>
    <ChatDetail  v-if="chatshow" :msg="msg" @back="back"/>
  </div>
</template>

<script>
import ChatDetail from './ChatDetail.vue'

export default {
    name: 'ChatlistItem',
    components: {
      ChatDetail
    },
    props: {
        msg: {
            type: Object
        }
    },
    data() {
      return {
        listshow: true,
        chatshow: false,
      }
    },
    methods: {
      godetail() {
        this.listshow = false
        this.chatshow = true
      },
      back() {
        this.listshow = true
        this.chatshow = false
      }
    }
}
</script>

<style>

</style>