package com.quiz.quizportal.service;

import com.quiz.quizportal.model.Result;
import com.quiz.quizportal.model.User;
import com.quiz.quizportal.repository.ResultRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.time.LocalDateTime;
import java.util.List;

@Service
public class ResultService {

    @Autowired
    private ResultRepository resultRepository;

    public void saveResult(User user, int score, int total, int testId) {
        Result result = new Result();
        result.setUser(user);
        result.setScore(score);
        result.setTotal(total);
        result.setTestId(testId);
        result.setTakenAt(LocalDateTime.now());
        resultRepository.save(result);
    }

    public List<Result> getResultsByUser(User user) {
        return resultRepository.findByUser(user);
    }
}