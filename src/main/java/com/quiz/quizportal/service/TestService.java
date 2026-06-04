package com.quiz.quizportal.service;

import com.quiz.quizportal.model.Test;
import com.quiz.quizportal.repository.QuestionRepository;
import com.quiz.quizportal.repository.ResultRepository;
import com.quiz.quizportal.repository.TestRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import java.util.List;

@Service
public class TestService {

    @Autowired
    private TestRepository testRepository;

    @Autowired
    private QuestionRepository questionRepository;

    @Autowired
    private ResultRepository resultRepository;

    public List<Test> getAllTests() {
        return testRepository.findAll();
    }

    public List<Test> getTestsByCourse(int courseId) {
        return testRepository.findByCourseId(courseId);
    }

    public Test getTestById(int id) {
        return testRepository.findById(id).orElse(null);
    }

    public void addTest(Test test) {
        testRepository.save(test);
    }

    @Transactional
    public boolean deleteTest(int id) {
        if (!testRepository.existsById(id)) {
            return false;
        }

        questionRepository.deleteByTestId(id);
        resultRepository.deleteByTestId(id);
        testRepository.deleteById(id);
        return true;
    }
}
