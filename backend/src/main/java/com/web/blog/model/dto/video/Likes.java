package com.web.blog.model.dto.video;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

@Getter
@Setter
@ToString
@NoArgsConstructor
public class Likes {
    private int vpostlikeNo;
    private int userNo;
    private int videopostNo;

    @Builder
    public Likes(int vpostlikeNo, int userNo, int videopostNo) {
        this.vpostlikeNo = vpostlikeNo;
        this.userNo = userNo;
        this.videopostNo = videopostNo;
    }
}