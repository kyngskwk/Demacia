package com.web.blog.model.service.video;

import java.util.List;

import com.web.blog.model.dao.video.VideoPostDao;
import com.web.blog.model.dto.video.Video;
import com.web.blog.model.dto.video.VideoPostDetail;
import com.web.blog.model.dto.video.VideoPostItem;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class videoPostService {

    @Autowired
    VideoPostDao dao;

    // 게시물 등록
    public int insert(Video video) {
        return dao.insert(video);
    }

    // 통합 검색
    public List<VideoPostItem> search(int limit, int offset, String option, String orderBy) {
        return dao.search(limit, offset, option, orderBy);
    }

    // 상세 조회
    public VideoPostDetail detail(int videoPostNo) {
        return dao.detail(videoPostNo);
    }

    // 게시물 삭제
    public int delete(int videoPostNo) {
        return dao.delete(videoPostNo);
    }

    // 게시물 수정
    public int update(Video video) {
        return dao.update(video);
    }

    // 조회수
    public int viewCount(int videoPostNo, int view) {
        return dao.viewCount(videoPostNo, view);
    }
}