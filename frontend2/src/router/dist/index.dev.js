"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports["default"] = void 0;

var _vue = _interopRequireDefault(require("vue"));

var _vueRouter = _interopRequireDefault(require("vue-router"));

var _Main = _interopRequireDefault(require("../page/Main"));

var _LoginJoin = _interopRequireDefault(require("../page/user/LoginJoin"));

var _Message = _interopRequireDefault(require("../page/Message"));

var _SearchPick = _interopRequireDefault(require("../page/SearchPick.vue"));

var _VideoDetail = _interopRequireDefault(require("../video/VideoDetail.vue"));

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { "default": obj }; }

// 메인 페이지
// 로그인 페이지
// 사이드 네브바
// 대기실 전적검색
// 비디오 게시판
_vue["default"].use(_vueRouter["default"]);

var _default = new _vueRouter["default"]({
  mode: "history",
  routes: [// 메인 페이지
  {
    path: "/",
    component: _Main["default"]
  }, // 로그인 페이지
  {
    path: "/login",
    name: "Login",
    component: _LoginJoin["default"]
  }, // 사이드 네브바
  {
    path: "/Message",
    name: "Message",
    component: _Message["default"]
  }, {
    path: "/searchpick",
    name: "SearchPick",
    component: _SearchPick["default"]
  }, {
    path: "/videodetail",
    name: "VideoDetail",
    component: _VideoDetail["default"]
  }]
});

exports["default"] = _default;