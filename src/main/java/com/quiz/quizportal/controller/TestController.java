package com.quiz.quizportal.controller;

import com.quiz.quizportal.model.Test;
import com.quiz.quizportal.model.User;
import com.quiz.quizportal.service.TestService;
import com.quiz.quizportal.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
public class TestController {

    @Autowired
    private TestService testService;

    @Autowired
    private UserService userService;

    @GetMapping("/tests")
    public List<Test> getAllTests() {
        return testService.getAllTests();
    }

    @GetMapping("/tests/my")
    public List<Test> getMyTests(@RequestParam String username,
                                 @RequestParam String password) {
        User user = userService.login(username, password);

        if (user == null) {
            return null;
        }

        return testService.getTestsByCourse(user.getCourseId());
    }

    @PostMapping("/tests/add")
    public String addTest(@RequestBody Test test) {

        if (test.getTestTitle() == null || test.getTestTitle().equals("") ||
                test.getSubjectId() <= 0 ||
                test.getCourseId() <= 0) {
            return "invalid";
        }

        testService.addTest(test);
        return "success";
    }

    @DeleteMapping("/tests/delete/{id}")
    public String deleteTest(@PathVariable int id) {
        boolean deleted = testService.deleteTest(id);

        if (!deleted) {
            return "not found";
        }

        return "success";
    }
}
