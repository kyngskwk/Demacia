<template>
    <v-card>
        <v-card-title>
            <v-icon class="mr-2">mdi-account-circle</v-icon>
            <span>{{ info.name }}</span>
        </v-card-title>
        <InfoList v-for="(game, i) in info.games" :key="i" :game="game"/>
    </v-card>
</template>

<script>
import InfoList from './InfoList.vue'

export default {
    name: 'UserInfoItem',
    components: {
        InfoList,
    },
    props: {
        info: {
            type: Object
        }
    },
    created() {
        console.log(this.info.games)
    }
}
</script>

<style>

</style>