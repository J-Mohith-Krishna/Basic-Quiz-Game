def run_quiz(questions):
    score = 0
    total_questions = len(questions)

    for question, answer in questions.items():
        print(question)
        user_answer = input("Your answer: ")

        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    print("\nQuiz Complete!")
    print("Your Score:", score, "out of", total_questions)

def main():
    questions = {
        "What is the capital of France?": "Paris",
        "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
        "What is the largest planet in our solar system?": "Jupiter",
        "What year did the Titanic sink?": "1912"
    }

    print("Welcome to the Quiz Game!")
    run_quiz(questions)

if __name__ == "__main__":
    main()
