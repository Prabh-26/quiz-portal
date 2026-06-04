package com.quiz.quizportal.service;

import com.quiz.quizportal.model.Subject;
import com.quiz.quizportal.repository.SubjectRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class SubjectService {

    @Autowired
    private SubjectRepository subjectRepository;

    public List<Subject> getAllSubjects() {
        return subjectRepository.findAll();
    }

    public List<Subject> getSubjectsByCourse(int courseId) {
        return subjectRepository.findByCourseId(courseId);
    }

    public void addSubject(Subject subject) {
        subjectRepository.save(subject);
    }
}
