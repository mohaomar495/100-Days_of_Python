student_heights = input("Input a list of student heights ").split()
sum = 0
average = 0
for student_height in student_heights:
  sum += int(student_height)
  average = sum / len(student_heights)
print(sum)
print(round(average))


#     OR

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

height_total = 0
for height in student_heights:
  height_total += height
print(height_total)

lenght_student = 0
for lenght in student_heights:
  lenght_student += 1
print(lenght_student)

print(round(height_total / lenght_student))

# End of program.

