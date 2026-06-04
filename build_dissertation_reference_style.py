from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.shared import Inches, Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn


OUT = "Online_Quiz_Portal_Dissertation_Reference_Style.docx"


def shade(cell, fill):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), fill)
    tc_pr.append(shd)


def cell_text(cell, text, bold=False, size=10):
    cell.text = ""
    p = cell.paragraphs[0]
    r = p.add_run(str(text))
    r.bold = bold
    r.font.size = Pt(size)
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER


def table(doc, headers, rows, widths=None):
    t = doc.add_table(rows=1, cols=len(headers))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(headers):
        cell_text(t.rows[0].cells[i], h, bold=True)
        shade(t.rows[0].cells[i], "E8EEF5")
        if widths:
            t.rows[0].cells[i].width = Inches(widths[i])
    for row in rows:
        cells = t.add_row().cells
        for i, v in enumerate(row):
            cell_text(cells[i], v)
            if widths:
                cells[i].width = Inches(widths[i])
    doc.add_paragraph()
    return t


def h(doc, text, level=1):
    p = doc.add_heading(text, level=level)
    for r in p.runs:
        r.font.color.rgb = RGBColor(0, 0, 0)
        r.font.bold = True
    return p


def p(doc, text):
    para = doc.add_paragraph(text)
    para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    para.paragraph_format.space_after = Pt(8)
    para.paragraph_format.line_spacing = 1.15
    return para


def bullets(doc, items):
    for item in items:
        para = doc.add_paragraph(style="List Bullet")
        para.add_run(item)
        para.paragraph_format.space_after = Pt(4)


def nums(doc, items):
    for item in items:
        para = doc.add_paragraph(style="List Number")
        para.add_run(item)
        para.paragraph_format.space_after = Pt(4)


def page_break(doc):
    doc.add_page_break()


def add_page_number(paragraph):
    paragraph.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = paragraph.add_run("Page ")
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), "PAGE")
    run._r.addnext(fld)


def add_toc(paragraph):
    run = paragraph.add_run()
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), r'TOC \o "1-3" \h \z \u')
    run._r.append(fld)


doc = Document()
sec = doc.sections[0]
sec.top_margin = Inches(0.9)
sec.bottom_margin = Inches(0.9)
sec.left_margin = Inches(1.0)
sec.right_margin = Inches(1.0)
add_page_number(sec.footer.paragraphs[0])

styles = doc.styles
styles["Normal"].font.name = "Times New Roman"
styles["Normal"].font.size = Pt(12)
for name, size in [("Heading 1", 14), ("Heading 2", 13), ("Heading 3", 12)]:
    st = styles[name]
    st.font.name = "Times New Roman"
    st.font.size = Pt(size)
    st.font.bold = True
    st.font.color.rgb = RGBColor(0, 0, 0)

# Cover
cover = doc.add_paragraph()
cover.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = cover.add_run("Final Year Project Dissertation\n")
r.bold = True
r.font.size = Pt(16)
r.font.name = "Times New Roman"

cover = doc.add_paragraph()
cover.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = cover.add_run("Project: Online Quiz Portal\n")
r.bold = True
r.font.size = Pt(20)
r.font.name = "Times New Roman"

cover = doc.add_paragraph()
cover.alignment = WD_ALIGN_PARAGRAPH.CENTER
cover.add_run("Course-wise Test Management, Student Dashboard, and Performance Tracking\n").bold = True

doc.add_paragraph()
for line in [
    "[Your Course / Programme]",
    "Level: Final Year",
    "Project for [Subject / Department]",
    "Student: [Your Name] ([Your Roll Number])",
    "Supervisor: [Guide/Faculty Name]",
    "Institution: [College/School Name]",
    "Academic Year: 2025-2026",
    "Word Count: [To be updated]",
]:
    para = doc.add_paragraph()
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    para.add_run(line)

page_break(doc)

h(doc, "TABLE OF CONTENTS", 1)
p(doc, "Right-click the table below in Microsoft Word and choose Update Field before final printing/submission.")
toc_para = doc.add_paragraph()
add_toc(toc_para)
page_break(doc)

h(doc, "1 ABSTRACT", 1)
p(
    doc,
    "The Online Quiz Portal is a web-based academic application designed to simplify the process of creating, "
    "conducting, and evaluating multiple-choice tests. The system has been developed using Java Spring Boot "
    "for the backend, MySQL for database management, and HTML, CSS, and JavaScript for the frontend. The project "
    "supports two major user roles: administrator and student. Administrators can manage quiz questions and tests, "
    "while students can register using approved roll numbers, log in, view tests according to their course, attempt "
    "quizzes, and view their previous performance."
)
p(
    doc,
    "A key problem addressed by this project is the manual effort involved in quiz preparation, evaluation, and "
    "result tracking. The system reduces this effort by automatically calculating scores and storing results in a "
    "structured database. The project also includes course-wise test visibility, so students only see relevant tests. "
    "The registration flow has been improved by using an approved student list and preventing duplicate roll number "
    "registration."
)
p(
    doc,
    "The system was implemented incrementally. The first increment focused on login, registration, and database "
    "connectivity. The second increment introduced admin question management and quiz attempts. The third increment "
    "added result history, approved roll number validation, course-wise subjects, tests, and student dashboard features. "
    "Future work may include AI-based question generation, better authentication through Spring Security, timer-based "
    "tests, and graphical performance analytics."
)
page_break(doc)

h(doc, "2 PROJECT INTRODUCTION", 1)
p(
    doc,
    "Most educational institutions conduct regular quizzes and internal assessments to evaluate student learning. "
    "In many cases, these quizzes are still managed manually or through disconnected tools. Manual quiz management "
    "requires question preparation, answer checking, result calculation, and record maintenance. This increases the "
    "workload of teachers and may lead to delays or mistakes in result processing."
)
p(
    doc,
    "The Online Quiz Portal provides a centralized web-based solution for this problem. It allows an admin to create "
    "and manage questions and allows students to attempt quizzes online. The system stores all important data in a "
    "MySQL database, including users, courses, subjects, tests, questions, and results."
)

h(doc, "2.1 Motivation for the Project", 2)
p(
    doc,
    "The motivation for this project comes from the need for a simple and practical academic testing system. A college "
    "or school may have students from multiple courses, and each course can have different subjects and tests. A manual "
    "system becomes difficult to manage when the number of students and subjects increases. A web-based quiz portal can "
    "make the process faster, more organized, and easier to maintain."
)

h(doc, "2.2 Aim and Objectives", 2)
h(doc, "2.2.1 Aim", 3)
p(
    doc,
    "The main aim of the project is to develop a web-based Online Quiz Portal that allows administrators to manage tests "
    "and questions while allowing students to register, log in, attempt course-wise tests, and view performance history."
)
h(doc, "2.2.2 Objectives", 3)
nums(
    doc,
    [
        "To design a role-based quiz portal for admin and student users.",
        "To implement student registration using approved roll number verification.",
        "To prevent duplicate registration using the same roll number.",
        "To store application data using MySQL tables and relationships.",
        "To implement REST endpoints using Java Spring Boot.",
        "To allow admins to add, view, and delete quiz questions.",
        "To create a student dashboard that displays course-wise available tests.",
        "To calculate quiz scores automatically and store result history.",
        "To prepare the system for future AI-based question generation.",
    ],
)
page_break(doc)

h(doc, "3 LITERATURE REVIEW", 1)
p(
    doc,
    "Online examination and quiz systems have become common in educational institutions because they reduce manual "
    "work and improve speed of evaluation. A web-based system allows users to access tests from a browser, while the "
    "server manages authentication, data storage, and result processing."
)
h(doc, "3.1 Web-based Examination Systems", 2)
p(
    doc,
    "Web-based examination systems generally provide login functionality, question display, answer submission, and "
    "result calculation. These systems reduce the dependency on paper-based tests and allow records to be stored "
    "digitally. For an academic institution, this can improve accuracy and reduce administrative effort."
)
h(doc, "3.2 Student Result Management", 2)
p(
    doc,
    "Result management is an important part of any assessment system. If marks are stored digitally, students can "
    "view their previous attempts and teachers can monitor performance. In this project, the results table stores "
    "the student reference, score, total marks, and attempt time."
)
h(doc, "3.3 Authentication and Role-based Access", 2)
p(
    doc,
    "A quiz portal needs to separate admin and student access. Admin users should manage questions and tests, while "
    "students should only attempt tests and view their own result history. The current project uses a users table "
    "with a role column. The role value decides whether the user is treated as admin or student."
)
h(doc, "3.4 Justification", 2)
p(
    doc,
    "The reviewed ideas justify the development of a course-wise quiz portal because it combines question management, "
    "student verification, test attempts, and result storage in one system. The project is suitable for a final-year "
    "software development submission because it demonstrates frontend development, backend API design, database "
    "relationships, and practical role-based workflows."
)
page_break(doc)

h(doc, "4 METHODOLOGY", 1)
h(doc, "4.1 Research Method and Requirement Understanding", 2)
p(
    doc,
    "The project requirements were understood by analysing common academic quiz workflows. The main stakeholders are "
    "admins or faculty members who manage tests, and students who attempt tests. The requirements were refined during "
    "development as practical concerns appeared, such as approved roll number validation, course-wise tests, and result "
    "history."
)
h(doc, "4.2 Development Methodology", 2)
p(
    doc,
    "An incremental development methodology was followed. The project was built in small working increments so each "
    "feature could be tested before moving to the next one. This approach was suitable because the application started "
    "as a basic quiz portal and was later extended with registration validation, dashboards, courses, subjects, tests, "
    "and performance tracking."
)
table(
    doc,
    ["Increment", "Features Implemented"],
    [
        ["First Increment", "Spring Boot project setup, MySQL connection, user login, registration"],
        ["Second Increment", "Admin question management, quiz page, score calculation"],
        ["Third Increment", "Result saving, result history, CSS styling, validation"],
        ["Fourth Increment", "Approved roll number registration and role-based page protection"],
        ["Fifth Increment", "Courses, subjects, tests, and student dashboard"],
    ],
    [1.6, 4.9],
)
h(doc, "4.3 IDE, Framework, Languages and Tools", 2)
table(
    doc,
    ["Tool/Technology", "Use in Project"],
    [
        ["IntelliJ IDEA Community", "Development environment"],
        ["Java", "Backend programming language"],
        ["Spring Boot", "Web application framework and embedded server"],
        ["Spring Data JPA", "Database access and object-relational mapping"],
        ["MySQL", "Relational database"],
        ["HTML/CSS/JavaScript", "Frontend pages and browser interaction"],
        ["MySQL Workbench", "Database creation and SQL execution"],
    ],
    [2.2, 4.3],
)
page_break(doc)

h(doc, "5 REQUIREMENTS, SPECIFICATION AND DESIGN", 1)
h(doc, "5.1 Functional Requirements", 2)
table(
    doc,
    ["ID", "Requirement", "User"],
    [
        ["FR1", "The system shall allow admin login.", "Admin"],
        ["FR2", "The system shall allow students to register using approved roll number.", "Student"],
        ["FR3", "The system shall prevent duplicate roll number registration.", "Student"],
        ["FR4", "The system shall allow admin to add questions.", "Admin"],
        ["FR5", "The system shall allow admin to delete questions.", "Admin"],
        ["FR6", "The system shall show course-wise tests to students.", "Student"],
        ["FR7", "The system shall calculate quiz score automatically.", "Student"],
        ["FR8", "The system shall save quiz result in database.", "Student"],
        ["FR9", "The system shall show previous result history.", "Student"],
    ],
    [0.7, 4.6, 1.2],
)
h(doc, "5.2 Non-functional Requirements", 2)
bullets(
    doc,
    [
        "Usability: The user interface should be simple enough for students and admins to use.",
        "Reliability: The system should store quiz and result data consistently in MySQL.",
        "Maintainability: The code is divided into model, repository, service, and controller packages.",
        "Security: Basic role-based page protection is included; professional security can be added later.",
        "Scalability: The database design supports multiple courses, subjects, and tests.",
    ],
)
h(doc, "5.3 Database Design", 2)
table(
    doc,
    ["Table", "Main Fields", "Purpose"],
    [
        ["users", "id, username, password, role, roll_number, course_id", "Stores registered users"],
        ["approved_students", "id, roll_number, student_name, course_id", "Validates student registration"],
        ["courses", "id, course_name", "Stores courses"],
        ["subjects", "id, subject_name, course_id", "Stores subjects by course"],
        ["tests", "id, test_title, subject_id, course_id", "Stores tests by subject/course"],
        ["questions", "id, test_id, question_text, options, correct_option", "Stores MCQ questions"],
        ["results", "id, user_id, score, total, taken_at", "Stores quiz performance"],
    ],
    [1.4, 3.2, 1.9],
)
h(doc, "5.4 System Architecture", 2)
p(doc, "The application follows a layered architecture:")
nums(
    doc,
    [
        "Frontend pages send requests using JavaScript fetch API.",
        "Controllers receive browser requests and return responses.",
        "Services contain business logic such as login, registration, and fetching tests.",
        "Repositories interact with MySQL using Spring Data JPA.",
        "Models represent database tables as Java classes.",
    ],
)
page_break(doc)

h(doc, "6 DEVELOPMENT AND IMPLEMENTATION", 1)
h(doc, "6.1 Backend Implementation", 2)
p(
    doc,
    "The backend was implemented using Spring Boot. REST controllers were created for authentication, questions, "
    "results, subjects, and tests. Repository interfaces extend JpaRepository, allowing Spring Boot to generate "
    "database queries automatically based on method names such as findByUsernameAndPassword and findByCourseId."
)
h(doc, "6.2 Frontend Implementation", 2)
p(
    doc,
    "The frontend was created using HTML, CSS, and JavaScript. Separate pages were created for login, registration, "
    "admin panel, student dashboard, quiz attempt, and result history. JavaScript fetch calls connect the frontend "
    "with Spring Boot endpoints."
)
h(doc, "6.3 Student Registration Logic", 2)
nums(
    doc,
    [
        "Student enters username, password, and roll number.",
        "System checks whether the username already exists.",
        "System checks whether the roll number exists in approved_students.",
        "System checks whether the roll number has already been used.",
        "If all checks pass, the user is saved with role student and course_id.",
    ],
)
h(doc, "6.4 Student Dashboard Logic", 2)
p(
    doc,
    "After login, the student lands on dashboard.html. The dashboard reads the logged-in user's details from browser "
    "storage and calls /tests/my. The backend identifies the student's course and returns only the tests belonging "
    "to that course."
)
h(doc, "6.5 API Endpoints", 2)
table(
    doc,
    ["Endpoint", "Method", "Description"],
    [
        ["/login", "POST", "Authenticates user and returns role"],
        ["/register", "POST", "Registers approved student"],
        ["/questions", "GET", "Fetches questions, optionally by testId"],
        ["/questions/add", "POST", "Adds question"],
        ["/questions/delete/{id}", "DELETE", "Deletes question"],
        ["/result/save", "POST", "Saves result"],
        ["/result/history", "GET", "Fetches result history"],
        ["/subjects/my", "GET", "Fetches subjects by student course"],
        ["/tests/my", "GET", "Fetches tests by student course"],
    ],
    [2.0, 1.0, 3.5],
)
page_break(doc)

h(doc, "7 TESTING AND RESULTS ANALYSIS", 1)
h(doc, "7.1 Unit Testing", 2)
p(doc, "Individual features were tested after implementation. Login, registration, question fetching, and result saving were tested separately.")
table(
    doc,
    ["Test Case", "Input", "Expected Output", "Result"],
    [
        ["Admin login", "admin/admin123", "Admin page opens", "Pass"],
        ["Student login", "prabh2/1234", "Dashboard opens", "Pass"],
        ["Invalid login", "Wrong credentials", "Error message", "Pass"],
        ["Valid registration", "Approved roll number", "Account created", "Pass"],
        ["Duplicate roll number", "Used roll number", "Registration failed", "Pass"],
        ["Invalid roll number", "999", "Registration failed", "Pass"],
        ["Fetch tests", "Student course_id 1", "BCA tests displayed", "Pass"],
        ["Submit quiz", "All answers selected", "Score displayed and saved", "Pass"],
    ],
    [1.6, 1.6, 2.2, 0.8],
)
h(doc, "7.2 Integration Testing", 2)
p(
    doc,
    "Integration testing was performed by checking complete flows between frontend, backend, and database. For "
    "example, student registration was tested from register.html to AuthController, UserService, UserRepository, "
    "and finally the users table in MySQL."
)
h(doc, "7.3 End-to-End Testing", 2)
nums(
    doc,
    [
        "Admin logs in and adds a question.",
        "Student registers using a valid roll number.",
        "Student logs in and reaches dashboard.",
        "Student starts a test and submits answers.",
        "System calculates score and stores result.",
        "Student views result history.",
    ],
)
h(doc, "7.4 Results Achieved", 2)
bullets(
    doc,
    [
        "The application successfully connects Spring Boot with MySQL.",
        "Role-based login redirects users to the correct page.",
        "Approved roll number validation works correctly.",
        "Course-wise tests are displayed on the student dashboard.",
        "Quiz results are calculated and stored successfully.",
    ],
)
page_break(doc)

h(doc, "8 CRITICAL EVALUATION AND REFLECTION", 1)
h(doc, "8.1 Review of Achievements Against Objectives", 2)
p(
    doc,
    "The project achieved its main objective of creating a working online quiz portal. The system supports admin "
    "and student users, validates student registration, displays course-wise tests, calculates scores, and stores "
    "result history. The database structure also supports future expansion into multiple courses and subjects."
)
h(doc, "8.2 Problems Faced and Solutions Adopted", 2)
table(
    doc,
    ["Problem", "Solution"],
    [
        ["Column naming mismatch between Java and MySQL", "Used @Column annotations to map camelCase fields to snake_case columns"],
        ["Static HTML not updating immediately", "Used browser refresh, Ctrl+F9 build, or app restart depending on file type"],
        ["Students could use same roll number", "Added roll_number column to users and checked uniqueness"],
        ["Dashboard initially showed raw JSON/API data", "Created dashboard.html to format API data for students"],
        ["Questions were not linked to tests", "Added test_id to questions table and repository query findByTestId"],
    ],
    [2.5, 4.0],
)
h(doc, "8.3 Product Evaluation", 2)
p(
    doc,
    "The product is suitable as a beginner-to-intermediate final year project because it demonstrates practical "
    "software engineering concepts. It includes database design, REST APIs, frontend-backend communication, user "
    "roles, validation, and result tracking. The system is not yet production ready, but it forms a strong base for "
    "further improvements."
)
h(doc, "8.4 Personal Reflection", 2)
p(
    doc,
    "During development, important concepts such as Spring Boot controllers, services, repositories, JPA models, "
    "foreign keys, API endpoints, and frontend fetch requests were understood in a practical way. The project also "
    "helped in understanding how requirements can change during development and how the database design must evolve "
    "to support new features."
)
page_break(doc)

h(doc, "9 CONCLUSIONS", 1)
p(
    doc,
    "The Online Quiz Portal project successfully provides a centralized system for academic quiz management. It allows "
    "admins to manage questions and students to register, log in, attempt tests, and view results. The addition of "
    "course-wise tests and student dashboard makes the system more suitable for real college or school use. The project "
    "also demonstrates a practical layered architecture using Spring Boot and MySQL."
)
p(
    doc,
    "Future development can include AI question generation, advanced security using Spring Security, test timers, "
    "charts for performance analytics, and an admin interface for creating subjects and tests directly from the browser."
)

h(doc, "REFERENCES", 1)
bullets(
    doc,
    [
        "Spring Boot Reference Documentation.",
        "Spring Data JPA Reference Documentation.",
        "MySQL 8.0 Reference Manual.",
        "Oracle Java Documentation.",
        "MDN Web Docs for HTML, CSS, and JavaScript.",
        "Google Gemini API Documentation for future AI question generation.",
    ],
)
page_break(doc)

h(doc, "APPENDIX 1 - SAMPLE DATABASE TABLES", 1)
table(
    doc,
    ["Table", "Sample Columns"],
    [
        ["users", "id, username, password, role, roll_number, course_id"],
        ["approved_students", "id, roll_number, student_name, course_id"],
        ["courses", "id, course_name"],
        ["subjects", "id, subject_name, course_id"],
        ["tests", "id, test_title, subject_id, course_id"],
        ["questions", "id, test_id, question_text, option_a, option_b, option_c, option_d, correct_option"],
        ["results", "id, user_id, score, total, taken_at"],
    ],
    [2.0, 4.5],
)

h(doc, "APPENDIX 2 - SAMPLE TEST PLAN", 1)
table(
    doc,
    ["Area", "Manual Test"],
    [
        ["Login", "Check admin, student, and invalid credentials"],
        ["Registration", "Check valid, invalid, duplicate roll numbers"],
        ["Admin", "Add, view, and delete questions"],
        ["Dashboard", "Verify tests shown according to course"],
        ["Quiz", "Check answer validation and scoring"],
        ["Results", "Check saved result history"],
    ],
    [2.0, 4.5],
)

h(doc, "APPENDIX 3 - FUTURE AI QUESTION GENERATION PLAN", 1)
p(
    doc,
    "In future, the admin panel can include an AI question generation feature. The admin can enter subject, topic, "
    "difficulty level, and number of questions. The Spring Boot backend can call a free-tier AI API such as Google "
    "Gemini API. The API key should remain in the backend and must not be placed in frontend JavaScript. The generated "
    "questions should be reviewed by the admin before being saved to the database."
)

doc.core_properties.title = "Online Quiz Portal Final Year Project Dissertation"
doc.core_properties.subject = "Final Year Project Dissertation"
doc.core_properties.author = "[Your Name]"
doc.save(OUT)
print(OUT)
