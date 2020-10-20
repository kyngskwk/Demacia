import Vue from "vue"
import Router from "vue-router"

// 메인 페이지
import main from "../page/Main"

Vue.use(Router);

export default new Router({
    mode: "history",
    routes: [
        // 메인 페이지
        {
            path: "/",
            component: main
        },
    ],
  });
