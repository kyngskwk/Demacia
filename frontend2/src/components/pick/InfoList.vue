<template>
    <v-card outlined class="gameinfo mb-1">
        <div v-if="game.win == true" style="background:#FFCDD2">{{ game.champion }} | {{ game.role }}
            <img :src="game.lane" alt="" style="width:20px">
            <v-chip x-small color="red darken-1" style="color:white" class="ml-2">WIN</v-chip>
        </div>
        <div v-if="game.win == false" style="background:#ECEFF1">{{ game.champion }} | {{ game.role }}
            <img :src="game.lane" alt="" style="width:20px">
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
    created() {
        this.game.lane = require(`../../assets/lane/` + this.game.lane + `.png`)
    }
}
</script>

<style>
</style>