package com.quiz.quizportal.repository;

import com.quiz.quizportal.model.ApprovedStudent;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ApprovedStudentRepository extends JpaRepository<ApprovedStudent, Integer> {
    ApprovedStudent findByRollNumber(String rollNumber);
}