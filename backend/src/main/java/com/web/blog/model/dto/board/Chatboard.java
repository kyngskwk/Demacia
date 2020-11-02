package com.web.blog.model.dto.board;

import lombok.Data;

@Data
@Builder
public class Chatboard {
	
	private int boardNo;
	private String boardTitle;
	private String boardContent;
	private int boardView;
	private Timestamp boardDate;
    private int userNo;
    private int category;
	
}