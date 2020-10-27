<template>
  <v-dialog v-model="dialog" persistent width="900">
    <v-card>
    <v-toolbar
        color="primary"
        cards
        dark
        flat
    >
        <v-btn icon @click="$emit('close')">
        <v-icon>mdi-arrow-left</v-icon>
        </v-btn>
        <v-card-title class="title font-weight-regular">
        메세지 보내기
        </v-card-title>
    </v-toolbar>
    
    <v-divider></v-divider>
    <v-card-actions>
        <v-btn
        text
        @click="$refs.form.reset()"
        >
        Clear
        </v-btn>
        <v-spacer></v-spacer>
        <v-btn
        class="white--text"
        color="primary"
        depressed
        @click="send"
        >
        전송
        </v-btn>
    </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
    name: "ChatList",
    props: {
        dialog: {
            type: Object,
            required: true
        }
    },
    data() {
        return { 
            title: '',
            content: '',
        }
    },
    methods: {
        send() {
            this.$emit('send')
        }
    }
}

</script>

<style>

</style>