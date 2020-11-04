package com.web.blog.model.service.chatbot;

import com.google.api.gax.core.FixedCredentialsProvider;
import com.google.auth.oauth2.GoogleCredentials;
import com.google.auth.oauth2.ServiceAccountCredentials;
import com.google.cloud.dialogflow.v2.SessionName;
import com.google.cloud.dialogflow.v2.SessionsClient;
import com.google.cloud.dialogflow.v2.SessionsSettings;
import com.web.blog.model.dto.chatbot.Session;

import org.springframework.stereotype.Service;

import javax.servlet.http.HttpSession;

import java.io.File;
import java.io.FileInputStream;
import java.util.UUID;

@Service
public class SessionServiceImpl implements SessionService {
    private final String KEY_JSON_FILE = "C:\\ssafy\\demacia-final\\s03p31a502\\backend\\src\\main\\resources\\demacia-yhjx-973f6e2974eb.json";

    @Override
    public Session createChatSessionID() throws Exception {
        Session createdChatSession = new Session();

        // uuid 생성
        String sessionId = UUID.randomUUID().toString();
        createdChatSession.setSessionId(sessionId);

        // 1. read json by InputStream

            GoogleCredentials credentials = GoogleCredentials
                    .fromStream(new FileInputStream(KEY_JSON_FILE));
        // new FileInputStream(KEY_JSON_FILE));
        System.out.println("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee");
        String projectId = ((ServiceAccountCredentials) credentials).getProjectId();
        System.out.println(projectId);
        createdChatSession.setProjectId(projectId);

        SessionName userSession = SessionName.of(projectId, sessionId);
        System.out.println("Session Path: " + userSession.toString());
        // projects/{PROJECT_ID}/agent/sessions/{SESSION_ID}
        createdChatSession.setUserSession(userSession);

        // 2. build SessionSettings
        SessionsSettings.Builder settingsBuilder = SessionsSettings.newBuilder();
        SessionsSettings sessionsSettings = settingsBuilder
                .setCredentialsProvider(FixedCredentialsProvider.create(credentials)).build();

        // 3. create SessionsClient
        SessionsClient sessionsClient = SessionsClient.create(sessionsSettings);
        createdChatSession.setSessionsClient(sessionsClient);

        return createdChatSession;
    }
}
