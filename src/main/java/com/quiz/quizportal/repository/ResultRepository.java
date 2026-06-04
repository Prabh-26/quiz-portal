package com.quiz.quizportal.repository;

import com.quiz.quizportal.model.Result;
import com.quiz.quizportal.model.User;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

public interface ResultRepository extends JpaRepository<Result, Integer> {
    List<Result> findByUser(User user);
    void deleteByTestId(int testId);
}
