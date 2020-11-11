package com.web.blog.model.dto.chatbot;

import com.google.cloud.dialogflow.v2.SessionName;
import com.google.cloud.dialogflow.v2.SessionsClient;

public class Session {
    private String sessionId;
    private String projectId;
    private SessionName userSession;
    private SessionsClient sessionsClient;

    public String getSessionId() {
        return sessionId;
    }
    public void setSessionId(String sessionId) {
        this.sessionId = sessionId;
    }

    public String getProjectId() {
        return projectId;
    }
    public void setProjectId(String projectId) {
        this.projectId = projectId;
    }

    public SessionName getUserSession() {
        return userSession;
    }
    public void setUserSession(SessionName userSession) {
        this.userSession = userSession;
    }

    public SessionsClient getSessionsClient() {
        return sessionsClient;
    }
    public void setSessionsClient(SessionsClient sessionsClient) {
        this.sessionsClient = sessionsClient;
    }
}
