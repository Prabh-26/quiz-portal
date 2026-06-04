package com.quiz.quizportal.service;

import com.quiz.quizportal.model.ApprovedStudent;
import com.quiz.quizportal.repository.ApprovedStudentRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class ApprovedStudentService {

    @Autowired
    private ApprovedStudentRepository approvedStudentRepository;

    public List<ApprovedStudent> getAllApprovedStudents() {
        return approvedStudentRepository.findAll();
    }

    public boolean addApprovedStudent(ApprovedStudent approvedStudent) {
        ApprovedStudent existing =
                approvedStudentRepository.findByRollNumber(approvedStudent.getRollNumber());

        if (existing != null) {
            return false;
        }

        approvedStudentRepository.save(approvedStudent);
        return true;
    }

    public boolean deleteApprovedStudent(int id) {
        if (!approvedStudentRepository.existsById(id)) {
            return false;
        }

        approvedStudentRepository.deleteById(id);
        return true;
    }
}
