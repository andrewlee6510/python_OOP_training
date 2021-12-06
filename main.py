from student import course, student

s1 = student("Tim", 19, 95)
s2 = student("Jerry", 23, 75)
s3 = student("Bozo", 16, 66)
science_course = course("science", 2)

science_course.add_student(s1)
science_course.add_student(s2)

print(science_course.students[1].name)


