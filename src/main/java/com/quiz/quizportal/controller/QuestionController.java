package com.quiz.quizportal.controller;

import com.quiz.quizportal.dto.QuestionGenerationRequest;
import com.quiz.quizportal.model.Question;
import com.quiz.quizportal.service.GeminiQuestionService;
import com.quiz.quizportal.service.QuestionService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
public class QuestionController {

    @Autowired
    private QuestionService questionService;

    @Autowired
    private GeminiQuestionService geminiQuestionService;

    @GetMapping("/questions")
    public List<Question> getAllQuestions(@RequestParam(required = false) Integer testId) {
        if (testId != null) {
            return questionService.getQuestionsByTest(testId);
        }

        return questionService.getAllQuestions();
    }

    @PostMapping("/questions/add")
    public String addQuestion(@RequestBody Question question) {

        if (question.getTestId() <= 0) {
            return "invalid test";
        }

        questionService.addQuestion(question);
        return "success";
    }

    @PostMapping("/questions/add-all")
    public String addQuestions(@RequestBody List<Question> questions) {

        if (questions == null || questions.isEmpty()) {
            return "invalid";
        }

        for (Question question : questions) {
            if (question.getTestId() <= 0) {
                return "invalid test";
            }
        }

        questionService.addQuestions(questions);
        return "success";
    }

    @PostMapping("/questions/generate")
    public ResponseEntity<?> generateQuestions(@RequestBody QuestionGenerationRequest generationRequest) {

        if (generationRequest.getTopic() == null || generationRequest.getTopic().equals("") ||
                generationRequest.getQuestionCount() <= 0 ||
                generationRequest.getQuestionCount() > 20 ||
                generationRequest.getTestId() <= 0) {
            return ResponseEntity.badRequest().body("invalid");
        }

        try {
            return ResponseEntity.ok(geminiQuestionService.generateQuestions(generationRequest));
        } catch (IllegalStateException exception) {
            if ("missing api key".equals(exception.getMessage())) {
                return ResponseEntity.status(HttpStatus.SERVICE_UNAVAILABLE).body("missing api key");
            }

            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("generation failed");
        } catch (Exception exception) {
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("generation failed");
        }
    }

    @DeleteMapping("/questions/delete/{id}")
    public String deleteQuestion(@PathVariable int id) {
        questionService.deleteQuestion(id);
        return "success";
    }
}
