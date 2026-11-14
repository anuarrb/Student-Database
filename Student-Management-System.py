import sqlite3

conn = sqlite3.connect('students.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    course TEXT
)

''')

conn.commit()

cursor.execute(
    "DELETE FROM students"
)

cursor.execute(
    "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
    ('Amit', 21, 'Python')
)
cursor.execute(
    "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
    ('Anita', 22, 'Data Science')
)
cursor.execute(
    "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
    ('Rahul', 23, 'Python')
)
cursor.execute(
    "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
    ('Bob', 23, 'Web Development')
)
print("\nStudent Record inserted successfully into the database!")

cursor.execute(
    "SELECT * FROM students"
)
rows = cursor.fetchall()
for row in rows:
    print("ID: ", row[0])
    print("Name: ", row[1])
    print("Age: ", row[2])
    print("Course: ", row[3])
    print("------------------")

conn.commit()

cursor.execute(
    "UPDATE students SET course = ? WHERE course = ?",
    ('Machine learning using Python', 'Python')
)
print("\nRecord updated successfully!")

conn.commit()

cursor.execute(
    "DELETE FROM students WHERE name = ?", ('Bob',)
)
print("\nRecord deleted successfully!")

conn.commit()

cursor.execute(
    "SELECT * FROM students"
)
rows = cursor.fetchall()
for row in rows:
    print("ID: ", row[0])
    print("Name: ", row[1])
    print("Age: ", row[2])
    print("Course: ", row[3])
    print("------------------")

conn.close()