print("Exam Grade Calculator")
name = input("Name of the exam:")
maxScore = int(input("Max. Poss. Score:"))
score = float(input("Your score:"))
score = round(score, 2)
if score >= 90.00:
    print("You got", score, ", which is an A+")
elif score >= 80.00:
    print("You got", score, ", which is an A")
elif score >= 70.00:
    print("You got", score, ", which is a B")
elif score >= 60.00:
    print("You got", score, ", which is a C")
elif score >= 50.00:
    print("You got", score, ", which is a D")
else:
    print("You got", score, ", which is a U")
