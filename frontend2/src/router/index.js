import Vue from "vue"
import Router from "vue-router"

// 메인 페이지
import main from "../page/Main"

// 사이드 네브바
import Message from "../page/Message.vue"

Vue.use(Router);

export default new Router({
    mode: "history",
    routes: [
        // 메인 페이지
        {
            path: "/",
            component: main
        },
        // 사이드 네브바
        {   
            path: "/Message",
            name: "Message",
            component: Message
        },
    ],
  });