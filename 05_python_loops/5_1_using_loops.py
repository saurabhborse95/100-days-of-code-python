#### For Loop


fruits = ["apple", "banana", "cherry", "mango"]

for fruit in fruits:
    print(fruit)
    print(fruit + ' pie')


### Sum function

student_scores = [90, 80, 70, 60, 55, 78, 88, 98, 18, 45]

#option 1
total_exam_score = sum(student_scores)
print(total_exam_score)

sum_scores = 0

#option 2 with For Loop
for score in student_scores:
    sum_scores += score

print(sum_scores)


### Max of all scores

#option1
max_exam_score = max(student_scores)
print(max_exam_score)

#option2 with For Loop
max_score = 0

for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)


###For Loop and Range Function

for number in range(a, b)
  print(number)

range function must be used in conjunction of for loop

for number in range(1,11):            # increment by 1
    print(number)

for number in range(1,11, 3):         # increment with 3
    print(number)


##### Solving the Gauss Carl Challenge
sum = 0
for number in range(1,101):
    sum += number
print(sum)