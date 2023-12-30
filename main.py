import sqlite3
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()


conn = sqlite3.connect('university.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        name TEXT,
        group_id INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS groups (
        group_id INTEGER PRIMARY KEY,
        name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS teachers (
        teacher_id INTEGER PRIMARY KEY,
        name TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS subjects (
        subject_id INTEGER PRIMARY KEY,
        name TEXT,
        teacher_id INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades (
        grade_id INTEGER PRIMARY KEY,
        student_id INTEGER,
        subject_id INTEGER,
        grade INTEGER,
        date TEXT,
        FOREIGN KEY (student_id) REFERENCES students (student_id),
        FOREIGN KEY (subject_id) REFERENCES subjects (subject_id)
    )
''')

# Заповнення таблиць випадковими даними
group_ids = list(range(1, 4))
for group_id in group_ids:
    cursor.execute('INSERT INTO groups (group_id, name) VALUES (?, ?)', (group_id, f'Group-{group_id}'))

teacher_ids = list(range(1, 6))
for teacher_id in teacher_ids:
    cursor.execute('INSERT INTO teachers (teacher_id, name) VALUES (?, ?)', (teacher_id, fake.name()))

subject_ids = list(range(1, 9))
for subject_id in subject_ids:
    cursor.execute('INSERT INTO subjects (subject_id, name, teacher_id) VALUES (?, ?, ?)',
                   (subject_id, fake.word(), random.choice(teacher_ids)))

student_ids = list(range(1, 51))
for student_id in student_ids:
    cursor.execute('INSERT INTO students (student_id, name, group_id) VALUES (?, ?, ?)',
                   (student_id, fake.name(), random.choice(group_ids)))


for _ in range(20):
    cursor.execute('INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)',
                   (random.choice(student_ids), random.choice(subject_ids), random.randint(60, 100),
                    (datetime.now() - timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d')))


conn.commit()
conn.close()
