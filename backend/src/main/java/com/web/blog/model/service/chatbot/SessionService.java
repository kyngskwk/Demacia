package com.web.blog.model.service.chatbot;

import com.web.blog.model.dto.chatbot.Session;

public interface SessionService {
    Session createChatSessionID() throws Exception;
}
