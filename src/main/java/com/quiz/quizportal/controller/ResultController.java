package com.quiz.quizportal.controller;

import com.quiz.quizportal.model.Result;
import com.quiz.quizportal.model.Test;
import com.quiz.quizportal.model.User;
import com.quiz.quizportal.service.ResultService;
import com.quiz.quizportal.service.TestService;
import com.quiz.quizportal.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
public class ResultController {

    @Autowired
    private ResultService resultService;

    @Autowired
    private UserService userService;

    @Autowired
    private TestService testService;

    @PostMapping("/result/save")
    public String saveResult(@RequestParam String username,
                             @RequestParam String password,
                             @RequestParam int score,
                             @RequestParam int total,
                             @RequestParam int testId) {

        User user = userService.login(username, password);

        if (user == null) {
            return "invalid user";
        }

        resultService.saveResult(user, score, total, testId);

        return "success";
    }

    @GetMapping("/result/history")
    public List<Map<String, Object>> getHistory(@RequestParam String username,
                                                @RequestParam String password) {
        User user = userService.login(username, password);
        if (user == null) {
            return null;
        }

        List<Result> results = resultService.getResultsByUser(user);
        List<Map<String, Object>> history = new ArrayList<>();

        results.forEach(result -> {
            Test test = testService.getTestById(result.getTestId());
            String testTitle = test != null ? test.getTestTitle() : "Unknown Test";

            Map<String, Object> item = new HashMap<>();
            item.put("id", result.getId());
            item.put("testId", result.getTestId());
            item.put("testTitle", testTitle);
            item.put("score", result.getScore());
            item.put("total", result.getTotal());
            item.put("takenAt", result.getTakenAt());
            history.add(item);
        });

        return history;
    }
}
