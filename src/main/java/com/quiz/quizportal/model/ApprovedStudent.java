package com.quiz.quizportal.model;

import jakarta.persistence.*;

@Entity
@Table(name = "approved_students")
public class ApprovedStudent {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @Column(name = "roll_number")
    private String rollNumber;

    @Column(name = "student_name")
    private String studentName;

    @Column(name = "course_id")
    private int courseId;

    public int getId() { return id; }
    public void setId(int id) { this.id = id; }

    public String getRollNumber() { return rollNumber; }
    public void setRollNumber(String rollNumber) { this.rollNumber = rollNumber; }

    public String getStudentName() { return studentName; }
    public void setStudentName(String studentName) { this.studentName = studentName; }

    public int getCourseId() { return courseId; }
    public void setCourseId(int courseId) { this.courseId = courseId; }
}