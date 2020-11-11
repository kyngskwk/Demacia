<template>
    <v-dialog
      scrollable
      v-model="dialog"
      width="500"
    >
    <template v-slot:activator="{ on, attrs }">
    <v-btn height="40" width="40" v-on="on" v-bind="attrs">
    <v-img src="../../assets/img/banner2.png" draggable="false" class="fixed"/>
    </v-btn>
    </template>
    <v-card>
        <v-card-title class="headline">
          <v-img src="../../assets/img/question.png"/>
        </v-card-title>
        <v-card-text>
           <v-list>
              <li class="other" v-for="(item, $index) in list" :key="$index">
                <div class="self" v-if="item.input">
                      <div>
                          <div class="msg">{{item.input}}</div>
                      </div>
                      <div class="self_date">
                        {{hours}}:{{minutes}} {{meridiem}}
                    </div>
                  </div>
                <div>
                  <div class="profileImg">
                    <img src="../../assets/img/chatProfile.png" class="profile">
                    </div>
                    <div class="msg" v-html="item.text"></div>
                    <div class="btn_suggestion" v-for="(itembtn, $index) in item.suggestions" :key="$index">
                        <button class="select" style="cursor: pointer" v-on:click="select(itembtn)">{{itembtn}}</button>
                    </div>
                    <div class="btn_link" v-if="item.linkname">
                        <button class="link" style="cursor: pointer" v-on:click="linkon(item.link)">{{item.linkname}}</button>
                    </div>
                      <div class="other_date">
                        {{hours}}:{{minutes}} {{meridiem}}
                    </div>
                    </div>
                    </li>
           </v-list>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-text-field v-model="message"
                  class="speech"
                  label="메세지를 입력하세요:)"
                  required
                ></v-text-field>
                <v-icon large color="rgb(146,168,209)" v-on:click="sendinput(message)">mdi-arrow-top-right-thick</v-icon>
          <v-btn
            text
            @click="dialog = false"
          >
          <v-img src="../../assets/img/btn_close.png" class="close" />
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
</template>

<script>
import axios from "axios";
import "../../assets/css/chatbot.css";

export default {
  components: {},
  data(){
      return{
        dialog: false,
        list : [],
        check: 0,
        time: "",
        hours: "",
        minutes: "",
        meridiem: "",
        message: "",
      };
  },

created(){
    axios
              .get(process.env.VUE_APP_API_URL + "/chatbot", {
                params: {
                  input: "다른 질문하기",
                  check: this.check,
                },
              })
              .then((res) => {
                  this.list = [];
                  this.list.push(res.data);
                  this.check = 1;
                  this.time = this.chatTime();
                  this.hours = this.time.hours;
                  this.minutes = this.time.minutes;
                  this.meridiem = this.time.meridiem;
              })
              .catch((err) => {
                  console.log(err);
              });

},

methods: {
  select(itembtn){
     console.log(itembtn);
            axios
                  .get(process.env.VUE_APP_API_URL + "/chatbot", {
                    params: {
                      input: itembtn,
                      check: this.check,
                    },
                  })
                  .then((res) => {
                      this.list.push(res.data);
                  })
                  .catch((err) => {
                      console.log(err);
                  });
  },

  chatTime() {
    var date = new Date();
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var meridiem;
    if (hours <= 12) {
        meridiem = "am";
    } else {
        hours = hours - 12;
        meridiem = "pm";
    }
    return {
        hours: hours,
        minutes: minutes,
        meridiem: meridiem
    };
  },

  linkon(link){
    location.href = link;
  },

  sendinput(msg){
    axios
                  .get(process.env.VUE_APP_API_URL + "/chatbot", {
                    params: {
                      input: msg,
                      check: this.check,
                    },
                  })
                  .then((res) => {
                      this.list.push(res.data);
                      this.message = "";
                  })
                  .catch((err) => {
                      console.log(err);
                  });
  },


},
    
};
</script>