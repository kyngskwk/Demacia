import Vue from "vue"

import Router from "vue-router"

// 메인 페이지
import main from "../page/Main"

// 로그인 페이지
import login from "../page/user/LoginJoin"

// 사이드 네브바
import Message from "../page/Message"

// 대기실 전적검색
import SearchPick from "../page/SearchPick.vue"

// 게시판
import Board from "../page/board/boardMain"

Vue.use(Router);

export default new Router({
    mode: "history",
    routes: [
        // 메인 페이지
        {
            path: "/",
            component: main
        },
        // 게시판
        {
            path: "/board",
            name: "board",
            component: Board,
        },
        // 로그인 페이지
        {
            path: "/login",
            name: "Login",
            component: login
        },
        // 사이드 네브바
        {
            path: "/Message",
            name: "Message",
            component: Message
        },
        {
            path: "/searchpick",
            name: "SearchPick",
            component: SearchPick
        },
    ],
});
