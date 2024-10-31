subjects = [int(input(f"Enter marks for subject {i+1}: ")) for i in range(3)]
total = sum(subjects)
percentage = total / 3
if percentage >= 90:
    grade = 'A'
elif percentage >= 75:
    grade = 'B'
elif percentage >= 50:
    grade = 'C'
else:
    grade = 'D'
print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade)
