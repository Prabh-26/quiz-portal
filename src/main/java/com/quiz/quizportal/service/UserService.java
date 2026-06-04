package com.quiz.quizportal.service;

import com.quiz.quizportal.model.ApprovedStudent;
import com.quiz.quizportal.model.User;
import com.quiz.quizportal.repository.ApprovedStudentRepository;
import com.quiz.quizportal.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class UserService {

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private ApprovedStudentRepository approvedStudentRepository;

    public User login(String username, String password) {
        return userRepository.findByUsernameAndPassword(username, password);
    }

    public User register(String username, String password, String rollNumber) {
        User existing = userRepository.findByUsername(username);
        if (existing != null) {
            return null; // username already taken
        }

        ApprovedStudent approvedStudent = approvedStudentRepository.findByRollNumber(rollNumber);
        if (approvedStudent == null) {
            return null; // roll number not approved
        }

        User rollNumberUsed = userRepository.findByRollNumber(rollNumber);
        if (rollNumberUsed != null){
            return null; //roll number already registered
        }

        User user = new User();
        user.setUsername(username);
        user.setPassword(password);
        user.setRole("student");
        user.setRollNumber(rollNumber);
        user.setCourseId(approvedStudent.getCourseId());

        return userRepository.save(user);
    }
}