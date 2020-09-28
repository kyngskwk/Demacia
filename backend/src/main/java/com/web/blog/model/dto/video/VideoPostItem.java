package com.web.blog.model.dto.video;

import java.time.LocalDateTime;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

@Getter
@Setter
@ToString
@NoArgsConstructor
public class VideoPostItem {
	private int videoPostNo;
	private int userNo;
	private String userNickname;
	private String userImage;
	private String thumbnail;
	private int isPrivate;
	private int view;
	private LocalDateTime postdate;
	private int totalLike;

	@Builder
	public VideoPostItem(int videoPostNo, int userNo, String userNickname, String userImage, String thumbnail,
			int isPrivate, int view, LocalDateTime postdate, int totalLike) {
		this.videoPostNo = videoPostNo;
		this.userNo = userNo;
		this.userNickname = userNickname;
		this.userImage = userImage;
		this.thumbnail = thumbnail;
		this.isPrivate = isPrivate;
		this.view = view;
		this.postdate = postdate;
		this.totalLike = totalLike;
	}
}