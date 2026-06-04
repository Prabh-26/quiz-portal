package com.quiz.quizportal.repository;

import com.quiz.quizportal.model.Subject;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

public interface SubjectRepository extends JpaRepository<Subject, Integer> {
    List<Subject> findByCourseId(int courseId);
}