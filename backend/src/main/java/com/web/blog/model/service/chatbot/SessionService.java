package com.web.blog.model.service.chatbot;

import javax.servlet.http.HttpSession;

import com.web.blog.model.dto.chatbot.Session;

public interface SessionService {
    void createChatSessionID(HttpSession session) throws Exception;
}
