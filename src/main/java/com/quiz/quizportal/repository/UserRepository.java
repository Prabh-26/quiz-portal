package com.quiz.quizportal.repository;

import com.quiz.quizportal.model.User;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Integer> {
    User findByUsername(String username);
    User findByUsernameAndPassword(String username, String password);
    User findByRollNumber(String rollNumber);
}