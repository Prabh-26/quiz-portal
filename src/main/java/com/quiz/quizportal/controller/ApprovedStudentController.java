package com.quiz.quizportal.controller;

import com.quiz.quizportal.model.ApprovedStudent;
import com.quiz.quizportal.service.ApprovedStudentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
public class ApprovedStudentController {

    @Autowired
    private ApprovedStudentService approvedStudentService;

    @GetMapping("/approved-students")
    public List<ApprovedStudent> getAllApprovedStudents() {
        return approvedStudentService.getAllApprovedStudents();
    }

    @PostMapping("/approved-students/add")
    public String addApprovedStudent(@RequestBody ApprovedStudent approvedStudent) {

        if (approvedStudent.getRollNumber() == null || approvedStudent.getRollNumber().equals("") ||
                approvedStudent.getStudentName() == null || approvedStudent.getStudentName().equals("") ||
                approvedStudent.getCourseId() <= 0) {
            return "invalid";
        }

        boolean added = approvedStudentService.addApprovedStudent(approvedStudent);

        if (!added) {
            return "duplicate";
        }

        return "success";
    }

    @DeleteMapping("/approved-students/delete/{id}")
    public String deleteApprovedStudent(@PathVariable int id) {
        boolean deleted = approvedStudentService.deleteApprovedStudent(id);

        if (!deleted) {
            return "not found";
        }

        return "success";
    }
}
