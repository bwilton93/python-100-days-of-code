# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# This stores a temp variable to be compared against using the for loop
output_score = 0

# On each loop this compares the score to the current output, if the score is greater it updates the output score
for score in student_scores:
    if score > output_score:
        output_score = score

print(f"The highest score in the class is: {output_score}")
