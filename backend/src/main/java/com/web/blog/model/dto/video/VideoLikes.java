package com.web.blog.model.dto.video;

import lombok.Builder;

public class VideoLikes {
    private int vpostlikeNo;
    private int userNo;
    private int videoPostNo;

    @Builder
    public VideoLikes(int vpostlikeNo, int userNo, int videoPostNo) {
        this.vpostlikeNo = vpostlikeNo;
        this.userNo = userNo;
        this.videoPostNo = videoPostNo;
    }

    public int getVpostlikeNo() {
        return vpostlikeNo;
    }

    public void setVpostlikeNo(int vpostlikeNo) {
        this.vpostlikeNo = vpostlikeNo;
    }

    public int getUserNo() {
        return userNo;
    }

    public void setUserNo(int userNo) {
        this.userNo = userNo;
    }

    public int getVideopostNo() {
        return videoPostNo;
    }

    public void setVideopostNo(int videoPostNo) {
        this.videoPostNo = videoPostNo;
    }

    @Override
    public String toString() {
        return "VideoLikes [userNo=" + userNo + ", videoPostNo=" + videoPostNo + ", vpostlikeNo=" + vpostlikeNo + "]";
    }

    public VideoLikes() {
    }

}