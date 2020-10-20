<template>
<div>
    <aside id="sidebar" class="nano">
    <v-navigation-drawer permanent >
      <v-list>
        <v-list-item>
          <v-list-item-avatar>
              <v-icon large color="primary">mdi-email</v-icon>
          </v-list-item-avatar>
        </v-list-item>

        <v-list-item >
          <v-list-item-content>
            <v-list-item-title class="title">{{nickname}}</v-list-item-title>
            <v-list-item-subtitle>{{username}}</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <v-divider></v-divider>
      <v-list
        nav
        dense
        :min-height="630" 
      >
        <v-list-item-group v-model="item" color="primary">
          <v-list-item
            v-for="(item, i) in items"
            :key="i"
            color="primary"
            @click="change(item.text)"
          >
            <v-list-item-icon>
              <v-icon v-text="item.icon"></v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title v-text="item.text"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
        <div id="box">
            <div class="face">
                <div class="eye"></div>
                <div class="eye right"></div>
                <div class="mouth happy"></div>
            </div>
            <div class="shadow scale"></div>
        </div>
    </aside>
    <!-- 오른쪽 부분 -->
    <div id="right"> 
        <header class="header">
          <h2 class="page-title"><a class="sidebar-toggle-btn trigger-toggle-sidebar"><span class="line"></span><span class="line"></span><span class="line"></span><span class="line line-angle1"></span><span class="line line-angle2"></span></a>{{typeString}}</h2>
        </header>
        <div class="TypeMail">
          <div v-if = "typeMail == 1">
            <RecieveMessage />
          </div>
          <div v-if = "typeMail == 2">
            <TotalMessage />
          </div>
          <div v-if = "typeMail == 3">
            <StoreMessage />
          </div>          
          <div v-if = "typeMail == 4">
            <TrashMessage />
          </div>
          <div v-if = "typeMail == 5">
            <SendMessage />
          </div>        
        </div>        
    </div>
  </div>
</template>

<script>

import RecieveMessage from '../components/message/RecieveMessage.vue';
import SendMessage from '../components/message/SendMessage.vue';
import StoreMessage from '../components/message/StoreMessage.vue';
import TotalMessage from '../components/message/TotalMessage.vue';
import TrashMessage from '../components/message/TrashMessage.vue';

export default {
    components: {
      RecieveMessage,
      SendMessage,
      StoreMessage,
      TotalMessage,
      TrashMessage,

    },
    data(){
        return{
            typeString : '받은 쪽지함',
            typeMail : 1,
            checkedNo:[],
            username: '',
            nickname: '',
            item: 0,
            items: [
                { text: '받은 쪽지함', icon: 'mdi-email' },
                { text: '보낸 쪽지함', icon: 'mdi-email-open' },
                { text: '전체 쪽지함', icon: 'mdi-mailbox' },
                { text: '보관함', icon: 'mdi-folder-open' },
                { text: '휴지통', icon: 'mdi-trash-can' },
            ],
           

        }
    },
    methods: {
          change(name){
          this.checkedNo = [];
          this.typeString = name;
          this.isTable = true;
          if(name == '받은 쪽지함') this.typeMail = 1;
          else if(name == '전체 쪽지함') this.typeMail = 2;
          else if(name == '보관함') this.typeMail = 3;
          else if(name == '휴지통') this.typeMail = 4;
          else if(name == '보낸 쪽지함') this.typeMail = 5;
      },

    },
}
</script>

<style scoped> 
.button {
  border: none;
  border-radius: 2px;
  background-color: red;
}
.unread{
  color : rgb(60, 139, 217);
}
.read {
  color : black !important;
}
.read a{
  color : black !important;
}
.content{
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  width: 100px;
  height: 5px;
}
@import url('https://fonts.googleapis.com/css?family=Lato:400,700');

html {
  display: grid;
  min-height: 100%;
}

body {
  display: grid;
  overflow: hidden;
  font-family: 'Lato', sans-serif;
  text-align: center;
}

#container {
  position: relative;
  margin: auto;
  overflow: hidden;
  width: 700px;
  height: 250px;
}

button, .dot {
  cursor: pointer;
}

#box {
  position: absolute;
  width: 350px;
  height: 300px;
  left: 75%;
  top: 68px;
  perspective: 40px;
  z-index: 0;
}

.dot {
  width: 8px;
  height: 8px;
  background: #FCFCFC;
  border-radius: 50%;
  position: absolute;
  top: 4%;
  right: 6%;
}

.two {
  right: 12%;
  opacity: .5;
}

.face {
  position: absolute;
  width: 22%;
  height: 22%;
  background: #FCFCFC;
  border-radius: 50%;
  border: 1px solid #777777;
  top: 21%;
  left: 37.5%;
  z-index: 2;
  animation: bounce 1s ease-in infinite;
}

.face2 {
  position: absolute;
  width: 22%;
  height: 22%;
  background: #FCFCFC;
  border-radius: 50%;
  border: 1px solid #777777;
  top: 21%;
  left: 37.5%;
  z-index: 2;
  animation: roll 3s ease-in-out infinite;
}

.eye {
  position: absolute;
  width: 5px;
  height: 5px;
  background: #777777;
  border-radius: 50%;
  top: 40%;
  left: 20%;
}

.right {
  left: 68%;
  padding : 0;
  margin : 0;
}

.mouth {
  position:absolute;
  top: 43%;
  left: 41%;
  width: 7px;
  height: 7px;
  border-radius: 50%;
}

.happy {
  border: 2px solid;
  border-color: transparent #777777 #777777 transparent;
  transform: rotate(45deg);
}

.sad {
  top: 49%;
  border: 2px solid;
  border-color: #777777 transparent transparent #777777;
  transform: rotate(45deg);
}

.shadow {
  position: absolute;
  width: 21%;
  height: 3%;
  opacity: .5;
  background: #777777;
  left: 40%;
  top: 43%;
  border-radius: 50%;
  z-index: 1;
}

.scale {
  animation: scale 1s ease-in infinite;
}
.move {
  animation: move 3s ease-in-out infinite;
}


.message {
  position: absolute;
  width: 100%;
  text-align: center;
  height: 40%;
  top: 47%;
}

.button-box {
  position: absolute;
  background: #FCFCFC;
  width: 50%;
  height: 15%;
  border-radius: 20px;
  top: 73%;
  left: 25%;
  outline: 0;
  border: none;
  box-shadow: 2px 2px 10px rgba(#777777, .5);
  transition: all .5s ease-in-out;
}

@keyframes bounce {
  50% {
     transform: translateY(-10px);
  }
}

@keyframes scale {
  50% {
    transform: scale(0.9);
  }
}

@keyframes roll {
  0% {
    transform: rotate(0deg);
    left: 25%;
  }
  50% {
    left: 60%;
    transform: rotate(168deg);
  }
  100% {
    transform: rotate(0deg);
    left: 25%;
  }
}

@keyframes move {
  0% {
    left: 25%;
  }
  50% {
    left: 60%;
  }
  100% {
    left: 25%;
  }
}
  #sidebar{
      float : left;
      width : 20%;
      height: 100%;
      transition-duration: 0.3s;
  }
  #right{
      float : right;
      width: 80%;
  }
  #sidebar a {
    color: #abb4be;
  }
  #sidebar .logo-container {
    font-weight: 100;
    font-size: 40px;
    line-height: 40px;
    text-align: center;
    margin: 30px 0;
    cursor: pointer;
  }
  #sidebar .logo-container .logo {
    position: relative;
    top: -6px;
    font-size: 20px;
    margin-right: 15px;
    padding: 10px;
    border: 2px solid #61c7b3;
    border-radius: 100px;
    text-indent: 1px;
    color: #61c7b3;
  }
  .header {
    padding: 54.5px 0px 54px 60px;
    border-bottom: 1px solid #efefef;
    overflow: hidden;
  }
  .header .page-title {
    display: block;
    text-align: left;
  }
  .header .page-title .sidebar-toggle-btn {
    width: 0;
    margin-top: 1px;
    padding: 11px 0 0 0;
    float: left;
    position: relative;
    display: block;
    cursor: pointer;
    transition-duration: 0.3s;
    transition-delay: 0.5s;
    opacity: 0;
    margin-right: 0;
  }
  .header .page-title .sidebar-toggle-btn {
    transition-delay: 0s;
  }
  .header .page-title .sidebar-toggle-btn .line {
    height: 3px;
    display: block;
    background: #888;
    margin-bottom: 4px;
    transition-duration: 0.5s;
    transition-delay: 0.5s;
  }
  .header .page-title .sidebar-toggle-btn .line-angle1 {
    transform: rotate(-120deg);
  }
  .header .page-title .sidebar-toggle-btn .line-angle2 {
    transform: rotate(120deg);
  }
  .header .page-title .sidebar-toggle-btn .line-angle1 {
    width: 8px;
    margin: 0;
    position: absolute;
    top: 15px;
    left: -11px;
    transform: rotate(-60deg);
  }
  .header .page-title .sidebar-toggle-btn .line-angle2 {
    width: 8px;
    margin: 0;
    position: absolute;
    top: 21px;
    left: -11px;
    transform: rotate(60deg);
  }
  .header .page-title .icon {
    font-size: 15px;
    margin-left: 20px;
    position: relative;
    top: -5px;
    cursor: pointer;
  }
  
</style>