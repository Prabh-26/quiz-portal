# Online Quiz Portal

A Spring Boot based online quiz portal for admins and students. Admins can approve students, create subjects, create tests, add or generate questions, and delete tests or approved students. Students can register, log in, take assigned quizzes, and view result history.

## Tech Stack

- Java 17+
- Spring Boot
- Spring Data JPA
- MySQL
- HTML, CSS, JavaScript
- Gemini API integration for question generation

## Features

- Admin login and student login
- Student registration with approved roll number validation
- Subject, test, question, and approved-student management
- Gemini-powered question generation
- Quiz attempt and result history
- Responsive static UI

## Setup

1. Create a MySQL database named `quiz_portal`.
2. Set environment variables for your local database:

```powershell
$env:DB_URL="jdbc:mysql://localhost:3306/quiz_portal"
$env:DB_USERNAME="root"
$env:DB_PASSWORD="your_mysql_password"
$env:GEMINI_API_KEY="your_gemini_api_key"
$env:DDL_AUTO="update"
```

3. Run the app:

```powershell
.\mvnw.cmd spring-boot:run
```

4. Open:

```text
http://localhost:8080/login.html
```

## Important

Do not commit real database passwords or API keys. This project reads sensitive values from environment variables.

## Testing

```powershell
.\mvnw.cmd test
```
