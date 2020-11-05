<template>
    <v-card>
        <v-card-title>
            <v-icon class="mr-2">mdi-account-circle</v-icon>
            <span>{{ info.name }}</span>
        </v-card-title>
        <v-row class="pa-3">
            <v-col class="col-3 rate">
                <v-progress-circular
                    :rotate="-90"
                    :size="100"
                    :width="15"
                    :value="wingamerate"
                    color="blue-grey">
                    {{ wingamerate }}%
                </v-progress-circular>
                <div class="mt-2">총 {{ totalgame }}개의 게임중 <br> {{ wingame }}게임을 이겼습니다.</div>
            </v-col>
            <v-col class="col-3 infoset">
                라인<br>{{ this.lanelist }}<br>
                챔피언<br>{{ this.chamlist }}
            </v-col>
            <v-col class="col-6">
                <InfoList v-for="(game, i) in info.games" :key="i" :game="game"/>
            </v-col>
        </v-row>
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
    data() {
        return {
            totalgame: '',
            wingame: '',
            wingamerate: 0,
            chamlist: [],
            lanelist: [],
        }
    },
    created() {
        var k = 0;
        var t = 0;
        for (var i in this.info.games) {
            k += 1
            // 이긴 횟수 세기
            if ( this.info.games[i].win == true) {
                t += 1
            }
            // lane 통계
            var lane = this.info.games[i].lane
            if ( !this.lanelist.includes(lane) && lane != 'NONE') {
                this.lanelist.push(lane)
            }
            // champion 통계
            var cham = this.info.games[i].champion
            if ( !this.chamlist.includes(cham)) {
                this.chamlist.push(cham)
            }

        }
        this.totalgame = k
        this.wingame = t
        this.wingamerate = (t / k) * 100 
        // console.log(this.totalgame)
        // console.log(this.wingame)
        // console.log(this.lanelist)
        // console.log(this.chamlist)
    }
}
</script>

<style>
.rate {
    border-right: 1px solid #607D8B
}
.infoset {
    border-right: 1px solid #607D8B
}
</style>