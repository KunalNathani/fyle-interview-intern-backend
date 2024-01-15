-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
SELECT COUNT(grade) FROM assignments WHERE teacher_id = (SELECT teacher_id FROM assignments GROUP BY teacher_id ORDER BY COUNT(teacher_id) DESC LIMIT 1) AND grade = 'A';
