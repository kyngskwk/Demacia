<template>
  <div class="container text-center mb-10">
    <h1 class="mb-5">유저 전적기록 검색</h1>

    <v-textarea 
        label="유저 전적기록 검색하기"
        placeholder="검색하고 싶은 유저의 소환사를 입력해주세요!
ex) Hide on Bush"
        outlined
        v-model="nickname"
    ></v-textarea>
    <p v-if="infoerror">{{ userinfo }}</p>
    <v-btn class="searchbtn blue-grey" @click="gosearch">검색하기</v-btn>
    <!-- 결과 안내창 -->
    <div class="loading-container" v-if="isloading">
      <div class="loading"></div>
      <div id="loading-text">loading</div>
    </div>
    <div class="mt-5" v-if="isresult">
        <v-row>
            <UserSearchList v-for="(info, i) in result" :key="i" :info="info"/>
        </v-row>
    </div>
    <div>

    </div>
  </div>
</template>

<script>
import axios from 'axios'
import UserSearchList from '../components/pick/UserSearchList.vue'

export default {
    name: 'UserSearch',
    components: {
        UserSearchList,
    },
    data() {
        return {
            nickname: '',
            isloading: false,
            infoerror: false,
            isresult: false,
            result: '',
        }
    },
    methods: {
        gosearch() {
            if (this.nickname != '') {
                this.isloading = true
                axios.post(`http://127.0.0.1:8000/django/api/usersearch/`, {
                // axios.post(`http://k3a502.p.ssafy.io/django/api/usersearch/`, {
                    nickname: this.nickname
                }).then(response => {
                    this.result = response.data
                    // console.log(this.result)
                    if (typeof this.result == 'string') {
                        this.loading = false
                        this.infoerror = true
                        this.isresult = false
                    } else {
                        this.isloading = false
                        this.infoerror = false
                        this.isresult = true
                    }
                }).catch(function (error) {
                    console.log(error.response.data)
                    this.isloading = false
                    this.infoerror = true
                    this.isresult = false
                })
            } 
        }
    }

}
</script>

<style scoped>
.searchbtn {
    display: inline-block;
    width: 100%;
    color: white;
}

@keyframes rotate-loading {
    0%  {transform: rotate(0deg);-ms-transform: rotate(0deg); -webkit-transform: rotate(0deg); -o-transform: rotate(0deg); -moz-transform: rotate(0deg);}
    100% {transform: rotate(360deg);-ms-transform: rotate(360deg); -webkit-transform: rotate(360deg); -o-transform: rotate(360deg); -moz-transform: rotate(360deg);}
}

@-moz-keyframes rotate-loading {
    0%  {transform: rotate(0deg);-ms-transform: rotate(0deg); -webkit-transform: rotate(0deg); -o-transform: rotate(0deg); -moz-transform: rotate(0deg);}
    100% {transform: rotate(360deg);-ms-transform: rotate(360deg); -webkit-transform: rotate(360deg); -o-transform: rotate(360deg); -moz-transform: rotate(360deg);}
}

@-webkit-keyframes rotate-loading {
    0%  {transform: rotate(0deg);-ms-transform: rotate(0deg); -webkit-transform: rotate(0deg); -o-transform: rotate(0deg); -moz-transform: rotate(0deg);}
    100% {transform: rotate(360deg);-ms-transform: rotate(360deg); -webkit-transform: rotate(360deg); -o-transform: rotate(360deg); -moz-transform: rotate(360deg);}
}

@-o-keyframes rotate-loading {
    0%  {transform: rotate(0deg);-ms-transform: rotate(0deg); -webkit-transform: rotate(0deg); -o-transform: rotate(0deg); -moz-transform: rotate(0deg);}
    100% {transform: rotate(360deg);-ms-transform: rotate(360deg); -webkit-transform: rotate(360deg); -o-transform: rotate(360deg); -moz-transform: rotate(360deg);}
}

@keyframes rotate-loading {
    0%  {transform: rotate(0deg);-ms-transform: rotate(0deg); -webkit-transform: rotate(0deg); -o-transform: rotate(0deg); -moz-transform: rotate(0deg);}
    100% {transform: rotate(360deg);-ms-transform: rotate(360deg); -webkit-transform: rotate(360deg); -o-transform: rotate(360deg); -moz-transform: rotate(360deg);}
}

@-moz-keyframes rotate-loading {
    0%  {transform: rotate(0deg);-ms-transform: rotate(0deg); -webkit-transform: rotate(0deg); -o-transform: rotate(0deg); -moz-transform: rotate(0deg);}
    100% {transform: rotate(360deg);-ms-transform: rotate(360deg); -webkit-transform: rotate(360deg); -o-transform: rotate(360deg); -moz-transform: rotate(360deg);}
}

@-webkit-keyframes rotate-loading {
    0%  {transform: rotate(0deg);-ms-transform: rotate(0deg); -webkit-transform: rotate(0deg); -o-transform: rotate(0deg); -moz-transform: rotate(0deg);}
    100% {transform: rotate(360deg);-ms-transform: rotate(360deg); -webkit-transform: rotate(360deg); -o-transform: rotate(360deg); -moz-transform: rotate(360deg);}
}

@-o-keyframes rotate-loading {
    0%  {transform: rotate(0deg);-ms-transform: rotate(0deg); -webkit-transform: rotate(0deg); -o-transform: rotate(0deg); -moz-transform: rotate(0deg);}
    100% {transform: rotate(360deg);-ms-transform: rotate(360deg); -webkit-transform: rotate(360deg); -o-transform: rotate(360deg); -moz-transform: rotate(360deg);}
}

@keyframes loading-text-opacity {
    0%  {opacity: 0}
    20% {opacity: 0}
    50% {opacity: 1}
    100%{opacity: 0}
}

@-moz-keyframes loading-text-opacity {
    0%  {opacity: 0}
    20% {opacity: 0}
    50% {opacity: 1}
    100%{opacity: 0}
}

@-webkit-keyframes loading-text-opacity {
    0%  {opacity: 0}
    20% {opacity: 0}
    50% {opacity: 1}
    100%{opacity: 0}
}

@-o-keyframes loading-text-opacity {
    0%  {opacity: 0}
    20% {opacity: 0}
    50% {opacity: 1}
    100%{opacity: 0}
}
.loading-container,
.loading {
    height: 100px;
    position: relative;
    width: 100px;
    border-radius: 100%;
}


.loading-container { margin:140px auto }

.loading {
    border: 2px solid transparent;
    border-color: transparent #607D8B transparent #607D8B;
    -moz-animation: rotate-loading 1.5s linear 0s infinite normal;
    -moz-transform-origin: 50% 50%;
    -o-animation: rotate-loading 1.5s linear 0s infinite normal;
    -o-transform-origin: 50% 50%;
    -webkit-animation: rotate-loading 1.5s linear 0s infinite normal;
    -webkit-transform-origin: 50% 50%;
    animation: rotate-loading 1.5s linear 0s infinite normal;
    transform-origin: 50% 50%;
}

.loading-container:hover .loading {
    border-color: transparent #E45635 transparent #E45635;
}
.loading-container:hover .loading,
.loading-container .loading {
    -webkit-transition: all 0.5s ease-in-out;
    -moz-transition: all 0.5s ease-in-out;
    -ms-transition: all 0.5s ease-in-out;
    -o-transition: all 0.5s ease-in-out;
    transition: all 0.5s ease-in-out;
}

#loading-text {
    -moz-animation: loading-text-opacity 2s linear 0s infinite normal;
    -o-animation: loading-text-opacity 2s linear 0s infinite normal;
    -webkit-animation: loading-text-opacity 2s linear 0s infinite normal;
    animation: loading-text-opacity 2s linear 0s infinite normal;
    color: #607D8B;
    font-family: "Helvetica Neue, "Helvetica", ""arial";
    font-size: 10px;
    font-weight: bold;
    margin-top: 45px;
    opacity: 0;
    position: absolute;
    text-align: center;
    text-transform: uppercase;
    top: 0;
    width: 100px;
}
</style>