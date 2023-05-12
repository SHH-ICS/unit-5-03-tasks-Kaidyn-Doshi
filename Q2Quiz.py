print("Google Pixel quiz: \n ")
with open("questions.txt", "r") as file:
    score = 0
    for line in file:
        if line.startswith("Correct Answer"):
            user_answer = input("Your answer: ")
            if user_answer.upper() == line[-2]:
                score += 1
        else:
            print(line.rstrip())
    print(f"You scored {score} out of 10.")
