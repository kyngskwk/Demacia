<template>
    <v-navigation-drawer
        absolute
        permanent
        right
        expand-on-hover
    >
        <v-list>
        <v-list-item class="px-2">
            <v-list-item-avatar>
            <v-img src="https://randomuser.me/api/portraits/women/85.jpg"></v-img>
            </v-list-item-avatar>
        </v-list-item>

        <v-list-item link>
            <v-list-item-content>
            <v-list-item-title class="title">
                DEMACIA
            </v-list-item-title>
            <v-list-item-subtitle>demacia@gmail.com</v-list-item-subtitle>
            </v-list-item-content>
        </v-list-item>
        </v-list>

        <v-divider></v-divider>

        <v-list
        nav
        dense
        >
        <v-list-item link>
            <v-list-item-icon>
            <v-icon>mdi-account</v-icon>
            </v-list-item-icon>
            <v-list-item-title>마이페이지</v-list-item-title>
        </v-list-item>
        <v-list-item link>
            <v-list-item-icon>
            <v-icon>mdi-chart-bar</v-icon>
            </v-list-item-icon>
            <v-list-item-title>나의 전적기록</v-list-item-title>
        </v-list-item>
        <v-list-item link @click="goMessage">
            <v-list-item-icon>
            <v-icon>mdi-message-text-outline</v-icon>
            </v-list-item-icon>
            <v-list-item-title>쪽지</v-list-item-title>
        </v-list-item>
        <v-list-item link>
            <v-list-item-icon>
            <v-icon>mdi-dots-horizontal</v-icon>
            </v-list-item-icon>
            <v-list-item-title>설정</v-list-item-title>
        </v-list-item>
        </v-list>
    </v-navigation-drawer>
</template>

<script>
export default {
    name: "SideNavi",
    methods: {
        goMessage() {
            this.$router.push({name: 'Message'})
        }
    }
}
</script>

<style>
</style>