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

// 비디오 게시판
import VideoDetail from "../video/VideoDetail.vue"
// 유저 전적검색
import UserSearch from "../page/UserSearch.vue"

// 게시판
import Board from "../page/board/boardMain"
// 게시판
import BoardWrite from "../page/board/boardWrite"

Vue.use(Router);

export default new Router({
    mode: "history",
    routes: [
        // 메인 페이지
        {
            path: "/",
            component: main,
        },
        // 게시판
        {
            path: "/board",
            name: "board",
            component: Board,
        },
        // 게시판 글쓰기
        {
            path: "/boardWrite",
            name: "boardWrite",
            component: BoardWrite,
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
        {
            path: "/videodetail",
            name: "VideoDetail",
            component: VideoDetail
        },
        {
            path: "/usersearch",
            name: "UserSearch",
            component: UserSearch,
            props: true
        }
    ],
});
