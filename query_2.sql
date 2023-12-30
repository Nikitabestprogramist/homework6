
SELECT s.name AS student_name, AVG(g.grade) AS average_grade
FROM students s
JOIN grades g ON s.student_id = g.student_id
WHERE g.subject_id = :subject_id
GROUP BY s.student_id
ORDER BY AVG(g.grade) DESC
LIMIT 1;
