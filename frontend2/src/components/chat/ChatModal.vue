<template>
  <v-dialog v-model="dialog" persistent width="900">
    <v-card>
    <v-toolbar
        color="primary"
        cards
        dark
        flat
    >   
        <!-- <v-btn icon @click="$emit('close')">
        <v-icon>mdi-close</v-icon>
        </v-btn> -->
        <v-card-title class="title font-weight-regular">
        채팅창
        </v-card-title>
    </v-toolbar>
    <ChatList v-if="list"/>
    <v-divider></v-divider>
    <v-card-actions>
        <!-- <v-btn
        text
        @click="$refs.form.reset()"
        >
        Clear
        </v-btn> -->
        <v-spacer></v-spacer>
        <v-btn
        class="white--text"
        color="primary"
        depressed
        @click="close"
        >
        닫기
        </v-btn>
    </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import ChatList from './ChatList.vue'

export default {
    name: "ChatModal",
    components: {
        ChatList
    },
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
            list: true,
        }
    },
    methods: {
        send() {
            this.$emit('send')
        },
        // gochat() {
        //     this.list = false
        //     console.log(this.list)
        // },
        close() {
            this.list = true
            this.$emit('close')
        }
    }
}

</script>

<style>

</style>