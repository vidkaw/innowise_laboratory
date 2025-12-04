import sqlite3
import os

def create_database():
    """Create database and execute all SQL queries"""
    
    # Remove old database if exists
    if os.path.exists('school.db'):
        os.remove('school.db')
    
    # Create database connection
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    
    # Create SQL file to log all queries
    sql_file = open('queries.sql', 'w', encoding='utf-8')
    
    def execute_and_log(sql_query, description=None):
        """Execute SQL query and log it to file"""
        if description:
            sql_file.write(f'-- {description}\n')
        sql_file.write(sql_query + '\n\n')
        cursor.execute(sql_query)
    
    print("=" * 60)
    print("Creating school.db database")
    print("=" * 60)
    
    # 1. Create tables
    print("\n1. Creating tables...")
    
    # Students table
    create_students_table = """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        birth_year INTEGER NOT NULL
    );
    """
    execute_and_log(create_students_table, "Create students table")
    
    # Grades table
    create_grades_table = """
    CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        subject TEXT NOT NULL,
        grade INTEGER NOT NULL CHECK (grade >= 1 AND grade <= 100),
        FOREIGN KEY (student_id) REFERENCES students(id)
    );
    """
    execute_and_log(create_grades_table, "Create grades table")
    
    # 2. Insert student data
    print("\n2. Inserting student data...")
    
    insert_students = """
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
    """
    execute_and_log(insert_students, "Insert student data")
    
    # 3. Insert grade data
    print("\n3. Inserting grade data...")
    
    # Get student IDs for correct grade insertion
    cursor.execute("SELECT id, full_name FROM students")
    students = cursor.fetchall()
    student_dict = {name: id for id, name in students}
    
    insert_grades = f"""
    INSERT INTO grades (student_id, subject, grade) VALUES
    ({student_dict['Alice Johnson']}, 'Math', 88),
    ({student_dict['Alice Johnson']}, 'English', 92),
    ({student_dict['Alice Johnson']}, 'Science', 85),
    ({student_dict['Brian Smith']}, 'Math', 75),
    ({student_dict['Brian Smith']}, 'History', 83),
    ({student_dict['Brian Smith']}, 'English', 79),
    ({student_dict['Carla Reyes']}, 'Science', 95),
    ({student_dict['Carla Reyes']}, 'Math', 91),
    ({student_dict['Carla Reyes']}, 'Art', 89),
    ({student_dict['Daniel Kim']}, 'Math', 84),
    ({student_dict['Daniel Kim']}, 'Science', 88),
    ({student_dict['Daniel Kim']}, 'Physical Education', 93),
    ({student_dict['Eva Thompson']}, 'English', 90),
    ({student_dict['Eva Thompson']}, 'History', 85),
    ({student_dict['Eva Thompson']}, 'Math', 88),
    ({student_dict['Felix Nguyen']}, 'Science', 72),
    ({student_dict['Felix Nguyen']}, 'Math', 78),
    ({student_dict['Felix Nguyen']}, 'English', 81),
    ({student_dict['Grace Patel']}, 'Art', 94),
    ({student_dict['Grace Patel']}, 'Science', 87),
    ({student_dict['Grace Patel']}, 'Math', 90),
    ({student_dict['Henry Lopez']}, 'History', 77),
    ({student_dict['Henry Lopez']}, 'Math', 83),
    ({student_dict['Henry Lopez']}, 'Science', 80),
    ({student_dict['Isabella Martinez']}, 'English', 96),
    ({student_dict['Isabella Martinez']}, 'Math', 89),
    ({student_dict['Isabella Martinez']}, 'Art', 92);
    """
    execute_and_log(insert_grades, "Insert grade data")
    
    # 4. Create indexes for optimization
    print("\n4. Creating indexes for query optimization...")
    
    indexes = [
        ("CREATE INDEX idx_students_birth_year ON students(birth_year);", "Index for student birth year"),
        ("CREATE INDEX idx_grades_student_id ON grades(student_id);", "Index for student_id in grades"),
        ("CREATE INDEX idx_grades_subject ON grades(subject);", "Index for subject in grades"),
        ("CREATE INDEX idx_students_name ON students(full_name);", "Index for student name")
    ]
    
    for sql, desc in indexes:
        execute_and_log(sql, desc)
    
    # 5. Execute required queries
    print("\n5. Executing required queries...")
    print("-" * 60)
    
    # Query 3: Find all grades for Alice Johnson
    print("\n3. All grades for Alice Johnson:")
    query3 = """
    SELECT s.full_name, g.subject, g.grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    WHERE s.full_name = 'Alice Johnson'
    ORDER BY g.subject;
    """
    execute_and_log(query3, "Query 3: All grades for Alice Johnson")
    cursor.execute(query3)
    for row in cursor.fetchall():
        print(f"  {row[1]}: {row[2]}")
    
    # Query 4: Average grade per student
    print("\n4. Average grade per student:")
    query4 = """
    SELECT s.full_name, ROUND(AVG(g.grade), 2) as average_grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    GROUP BY s.id, s.full_name
    ORDER BY average_grade DESC;
    """
    execute_and_log(query4, "Query 4: Average grade per student")
    cursor.execute(query4)
    for row in cursor.fetchall():
        print(f"  {row[0]}: {row[1]}")
    
    # Query 5: Students born after 2004
    print("\n5. Students born after 2004:")
    query5 = """
    SELECT full_name, birth_year
    FROM students
    WHERE birth_year > 2004
    ORDER BY birth_year, full_name;
    """
    execute_and_log(query5, "Query 5: Students born after 2004")
    cursor.execute(query5)
    for row in cursor.fetchall():
        print(f"  {row[0]} (born {row[1]})")
    
    # Query 6: Average grade per subject
    print("\n6. Average grade per subject:")
    query6 = """
    SELECT subject, ROUND(AVG(grade), 2) as average_grade, COUNT(*) as grade_count
    FROM grades
    GROUP BY subject
    ORDER BY average_grade DESC;
    """
    execute_and_log(query6, "Query 6: Average grade per subject")
    cursor.execute(query6)
    for row in cursor.fetchall():
        print(f"  {row[0]}: {row[1]} (grades: {row[2]})")
    
    # Query 7: Top 3 students by average grade
    print("\n7. Top 3 students by average grade:")
    query7 = """
    SELECT s.full_name, ROUND(AVG(g.grade), 2) as average_grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    GROUP BY s.id, s.full_name
    ORDER BY average_grade DESC
    LIMIT 3;
    """
    execute_and_log(query7, "Query 7: Top 3 students by average grade")
    cursor.execute(query7)
    for i, row in enumerate(cursor.fetchall(), 1):
        print(f"  {i}. {row[0]}: {row[1]}")
    
    # Query 8: Students with grade below 80 in any subject
    print("\n8. Students with grade below 80 in any subject:")
    query8 = """
    SELECT DISTINCT s.full_name, g.subject, g.grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    WHERE g.grade < 80
    ORDER BY s.full_name, g.grade;
    """
    execute_and_log(query8, "Query 8: Students with grade below 80 in any subject")
    cursor.execute(query8)
    for row in cursor.fetchall():
        print(f"  {row[0]}: {row[1]} - {row[2]}")
    
    # Statistics
    print("\n" + "=" * 60)
    print("DATABASE STATISTICS:")
    print("=" * 60)
    
    cursor.execute("SELECT COUNT(*) FROM students")
    print(f"Total students: {cursor.fetchone()[0]}")
    
    cursor.execute("SELECT COUNT(*) FROM grades")
    print(f"Total grades: {cursor.fetchone()[0]}")
    
    cursor.execute("SELECT COUNT(DISTINCT subject) FROM grades")
    print(f"Total subjects: {cursor.fetchone()[0]}")
    
    # Save changes and close connection
    conn.commit()
    sql_file.close()
    conn.close()
    
    print("\n" + "=" * 60)
    print("Database successfully created!")
    print("Files created:")
    print("  - school.db (SQLite database)")
    print("  - queries.sql (all SQL queries)")
    print("=" * 60)

if __name__ == "__main__":
    create_database()
