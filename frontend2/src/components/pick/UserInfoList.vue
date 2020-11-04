<template>
  <div>
      <UserInfoItem v-for="(info, i) in userinfo" :key="i" :info="info" class="mb-5"/>
  </div>
</template>

<script>
import UserInfoItem from './UserInfoItem.vue'

export default {
    name: 'UserInfoList',
    props: {
        userinfo: {
            type: Object
        }
    },
    components: {
        UserInfoItem,
    }
}
</script>

<style>

</style>