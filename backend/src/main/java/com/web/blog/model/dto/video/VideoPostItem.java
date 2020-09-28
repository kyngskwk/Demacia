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
	private int videoNo;
	private int userNo;
	private int userNickname;
	private int userImage;
	private int thumbnail;
	private int isPrivate;
	private int view;
	private LocalDateTime postdate;
	private int totalLike;

	@Builder
	public VideoPostItem(int videoNo, int userNo, int userNickname, int userImage, int thumbnail, int isPrivate,
			int view, LocalDateTime postdate, int totalLike) {
		this.videoNo = videoNo;
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