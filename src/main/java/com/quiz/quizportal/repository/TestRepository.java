package com.quiz.quizportal.repository;

import com.quiz.quizportal.model.Test;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

public interface TestRepository extends JpaRepository<Test, Integer> {
    List<Test> findByCourseId(int courseId);
}