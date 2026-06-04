package com.quiz.quizportal.controller;

import com.quiz.quizportal.model.Subject;
import com.quiz.quizportal.model.User;
import com.quiz.quizportal.service.SubjectService;
import com.quiz.quizportal.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
public class SubjectController {

    @Autowired
    private SubjectService subjectService;

    @Autowired
    private UserService userService;

    @GetMapping("/subjects")
    public List<Subject> getAllSubjects() {
        return subjectService.getAllSubjects();
    }

    @GetMapping("/subjects/my")
    public List<Subject> getMySubjects(@RequestParam String username,
                                       @RequestParam String password) {
        User user = userService.login(username, password);

        if (user == null) {
            return null;
        }

        return subjectService.getSubjectsByCourse(user.getCourseId());
    }

    @PostMapping("/subjects/add")
    public String addSubject(@RequestBody Subject subject) {

        if (subject.getSubjectName() == null || subject.getSubjectName().equals("") ||
                subject.getCourseId() <= 0) {
            return "invalid";
        }

        subjectService.addSubject(subject);
        return "success";
    }
}
