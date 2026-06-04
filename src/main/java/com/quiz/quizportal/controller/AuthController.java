package com.quiz.quizportal.controller;

import com.quiz.quizportal.model.User;
import com.quiz.quizportal.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
public class AuthController {

    @Autowired
    private UserService userService;

    @PostMapping("/login")
    public String login(@RequestParam String username, @RequestParam String password) {
        User user = userService.login(username, password);
        if (user == null) {
            return "invalid";
        }
        return user.getRole(); // returns "admin" or "student"
    }

    @PostMapping("/register")
    public String register(@RequestParam String username, @RequestParam String password, @RequestParam String rollNumber) {
        User user = userService.register(username, password, rollNumber);
        if (user == null) {
            return "failed";
        }
        return "success";
    }
}