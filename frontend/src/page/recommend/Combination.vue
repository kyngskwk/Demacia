<template>
<b-container class="bv-example-row bv-example-row-flex-cols">
  <b-card>
  <b-row align-v="start">
    <b-col><h1 id="title">조합 추천</h1></b-col>
  </b-row>
<b-row align-v="stretch" class="section">
    <b-col cols="2">
        <h3>2명파티</h3>  
    </b-col>

    <b-col>
      <h5>1위</h5>
      <b-row align-v="center">
        <b-col>
        <b-img
                style="border-style:ridge; border: #fcd000 3px ridge;"
                width="100%"
                :src="first_cham.imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
        />
        <h6>{{first_cham.korname}}</h6>
        <h6>({{first_cham.chamname}})</h6>
        </b-col>
      <b-col>
        <b-img
                style="border-style:ridge; border: #fcd000 3px ridge;"
                width="100%"
                :src="comb_info[0].imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
        />
        <h6>{{comb_info[0].korname}}</h6>
        <h6>({{comb_info[0].chamname}})</h6>
      </b-col>
      </b-row>
    </b-col>

    <b-col class="article">
        <h5>2위</h5>
        <b-row align-v="center">
        <b-col>
        <b-img
                style="border-style:ridge; border: #fcd000 3px ridge;"
                width="100%"
                :src="second_cham.imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
        />
        <h6>{{second_cham.korname}}</h6>
        <h6>({{second_cham.chamname}})</h6>
        </b-col>
      <b-col>
        <b-img
                style="border-style:ridge; border: #fcd000 3px ridge;"
                width="100%"
                :src="comb_info[4].imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
        />
        <h6>{{comb_info[4].korname}}</h6>
        <h6>({{comb_info[4].chamname}})</h6>
      </b-col>
      </b-row>
    </b-col>

    <b-col>
        <h5>3위</h5>
        <b-row align-v="center">
        <b-col>
        <b-img
                style="border-style:ridge; border: #fcd000 3px ridge;"
                width="100%"
                :src="third_cham.imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
        />
        <h6>{{third_cham.korname}}</h6>
        <h6>({{third_cham.chamname}})</h6>
        </b-col>
      <b-col>
        <b-img
                style="border-style:ridge; border: #fcd000 3px ridge;"
                width="100%"
                :src="comb_info[8].imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
        />
        <h6>{{comb_info[8].korname}}</h6>
        <h6>({{comb_info[8].chamname}})</h6>
      </b-col>
      </b-row>
    </b-col>
  </b-row>

  <b-row align-v="stretch" class="section">
    <b-col cols="2">
        <h3>3명파티</h3>        
    </b-col>

    <b-col>
        <b-row align-v="center">
        <b-col>
        <b-img
                style="border-style:ridge; border: #fcd000 3px ridge;"
                width="100%"
                :src="first_cham.imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
        />
        <h6>{{first_cham.korname}}</h6>
        <h6>({{first_cham.chamname}})</h6>
        </b-col>
        </b-row>

        <b-row align-v="center">
        <b-col>
          <b-img
                  style="border-style:ridge; border: #fcd000 3px ridge;"
                  width="100%"
                  :src="comb_info[0].imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
          />
          <h6>{{comb_info[0].korname}}</h6>
          <h6>({{comb_info[0].chamname}})</h6>
        </b-col>

        <b-col>
          <b-img
                  style="border-style:ridge; border: #fcd000 3px ridge;"
                  width="100%"
                  :src="comb_info[1].imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
          />
          <h6>{{comb_info[1].korname}}</h6>
          <h6>({{comb_info[1].chamname}})</h6>
        </b-col>
        </b-row>
    </b-col>

    <b-col class="article">
        <b-row align-v="center">
        <b-col>
        <b-img
                style="border-style:ridge; border: #fcd000 3px ridge;"
                width="100%"
                :src="second_cham.imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
        />
        <h6>{{second_cham.korname}}</h6>
        <h6>({{second_cham.chamname}})</h6>
        </b-col>
        </b-row>

        <b-row align-v="center">
        <b-col>
          <b-img
                  style="border-style:ridge; border: #fcd000 3px ridge;"
                  width="100%"
                  :src="comb_info[4].imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
          />
          <h6>{{comb_info[4].korname}}</h6>
          <h6>({{comb_info[4].chamname}})</h6>
        </b-col>

        <b-col>
          <b-img
                  style="border-style:ridge; border: #fcd000 3px ridge;"
                  width="100%"
                  :src="comb_info[5].imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
          />
          <h6>{{comb_info[5].korname}}</h6>
          <h6>({{comb_info[5].chamname}})</h6>
        </b-col>
        </b-row>
    </b-col>

    <b-col>
        <b-row align-v="center">
        <b-col>
        <b-img
                style="border-style:ridge; border: #fcd000 3px ridge;"
                width="100%"
                :src="third_cham.imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
        />
        <h6>{{third_cham.korname}}</h6>
        <h6>({{third_cham.chamname}})</h6>
        </b-col>
        </b-row>

        <b-row align-v="center">
        <b-col>
          <b-img
                  style="border-style:ridge; border: #fcd000 3px ridge;"
                  width="100%"
                  :src="comb_info[8].imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
          />
          <h6>{{comb_info[8].korname}}</h6>
          <h6>({{comb_info[8].chamname}})</h6>
        </b-col>

        <b-col>
          <b-img
                  style="border-style:ridge; border: #fcd000 3px ridge;"
                  width="100%"
                  :src="comb_info[9].imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
          />
          <h6>{{comb_info[9].korname}}</h6>
          <h6>({{comb_info[9].chamname}})</h6>
        </b-col>
        </b-row>
    </b-col>

  </b-row>

<b-row align-v="stretch" class="section">
    <b-col cols="2">
        <h3>5명파티</h3>  
    </b-col>

    <b-col>
        <b-row align-v="center">
        <b-col>
        <b-img
                style="border-style:ridge; border: #fcd000 3px ridge;"
                width="100%"
                :src="first_cham.imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
        />
        <h6>{{first_cham.korname}}</h6>
        <h6>({{first_cham.chamname}})</h6>
        </b-col>
      <b-col>
        <b-img
                style="border-style:ridge; border: #fcd000 3px ridge;"
                width="100%"
                :src="comb_info[0].imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
        />
        <h6>{{comb_info[0].korname}}</h6>
        <h6>({{comb_info[0].chamname}})</h6>
      </b-col>
      </b-row>

      <b-row align-v="center">
        <b-col>
        <b-img
                style="border-style:ridge; border: #fcd000 3px ridge;"
                width="100%"
                :src="comb_info[1].imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
        />
        <h6>{{comb_info[1].korname}}</h6>
        <h6>({{comb_info[1].chamname}})</h6>
      </b-col>
      </b-row>

      <b-row align-v="center">
      <b-col>
        <b-img
                style="border-style:ridge; border: #fcd000 3px ridge;"
                width="100%"
                :src="comb_info[2].imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
        />
        <h6>{{comb_info[2].korname}}</h6>
        <h6>({{comb_info[2].chamname}})</h6>
      </b-col>
      <b-col>
        <b-img
                style="border-style:ridge; border: #fcd000 3px ridge;"
                width="100%"
                :src="comb_info[3].imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
        />
        <h6>{{comb_info[3].korname}}</h6>
        <h6>({{comb_info[3].chamname}})</h6>
      </b-col>
      </b-row>
    </b-col>

    <b-col class="article">
        <b-row align-v="center">
        <b-col>
        <b-img
                style="border-style:ridge; border: #fcd000 3px ridge;"
                width="100%"
                :src="second_cham.imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
        />
        <h6>{{second_cham.korname}}</h6>
        <h6>({{second_cham.chamname}})</h6>
        </b-col>
      <b-col>
        <b-img
                style="border-style:ridge; border: #fcd000 3px ridge;"
                width="100%"
                :src="comb_info[4].imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
        />
        <h6>{{comb_info[4].korname}}</h6>
        <h6>({{comb_info[4].chamname}})</h6>
      </b-col>
      </b-row>

      <b-row align-v="center">
        <b-col>
        <b-img
                style="border-style:ridge; border: #fcd000 3px ridge;"
                width="100%"
                :src="comb_info[5].imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
        />
        <h6>{{comb_info[5].korname}}</h6>
        <h6>({{comb_info[5].chamname}})</h6>
      </b-col>
      </b-row>

      <b-row align-v="center">
      <b-col>
        <b-img
                style="border-style:ridge; border: #fcd000 3px ridge;"
                width="100%"
                :src="comb_info[6].imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
        />
        <h6>{{comb_info[6].korname}}</h6>
        <h6>({{comb_info[6].chamname}})</h6>
      </b-col>
      <b-col>
        <b-img
                style="border-style:ridge; border: #fcd000 3px ridge;"
                width="100%"
                :src="comb_info[7].imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
        />
        <h6>{{comb_info[7].korname}}</h6>
        <h6>({{comb_info[7].chamname}})</h6>
      </b-col>
      </b-row>
    </b-col>

    <b-col>
        <b-row align-v="center">
        <b-col>
        <b-img
                style="border-style:ridge; border: #fcd000 3px ridge;"
                width="100%"
                :src="third_cham.imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
        />
        <h6>{{third_cham.korname}}</h6>
        <h6>({{third_cham.chamname}})</h6>
        </b-col>
      <b-col>
        <b-img
                style="border-style:ridge; border: #fcd000 3px ridge;"
                width="100%"
                :src="comb_info[8].imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
        />
        <h6>{{comb_info[8].korname}}</h6>
        <h6>({{comb_info[8].chamname}})</h6>
      </b-col>
      </b-row>

      <b-row align-v="center">
        <b-col>
        <b-img
                style="border-style:ridge; border: #fcd000 3px ridge;"
                width="100%"
                :src="comb_info[9].imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
        />
        <h6>{{comb_info[9].korname}}</h6>
        <h6>({{comb_info[9].chamname}})</h6>
      </b-col>
      </b-row>

      <b-row align-v="center">
      <b-col>
        <b-img
                style="border-style:ridge; border: #fcd000 3px ridge;"
                width="100%"
                :src="comb_info[10].imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
        />
        <h6>{{comb_info[10].korname}}</h6>
        <h6>({{comb_info[10].chamname}})</h6>
      </b-col>
      <b-col>
        <b-img
                style="border-style:ridge; border: #fcd000 3px ridge;"
                width="100%"
                :src="comb_info[11].imgsrc.replace('@/assets/img', '').replace('_1.', '_0.')"
        />
        <h6>{{comb_info[11].korname}}</h6>
        <h6>({{comb_info[11].chamname}})</h6>
      </b-col>
      </b-row>
    </b-col>

  </b-row>
  </b-card>
</b-container>


</template>

<style>
  @import "../../assets/css/combination.css";
</style>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      user: {},
      first_cham: {},
      second_cham: {},
      third_cham:{},
      cham_dic:{},
      comb_info:[],
      //0-3 : champion1
      //4-7 : champion2
      //8-11: champion3
    };
  },

  async created() {
    this.user = JSON.parse(sessionStorage.getItem("user"));
    console.log(this.user);

    await axios
      .get(
        process.env.VUE_APP_DAPI_URL +
         "/recommand/" + 
         this.user.userNo + 
         "/group"
         )
        .then((res) => {
          this.first_cham = res.data.First_cham[0];
          this.second_cham = res.data.Second_cham[0];
          this.third_cham = res.data.Third_cham[0];
          let temp = this.first_cham.dictionary.replace("[", "").replace("]","");
          this.cham_dic = temp.split(",");
          temp = this.second_cham.dictionary.replace("[", "").replace("]","");
          let temp2 = temp.split(",");
          temp2.forEach(e =>{
            this.cham_dic.push(e);
          });
          temp = this.third_cham.dictionary.replace("[", "").replace("]","");
          let temp3 = temp.split(",");
          temp3.forEach(e =>{
            this.cham_dic.push(e.trim());
          });
          console.log(this.cham_dic);

          this.cham_dic.forEach(e =>{
              setTimeout(() => this.callchaminfo(e),1000);
          });
          console.log(this.comb_info);
        })
        .catch((err) => {
          location.href = "/error/로그인 중 서버 오류가 발생했습니다. " + err;
        });
  },

  computed: {

  },

  methods: {
    callchaminfo(chamno){
        axios
          .get(
            process.env.VUE_APP_DAPI_URL +
            "/champions/"
            )
            .then((res) => {
              this.comb_info.push(res.data.find(o => o.id == chamno));
            })
            .catch((err) => {
              location.href = "/error/로그인 중 서버 오류가 발생했습니다. " + err;
            });
    },
  },


};
</script>

<style>

</style>
