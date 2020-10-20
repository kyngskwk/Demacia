<template>
  <v-app>
    <v-main>
      <Message/>
    </v-main>
  </v-app>
</template>

<script>
import Message from './views/Message';

export default {
  name: 'App',

  components: {
    Message,
  },

  data: () => ({
    //
  }),
};
</script>
