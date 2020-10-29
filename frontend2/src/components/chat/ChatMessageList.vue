<template>
  <v-list v-auto-bottom="msgs">
    <transition-group name="list" >
      <div v-for="(msg,index) in msgs" v-bind:key="index">
        <v-list-tile>
          <v-list-tile-action>
            <span>{{msg.from.name}}</span>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>{{msg.msg}}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-divider inset></v-divider>
      </div>
    </transition-group>
  </v-list>
</template>

<script>
export default {
    name: 'ChatMessageList'
}
</script>

<style>

</style>