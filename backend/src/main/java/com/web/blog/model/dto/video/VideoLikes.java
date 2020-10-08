package com.web.blog.model.dto.video;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

public class VideoLikes {
    private int vpostlikeNo;
    private int userNo;
    private int videopostNo;

    @Builder
    public VideoLikes(int vpostlikeNo, int userNo, int videopostNo) {
        this.vpostlikeNo = vpostlikeNo;
        this.userNo = userNo;
        this.videopostNo = videopostNo;
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
        return videopostNo;
    }

    public void setVideopostNo(int videopostNo) {
        this.videopostNo = videopostNo;
    }

    @Override
    public String toString() {
        return "VideoLikes [userNo=" + userNo + ", videopostNo=" + videopostNo + ", vpostlikeNo=" + vpostlikeNo + "]";
    }

    public VideoLikes() {
    }

}