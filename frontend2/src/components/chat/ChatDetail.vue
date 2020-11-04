<template>
  <v-card style="height: 500px; margin:10px 0 0 0">
    <v-toolbar
      color="indigo"
      dark
    >
      <v-btn icon @click="$emit('back')">
        <v-icon>mdi-close</v-icon>
      </v-btn>
      <v-toolbar-title>{{ msg.title }}</v-toolbar-title>
      <v-spacer></v-spacer>
    </v-toolbar>
    <div style="height: 380px;">
    </div>
    <div class="d-flex" style="padding:0 5px 0 15px">
        <v-text-field filled dense></v-text-field>
        <v-btn icon @click="$emit('back')">
            <v-icon bottom>mdi-send</v-icon>
      </v-btn>
    </div>
  </v-card>
</template>

<script>
export default {
    name: 'ChatDetail',
    props: {
        msg: {
            type: Object
        }
    },
}
</script>

<style>
</style>