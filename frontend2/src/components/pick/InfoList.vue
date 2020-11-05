<template>
    <v-card outlined class="gameinfo mb-1">
        <div v-if="game.win == true" style="background:#FFCDD2">{{ game.champion }} | {{ game.role }} | {{ game.lane }}
        </div>
        <div v-if="game.win == false" style="background:#BBDEFB">{{ game.champion }} | {{ game.role }} | {{ game.lane }}
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
    }
}
</script>

<style>
</style>