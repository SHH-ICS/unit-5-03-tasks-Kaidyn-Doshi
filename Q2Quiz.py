# Create a second program that will read the file questions.txt, formatted as described above, and pose the questions to the user. 
# The program will keep score of the number of questions answered correctly.
# Open the file in read mode
with open("questions.txt", "r") as file:
    score = 0
    for line in file:
        if line.startswith("Correct Answer"):
            user_answer = input("Your answer: ")
            if user_answer.upper() == correct_answer:
                score += 1
        else:
            print(line.rstrip())
            if line.startswith(("A.", "B.", "C.", "D.")):
                if line.startswith("Correct Answer"):
                    correct_answer = line[-2]
    print(f"You scored {score} out of 5.")
