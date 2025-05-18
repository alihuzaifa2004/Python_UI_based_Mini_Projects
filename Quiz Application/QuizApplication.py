# console based Quiz Application

questions = {
    "What is the capital of France?": "paris",
    "What is 2 + 2?": "4",
    "What is the color of the sky?": "blue"
}
score = 0

for q, a in questions.items():
    ans = input(q + " ").lower()
    if ans == a:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print(f"Your score: {score}/{len(questions)}")
