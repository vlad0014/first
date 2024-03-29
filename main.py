math_scores = {
    "Іван": [85, 90, 95],
    "Марія": [75, 80, 85],
    "Петро": [90, 92, 88],
    "Олена": [82, 88, 90]
}
total_scores = 0
total_math = 0

for scores in math_scores.values():
    total_scores += sum(scores)
    total_math += len(scores)

many_score = total_scores / total_math

print("Середній бал усіх учнів:", many_score)