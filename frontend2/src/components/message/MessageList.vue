<template>
    <div class="d-flex">
        <v-checkbox :input-value="active"></v-checkbox>
        <v-list-item :key="msg.title">
          <template v-slot:default="{ active }">
            <v-list-item-content>
              <v-list-item-title v-text="msg.title"></v-list-item-title>

              <v-list-item-subtitle
                class="text--primary"
                v-text="msg.headline"
              ></v-list-item-subtitle>

              <v-list-item-subtitle v-text="msg.subtitle"></v-list-item-subtitle>
            </v-list-item-content>

            <v-list-item-action>
              <v-list-item-action-text v-text="msg.action"></v-list-item-action-text>

              <v-icon
                v-if="!active"
                color="grey lighten-1"
              >
                mdi-star-outline
              </v-icon>

              <v-icon
                v-else
                color="yellow darken-3"
              >
                mdi-star
              </v-icon>
            </v-list-item-action>
          </template>
        </v-list-item>
        <v-divider></v-divider>
    </div>
</template>

<script>
export default {
    name: 'MessageList',
    props: {
        msg: {
            type: Object
        }
    }
}
</script>

<style>

</style>