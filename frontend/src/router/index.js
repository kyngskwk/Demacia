import Vue from "vue";
import Router from "vue-router";

import constants from "../lib/constants";

// 메인 페이지
import main from "../page/Main"

// 포스트
import List from "../page/post/List.vue";
import Write from "../page/post/Write.vue";
import Detail from "../page/post/Detail.vue";
import Edit from "../page/post/Edit.vue";
import Result from "../page/post/Result.vue";

//에러
import PNF from "../page/error/PageNotFound.vue";
import Err from "../page/error/Error.vue";

//유저
import Login from "../page/user/Login.vue";
import Join from "../page/user/Join.vue";
import Mypage from "../page/user/Mypage.vue";
import Myprofile from "../page/user/Myprofile.vue";

// 영상분석
import videoList from "../page/video/List.vue";
import videoWrite from "../page/video/Write.vue";
import videoDetail from "../page/video/Detail.vue";
import videoEdit from "../page/video/Edit.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    // 메인 페이지
    {
      path: "/",
      component: main
    },
    // 포스트
    {
      path: "/list",
      name: constants.URL_TYPE.POST.MAIN,
      component: List,
    },
    {
      path: "/write",
      name: constants.URL_TYPE.POST.WRITE,
      component: Write,
    },
    {
      path: "/detail/:postNo",
      name: constants.URL_TYPE.POST.DETAIL,
      component: Detail,
    },
    {
      path: "/edit/:postNo",
      name: constants.URL_TYPE.POST.EDIT,
      component: Edit,
    },
    {
      path: "/result/:postNo",
      name: constants.URL_TYPE.POST.RESULT,
      component: Result,
    },
    // 영상분석
    {
      path: "/vlist",
      name: constants.URL_TYPE.VIDEO.MAIN,
      component: videoList,
    },
    {
      path: "/vwrite",
      name: constants.URL_TYPE.VIDEO.WRITE,
      component: videoWrite,
    },
    {
      path: "/vdetail/:videoNo",
      name: constants.URL_TYPE.VIDEO.DETAIL,
      component: videoDetail,
    },
    {
      path: "/vedit/:videoNo",
      name: constants.URL_TYPE.VIDEO.EDIT,
      component: videoEdit,
    },
    // 유저
    {
      path: "/login",
      name: constants.URL_TYPE.USER.LOGIN,
      component: Login,
    },
    {
      path: "/join",
      name: constants.URL_TYPE.USER.JOIN,
      component: Join,
    },
    {
      path: "/mypage",
      name: constants.URL_TYPE.USER.MYPAGE,
      component: Mypage,
    },
    {
      path: "/myprofile",
      name: constants.URL_TYPE.USER.MYPROFILE,
      component: Myprofile,
    },
    // Error
    {
      path: "/error/:msg",
      name: constants.URL_TYPE.ERROR.ERROR,
      component: Err,
    },
    // 404
    {
      path: "*",
      name: constants.URL_TYPE.ERROR.PAGE_NOT_FOUND,
      component: PNF,
    },
  ],
});
