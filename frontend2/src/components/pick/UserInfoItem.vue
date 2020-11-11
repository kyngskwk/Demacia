<template>
    <v-card>
        <v-card-title>
            <v-icon class="mr-2">mdi-account-circle</v-icon>
            <span>{{ info.name }}</span>
            <span style="font-size:13px; color:grey;" class="ml-3">
                ※ 최근 10개의 경기에서 가져온 데이터 입니다.</span>
        </v-card-title>
        <v-row class="pa-3">
            <v-col class="col-6 rate mt-5">
                <v-progress-circular
                    :rotate="-90"
                    :size="100"
                    :width="15"
                    :value="wingamerate"
                    color="blue-grey">
                    {{ wingamerate }}%
                </v-progress-circular>

                <div class="mt-3 mb-3">총 {{ totalgame }}개의 게임중 {{ wingame }}게임을 이겼습니다.</div>

                <v-row class="px-3 mt-5">
                    <v-chip color="blue-grey mt-2 mr-3" style="color:white;">MAIN LANE</v-chip>
                    <li v-for="(lane, idx) in lanelist" :key="idx" style="list-style:none; width:50px; float:left;">
                        <img :src="lane" alt=""
                        style="width:50px; height:50px;">
                    </li>
                </v-row>
                <v-row class="px-3 mt-5">
                    <v-chip color="blue-grey mt-2 mr-3" style="color:white;">CHAMPION</v-chip>
                    <li v-for="(cham, idx) in chamlist" :key="idx" style="list-style:none; width:50px; float:left;" class="mr-2">
                        <img :src="cham" alt=""
                        style="width:50px; height:50px;">
                    </li>
                </v-row>
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
        for (var idx in this.lanelist) {
            this.lanelist[idx] = require(`../../assets/lane/` + this.lanelist[idx] + `.png`)
        }

        // console.log(this.chamlist)
        for (var p in this.chamlist) {
            this.chamlist[p] = require(`../../assets/tiles/` + this.chamlist[p] + `.png`)
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
.laneinfo {
    background: #607D8B;

}
</style>