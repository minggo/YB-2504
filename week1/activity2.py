import numpy as np

scores = np.array([
    [78, 85, 90],
    [88, 79, 92],
    [84, 76, 88],
    [90, 93, 94],
    [75, 80, 70]
])

student_average_score = np.average(scores, axis=1)
print(f"The average score of each student is",
      np.array2string(student_average_score, formatter={'float_kind':lambda x: f"{x:.2f}"}))

subject_average_score = np.average(scores, axis=0)
print(f"The average score of each subject is",
      np.array2string(subject_average_score, formatter={'float_kind':lambda x: f"{x:.2f}"}))


print(f"The student (row index) with the highest total score is {np.argmax(student_average_score)}")

# Add 5 bonus points to the third subject for all students.
scores[:, 2] += 5
print("After adding 5 bonus points to the third subject for all students, the result is:")
print(f"{scores}")