package com.web.blog.model.dao.board;

import java.util.List;

import com.web.blog.model.dto.board.Chatboard;

import org.apache.ibatis.annotations.Mapper;
import org.springframework.stereotype.Repository;

@Mapper
@Repository
public interface PostDao {

     // 게시물 등록
     public int chatboardInsert(Chatboard chatboard);

     // 게시물 검색
     public List<Chatboard> chatboardSearch(String orderby, int limit, int offset, String tabOption);

     // 게시물 상세 조회
     public PostDetail chatboardDetail(int boardNo);

     // 게시물 삭제
     public int chatboardDelete(int boardNo);

     // 게시물 수정
     public int chatboardUpdate(Chatboard chatboard);

     // 게시물 카운트
     public int chatboardVisitCount(int boardNo,int boardView);

}