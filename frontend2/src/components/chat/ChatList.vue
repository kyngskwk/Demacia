<template>
  <v-list>
    <v-list-item-group
      v-model="selected"
      active-class="blue--text"
      multiple
    >

      <ChatListItem v-for="msg in msgs" :key="msg.pk" :msg="msg"/>
    </v-list-item-group>
  </v-list>
</template>


<script>
import ChatListItem from "./ChatListItem.vue"

export default {
  name: 'ChatList',
  components: {
    ChatListItem
  },
  data: () => ({
      selected: [2],
      msgs: [
        {
          pk: 4,
          action: '12 hr',
          headline: 'Birthday gift',
          subtitle: 'Have any ideas about what we should get Heidi for her birthday?',
          title: 'Trevor Hansen',
        },
        {
          pk: 5,
          action: '18hr',
          headline: 'Recipe to try',
          subtitle: 'We should eat this: Grate, Squash, Corn, and tomatillo Tacos.',
          title: 'Britta Holt',
        },
      ],
    }),

}
</script>

<style>
.v-list {
  padding:0 30px
}
</style>