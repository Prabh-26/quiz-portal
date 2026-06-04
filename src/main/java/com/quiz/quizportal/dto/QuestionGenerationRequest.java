package com.quiz.quizportal.dto;

public class QuestionGenerationRequest {

    private String topic;
    private int questionCount;
    private int testId;

    public String getTopic() { return topic; }
    public void setTopic(String topic) { this.topic = topic; }

    public int getQuestionCount() { return questionCount; }
    public void setQuestionCount(int questionCount) { this.questionCount = questionCount; }

    public int getTestId() { return testId; }
    public void setTestId(int testId) { this.testId = testId; }
}
