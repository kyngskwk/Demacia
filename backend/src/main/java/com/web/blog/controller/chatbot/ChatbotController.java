package com.web.blog.controller.chatbot;

import com.google.api.gax.rpc.ApiException;
import com.google.cloud.dialogflow.v2.DetectIntentResponse;
import com.google.cloud.dialogflow.v2.QueryInput;
import com.google.cloud.dialogflow.v2.QueryResult;
import com.google.cloud.dialogflow.v2.SessionName;
import com.google.cloud.dialogflow.v2.SessionsClient;
import com.google.cloud.dialogflow.v2.TextInput;
import com.google.common.collect.Maps;
import java.io.IOException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;

import javax.servlet.http.HttpSession;

import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiResponse;
import io.swagger.annotations.ApiResponses;

import com.web.blog.model.dto.chatbot.Session;
import com.web.blog.model.service.chatbot.SessionService;
import com.web.blog.util.BasicResponse;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@ApiResponses(value = { @ApiResponse(code = 401, message = "Unauthorized", response = BasicResponse.class),
        @ApiResponse(code = 403, message = "Forbidden", response = BasicResponse.class),
        @ApiResponse(code = 404, message = "Not Found", response = BasicResponse.class),
        @ApiResponse(code = 500, message = "Failure", response = BasicResponse.class) })

@CrossOrigin(origins = { "*" })
@RestController
public class ChatbotController {

  @Autowired
  private SessionService sessionService;

  @GetMapping("/chatbot")
  public Object chatbot(String input) {
    System.out.println("User input : " + input);
    ResponseEntity response = null;
    final BasicResponse result = new BasicResponse();

    try {
            Session createdChatSession = sessionService.createChatSessionID();

            SessionsClient sessionsClient = createdChatSession.getSessionsClient();
            SessionName userSession = createdChatSession.getUserSession();

            TextInput.Builder textInput = TextInput.newBuilder().setText(input).setLanguageCode("ko");

            QueryInput queryInput = QueryInput.newBuilder().setText(textInput).build();

            DetectIntentResponse res = sessionsClient.detectIntent(userSession, queryInput);

            QueryResult queryResult = res.getQueryResult();

            HashMap<String, Object> resultMap = new HashMap();
            resultMap.put("intent", queryResult.getIntent().getDisplayName());
            resultMap.put("output", queryResult.getFulfillmentText());
            ResponseEntity<HashMap<String, Object>> responseEntity = new ResponseEntity<>(resultMap, HttpStatus.OK);

            System.out.println("====================");
            System.out.println("Session Path: " + userSession.toString());
            System.out.format("Query Text: '%s'\n", queryResult.getQueryText());
            System.out.format("Detected Intent: %s (confidence: %f)\n",
                    queryResult.getIntent().getDisplayName(), queryResult.getIntentDetectionConfidence());
            System.out.format("Fulfillment: '%s'\n", queryResult.getFulfillmentMessagesList());
            System.out.println(responseEntity);
            System.out.println(queryResult.getIntent().getDisplayName());

            return responseEntity;

    } catch (Exception e) {
        result.status = false;
        result.data = "calldialogflow Fail";
        System.out.println("calldialogflow Fail");

        response = new ResponseEntity<>(null, HttpStatus.NOT_FOUND);
        return response;
    }
    
  }
  
}