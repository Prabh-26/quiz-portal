package com.quiz.quizportal.service;

import com.quiz.quizportal.dto.QuestionGenerationRequest;
import com.quiz.quizportal.model.Question;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import tools.jackson.core.type.TypeReference;
import tools.jackson.databind.JsonNode;
import tools.jackson.databind.ObjectMapper;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.List;
import java.util.Map;

@Service
public class GeminiQuestionService {

    @Value("${gemini.api.key:}")
    private String apiKey;

    @Value("${gemini.model:gemini-2.5-flash}")
    private String model;

    private final ObjectMapper objectMapper;
    private final HttpClient httpClient;

    public GeminiQuestionService(ObjectMapper objectMapper) {
        this.objectMapper = objectMapper;
        this.httpClient = HttpClient.newHttpClient();
    }

    public List<Question> generateQuestions(QuestionGenerationRequest generationRequest) throws Exception {
        if (apiKey == null || apiKey.isBlank()) {
            throw new IllegalStateException("missing api key");
        }

        String prompt = buildPrompt(generationRequest);
        String requestBody = objectMapper.writeValueAsString(Map.of(
                "contents", List.of(Map.of(
                        "parts", List.of(Map.of("text", prompt))
                )),
                "generationConfig", Map.of(
                        "responseMimeType", "application/json"
                )
        ));

        String url = "https://generativelanguage.googleapis.com/v1beta/models/" +
                model + ":generateContent";

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("x-goog-api-key", apiKey)
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(requestBody))
                .build();

        HttpResponse<String> response =
                httpClient.send(request, HttpResponse.BodyHandlers.ofString());

        if (response.statusCode() < 200 || response.statusCode() >= 300) {
            throw new IllegalStateException("gemini api error");
        }

        JsonNode root = objectMapper.readTree(response.body());
        String generatedText = root.path("candidates")
                .path(0)
                .path("content")
                .path("parts")
                .path(0)
                .path("text")
                .asText();

        List<Question> questions = objectMapper.readValue(
                extractJsonArray(generatedText),
                new TypeReference<List<Question>>() {}
        );

        questions.forEach(question -> {
            question.setId(0);
            question.setTestId(generationRequest.getTestId());
            question.setCorrectOption(question.getCorrectOption().toUpperCase());
        });

        return questions;
    }

    private String buildPrompt(QuestionGenerationRequest generationRequest) {
        return """
                Generate %d multiple choice questions for this quiz topic: %s.
                Return only a valid JSON array.
                Each item must have exactly these fields:
                questionText, optionA, optionB, optionC, optionD, correctOption.
                correctOption must be only one letter: A, B, C, or D.
                Do not include markdown, explanation, numbering, or extra text.
                """.formatted(generationRequest.getQuestionCount(), generationRequest.getTopic());
    }

    private String extractJsonArray(String text) {
        int start = text.indexOf("[");
        int end = text.lastIndexOf("]");

        if (start == -1 || end == -1 || end <= start) {
            throw new IllegalStateException("invalid ai response");
        }

        return text.substring(start, end + 1);
    }
}
