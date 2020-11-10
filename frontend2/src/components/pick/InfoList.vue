<template>
    <v-card outlined class="gameinfo mb-1">
        <div v-if="game.win == true" style="background:#FFCDD2">
            <img :src="chamurl" alt="" style="width:20px">
            {{ game.role }}
            <img :src="laneurl" alt="" style="width:20px">
            <v-chip x-small color="red darken-1" style="color:white" class="ml-2">WIN</v-chip>
        </div>
        <div v-if="game.win == false" style="background:#ECEFF1">
            <img :src="chamurl" alt="" style="width:20px">
            {{ game.role }}
            <img :src="laneurl" alt="" style="width:20px">
            <v-chip x-small color="blue-grey" style="color:white" class="ml-2">LOSE</v-chip>
        </div>
    </v-card>
</template>

<script>
export default {
    name: 'InfoList',
    props: {
        game: {
            type: Object
        }
    },
    data() {
        return {
            chamurl: '',
            laneurl: ''
        }
    },
    created() {
        // console.log(this.game)
        // console.log(this.game)
        this.laneurl = require(`../../assets/lane/` + this.game.lane + `.png`)
        // console.log(this.game.champion)
        this.chamurl = require(`../../assets/tiles/` + this.game.champion + `.png`)
    }
}
</script>

<style>
</style>