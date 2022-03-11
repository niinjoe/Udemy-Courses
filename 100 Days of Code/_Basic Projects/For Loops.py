# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total=0
for heights in student_heights:
  total+=heights
print(total)

num_students=0
for students in student_heights:
  num_students+=1
print(num_students)

avg=round(total/num_students)
print(avg)

for heights in student_heights:
  if heights%2==0:
    print(f"{heights} es par.")
  else:
    print(f"{heights} es impar.")
