package com.quiz.quizportal.repository;

import com.quiz.quizportal.model.Question;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

public interface QuestionRepository extends JpaRepository<Question, Integer> {
    List<Question> findAll();
    List<Question> findByTestId(int testId);
    void deleteByTestId(int testId);
}
