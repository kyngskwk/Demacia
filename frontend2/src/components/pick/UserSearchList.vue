<template>
    <v-col class="col-2">
        <v-card v-if="info.win" class="wingame">
            <v-img width="100%" :src="this.chamurl"></v-img>
            <div>
                <v-chip small color="red darken-1" style="color:white" class="mt-2">
                    WIN
                </v-chip>
            </div>
            <div class="mt-3">
                <img :src="this.raneurl" alt="" style="width:30px; height:30px;">
                <v-chip class="mb-4 ml-2">{{ info.role }}</v-chip>
            </div>
            <v-chip color="red lighten-4">🔪 KILLS 
                <v-avatar right color="white">{{ info.kills }}</v-avatar>
            </v-chip>
            <v-chip class="mt-1" color="grey lighten-4">💀 DEATHS 
                <v-avatar right color="white">{{ info.deaths }}</v-avatar>
            </v-chip>
            <v-chip class="mt-1 mb-2" color="blue lighten-4">💪🏻 ASSIST 
                <v-avatar right color="white">{{ info.assists }}</v-avatar>
            </v-chip>
        </v-card>

        <!--졌을 때-->
        <v-card v-if="!info.win" class="losegame">
            <v-img width="100%" :src="this.chamurl"></v-img>
            <div>
                <v-chip small color="blue-grey" style="color:white" class="mt-2">
                    LOSE
                </v-chip>
            </div>
            <div class="mt-3">
                <img :src="this.raneurl" alt="" style="width:30px; height:30px;">
                <v-chip class="mb-4 ml-2">{{ info.role }}</v-chip>
            </div>
            <v-chip color="red lighten-4">🔪 KILLS 
                <v-avatar right color="white">{{ info.kills }}</v-avatar>
            </v-chip>
            <v-chip class="mt-1" color="grey lighten-4">💀 DEATHS 
                <v-avatar right color="white">{{ info.deaths }}</v-avatar>
            </v-chip>
            <v-chip class="mt-1 mb-2" color="blue lighten-4">💪🏻 ASSIST 
                <v-avatar right color="white">{{ info.assists }}</v-avatar>
            </v-chip>
        </v-card>
    </v-col>
</template>

<script>
export default {
    name: 'UserSearchList',
    props: {
        info: {
            type: Object
        },
    },
    data() {
        return {
            chamurl: '',
            raneurl: ''
        }
    },
    created() {
        console.log(this.info)
        // console.log(this.i)
        this.chamurl = require(`../../assets/tiles/` + this.info.champion + `.png`)
        this.raneurl = require(`../../assets/lane/` + this.info.lane + `.png`)
    }
} 
</script>

<style scoped>
.wingame {
    
}

</style>