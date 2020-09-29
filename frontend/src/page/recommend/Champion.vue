<template>
<b-container class="bv-example-row bv-example-row-flex-cols">
  <b-card class="m-2">
  <b-row align-v="start">
    <b-col><h1 id="title">챔피언 추천</h1></b-col>
  </b-row>
<b-row align-v="stretch" class="article">
    <b-col cols="4">
        <h3 class="rank">1위</h3>
        <img
                thumbnail
                width="100%"
                :src="cham_no1.imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
        />   
    </b-col>
    <b-col cols="8" class="sub">
        <b-row align-v="center">
            <b-col><h3>{{user.userNickname}}님이 가장 잘하는 챔피언은 {{cham_no1.korname}}</h3></b-col>
        </b-row>
        <b-row align-v="center">
            <b-col><h3>{{cham_no1.korname}}의 승률은 {{cham_no1_rate}}%</h3></b-col>
        </b-row>
        <b-row align-v="center">
            <b-col>비슷한 성향을 가진 챔피언들 : </b-col>
        </b-row>
        <b-row align-v="center">
          <b-col>
          <b-img
                thumbnail
                width="100%"
                :src="sim_info[0].imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
          /> 
        </b-col>
        <b-col>
          <b-img
                thumbnail
                width="100%"
                :src="sim_info[1].imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
          /> 
        </b-col>
        <b-col>
          <b-img
                thumbnail
                width="100%"
                :src="sim_info[2].imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
          /> 
        </b-col>
        </b-row>
          <b-row align-v="center">
            <b-col><h5>{{sim_info[0].korname}}</h5></b-col>
            <b-col><h5>{{sim_info[1].korname}}</h5></b-col>
            <b-col><h5>{{sim_info[2].korname}}</h5></b-col>
        </b-row>
    </b-col>
  </b-row>

  <b-row align-v="stretch" class="article">
    <b-col cols="4">
        <h3 class="rank">2위</h3>
        <img
                thumbnail
                width="100%"
                :src="cham_no2.imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
        />   
    </b-col>
    <b-col cols="8" class="sub">
        <b-row align-v="center">
            <b-col><h3>{{user.userNickname}}님이 가장 잘하는 챔피언은 {{cham_no2.korname}}</h3></b-col>
        </b-row>
        <b-row align-v="center">
            <b-col><h3>{{cham_no2.korname}}의 승률은 {{cham_no2_rate}}%</h3></b-col>
        </b-row>
        <b-row align-v="center">
            <b-col>비슷한 성향을 가진 챔피언들 : </b-col>
        </b-row>
        <b-row align-v="center">
          <b-col>
          <b-img
                thumbnail
                width="100%"
                :src="sim_info[3].imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
          /> 
        </b-col>
        <b-col>
          <b-img
                thumbnail
                width="100%"
                :src="sim_info[4].imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
          /> 
        </b-col>
        <b-col>
          <b-img
                thumbnail
                width="100%"
                :src="sim_info[5].imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
          /> 
        </b-col>
        </b-row>
          <b-row align-v="center">
            <b-col><h5>{{sim_info[3].korname}}</h5></b-col>
            <b-col><h5>{{sim_info[4].korname}}</h5></b-col>
            <b-col><h5>{{sim_info[5].korname}}</h5></b-col>
        </b-row>
    </b-col>
  </b-row>

  <b-row align-v="stretch" class="article">
    <b-col cols="4">
        <h3 class="rank">3위</h3>
        <img
                thumbnail
                width="100%"
                :src="cham_no3.imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
        />   
    </b-col>
    <b-col cols="8" class="sub">
        <b-row align-v="center">
            <b-col><h3>{{user.userNickname}}님이 가장 잘하는 챔피언은 {{cham_no3.korname}}</h3></b-col>
        </b-row>
        <b-row align-v="center">
            <b-col><h3>{{cham_no3.korname}}의 승률은 {{cham_no3_rate}}%</h3></b-col>
        </b-row>
        <b-row align-v="center">
            <b-col>비슷한 성향을 가진 챔피언들 : </b-col>
        </b-row>
        <b-row align-v="center">
          <b-col>
          <b-img
                thumbnail
                width="100%"
                :src="sim_info[6].imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
          /> 
        </b-col>
        <b-col>
          <b-img
                thumbnail
                width="100%"
                :src="sim_info[7].imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
          /> 
        </b-col>
        <b-col>
          <b-img
                thumbnail
                width="100%"
                :src="sim_info[8].imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
          /> 
        </b-col>
        </b-row>
          <b-row align-v="center">
            <b-col><h5>{{sim_info[6].korname}}</h5></b-col>
            <b-col><h5>{{sim_info[7].korname}}</h5></b-col>
            <b-col><h5>{{sim_info[8].korname}}</h5></b-col>
        </b-row>
    </b-col>
  </b-row>


  </b-card>
</b-container>


</template>
<style>
  @import "../../assets/css/champion.css";
</style>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      user: {},
      recommand_cham_info: {},
      similar_cham_recommand: {},
      champions: {},
      cham_no1_rate:"",
      cham_no2_rate:"",
      cham_no3_rate:"",
      cham_no1_id:"",
      cham_no2_id:"",
      cham_no3_id:"",
      cham_no1: {},
      cham_no2: {},
      cham_no3: {},
      sim_no1: {},
      sim_no2: {},
      sim_no3: {},
      sim_info: [],
    };
  },

  created() {
    this.user = JSON.parse(sessionStorage.getItem("user"));
    console.log(this.user);
    axios
      .get(
        process.env.VUE_APP_DAPI_URL +
         "/recommand/" + 
         this.user.userNo + 
         "/champion"
         )
        .then((res) => {
          this.recommand_cham_info = res.data.recommand_cham_info;
          this.similar_cham_recommand = res.data.similar_cham_recommand[0];
          let temp = JSON.parse(this.recommand_cham_info[0].recommand_champion.replaceAll("'", '"'));
          this.champions = Object.entries(temp).sort((a, b) => b[1].localeCompare(a[1]));
          this.cham_no1_id = this.champions[0][0];
          this.cham_no2_id = this.champions[1][0];
          this.cham_no3_id = this.champions[2][0];
          this.cham_no1_rate = this.champions[0][1]*100;
          this.cham_no2_rate = this.champions[1][1]*100;
          this.cham_no3_rate = this.champions[2][1]*100;
          this.sim_no1 = this.similar_cham_recommand[this.cham_no1_id];
          this.sim_no2 = this.similar_cham_recommand[this.cham_no2_id];
          this.sim_no3 = this.similar_cham_recommand[this.cham_no3_id];
          this.callsim(this.sim_no1);
          this.callsim(this.sim_no2);
          this.callsim(this.sim_no3);
          this.callchampion();
        })
        .catch((err) => {
          location.href = "/error/로그인 중 서버 오류가 발생했습니다. " + err;
        });
  },

  computed: {

  },

  methods: {
    callchampion(){
      axios
      .get(
        process.env.VUE_APP_DAPI_URL +
         "/champions/"
         )
        .then((res) => {
          this.cham_no1 = res.data.find(o => o.id == this.cham_no1_id);
          this.cham_no2 = res.data.find(o => o.id == this.cham_no2_id);
          this.cham_no3 = res.data.find(o => o.id == this.cham_no3_id);
        })
        .catch((err) => {
          location.href = "/error/로그인 중 서버 오류가 발생했습니다. " + err;
        });
    },

    callsim(sim){
      sim.forEach(element => {
        axios
          .get(
            process.env.VUE_APP_DAPI_URL +
            "/champions/"
            )
            .then((res) => {
              this.sim_info.push(res.data.find(o => o.id == element));
            })
            .catch((err) => {
              location.href = "/error/로그인 중 서버 오류가 발생했습니다. " + err;
            });
          });
    },

  }
};
</script>

<style>

</style>
