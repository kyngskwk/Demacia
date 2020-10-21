<template>
  <v-list>
    <v-list-item-group
      v-model="selected"
      active-class="blue--text"
      multiple
    >
      <MessageList v-for="msg in msgs" :key="msg.pk" :msg="msg"/>
    </v-list-item-group>
  </v-list>
</template>

<script>
import MessageList from "./MessageList.vue"

export default {
  name: 'TrashMessage',
  components: {
    MessageList
  },
  data: () => ({
      selected: [2],
      msgs: [
        {
          pk: 1,
          action: '15 min',
          headline: 'Brunch this weekend?',
          subtitle: `I'll be in your neighborhood doing errands this weekend. Do you want to hang out?`,
          title: 'Ali Connors',
        },
      ],
    }),

}
</script>

<style scoped>
.v-list {
  padding:0 100px 0 30px
}
</style>