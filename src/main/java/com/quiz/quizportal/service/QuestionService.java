package com.quiz.quizportal.service;

import com.quiz.quizportal.model.Question;
import com.quiz.quizportal.repository.QuestionRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class QuestionService {

    @Autowired
    private QuestionRepository questionRepository;

    public List<Question> getAllQuestions() {
        return questionRepository.findAll();
    }

    public List<Question> getQuestionsByTest(int testId) {
        return questionRepository.findByTestId(testId);
    }

    public void addQuestion(Question question) {
        questionRepository.save(question);
    }

    public void addQuestions(List<Question> questions) {
        questionRepository.saveAll(questions);
    }

    public void deleteQuestion(int id) {
        questionRepository.deleteById(id);
    }
}
