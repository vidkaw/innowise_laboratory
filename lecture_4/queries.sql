-- Create students table

    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        birth_year INTEGER NOT NULL
    );
    

-- Create grades table

    CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        subject TEXT NOT NULL,
        grade INTEGER NOT NULL CHECK (grade >= 1 AND grade <= 100),
        FOREIGN KEY (student_id) REFERENCES students(id)
    );
    

-- Insert student data

    INSERT INTO students (full_name, birth_year) VALUES
    ('Alice Johnson', 2005),
    ('Brian Smith', 2004),
    ('Carla Reyes', 2006),
    ('Daniel Kim', 2005),
    ('Eva Thompson', 2003),
    ('Felix Nguyen', 2007),
    ('Grace Patel', 2005),
    ('Henry Lopez', 2004),
    ('Isabella Martinez', 2006);
    

-- Insert grade data

    INSERT INTO grades (student_id, subject, grade) VALUES
    (1, 'Math', 88),
    (1, 'English', 92),
    (1, 'Science', 85),
    (2, 'Math', 75),
    (2, 'History', 83),
    (2, 'English', 79),
    (3, 'Science', 95),
    (3, 'Math', 91),
    (3, 'Art', 89),
    (4, 'Math', 84),
    (4, 'Science', 88),
    (4, 'Physical Education', 93),
    (5, 'English', 90),
    (5, 'History', 85),
    (5, 'Math', 88),
    (6, 'Science', 72),
    (6, 'Math', 78),
    (6, 'English', 81),
    (7, 'Art', 94),
    (7, 'Science', 87),
    (7, 'Math', 90),
    (8, 'History', 77),
    (8, 'Math', 83),
    (8, 'Science', 80),
    (9, 'English', 96),
    (9, 'Math', 89),
    (9, 'Art', 92);
    

-- Index for student birth year
CREATE INDEX idx_students_birth_year ON students(birth_year);

-- Index for student_id in grades
CREATE INDEX idx_grades_student_id ON grades(student_id);

-- Index for subject in grades
CREATE INDEX idx_grades_subject ON grades(subject);

-- Index for student name
CREATE INDEX idx_students_name ON students(full_name);

-- Query 3: All grades for Alice Johnson

    SELECT s.full_name, g.subject, g.grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    WHERE s.full_name = 'Alice Johnson'
    ORDER BY g.subject;
    

-- Query 4: Average grade per student

    SELECT s.full_name, ROUND(AVG(g.grade), 2) as average_grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    GROUP BY s.id, s.full_name
    ORDER BY average_grade DESC;
    

-- Query 5: Students born after 2004

    SELECT full_name, birth_year
    FROM students
    WHERE birth_year > 2004
    ORDER BY birth_year, full_name;
    

-- Query 6: Average grade per subject

    SELECT subject, ROUND(AVG(grade), 2) as average_grade, COUNT(*) as grade_count
    FROM grades
    GROUP BY subject
    ORDER BY average_grade DESC;
    

-- Query 7: Top 3 students by average grade

    SELECT s.full_name, ROUND(AVG(g.grade), 2) as average_grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    GROUP BY s.id, s.full_name
    ORDER BY average_grade DESC
    LIMIT 3;
    

-- Query 8: Students with grade below 80 in any subject

    SELECT DISTINCT s.full_name, g.subject, g.grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    WHERE g.grade < 80
    ORDER BY s.full_name, g.grade;
    

