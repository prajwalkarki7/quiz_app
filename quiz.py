import time

# List of questions with options and correct answers
questions = [
    ("who is the first crewmate of luffy?", ["a) nami", "b) zoro", "c) ussop", "d) sanji"], "b"),
    ("who is shaktiman?", ["a) shivadhar", "b) shanidhar", "c) gangadhar", "d) lucky"], "c"),
    ("what is the caste of naruto?", ["a) uzumaki", "b) shippuden", "c) uchiha", "d) ninja"], "a"),
    ("what is the name of luffy devil fruit'?", ["a) goro goro no mi", "b) hana hana no mi", "c) hito hito no mi", "d) gomu gomu no mi"], "d"),
    ("who is the leader of akatsuki?", ["a) konan", "b) nagato", "c) obito", "d) madara"], "b"),
    ("what is the name of the villian in death note", ["a) light", "b) L", "c) shinigami", "d) zoro"], "a"),
    ("how do you say pizza in french", ["a) Le Pizza", "b) La Pizza", "c)L'Pizza ", "d) Li Pizza"], "b"),
    ("What is the name of iron man?", ["a)Edward Tony stark", "b)Anthony Edward stark ", "c)Haward stark", "d) robbert downry junior"], "b")
]

# Initialize score
score = 0

# Function to ask a question
def ask_question(question, options, correct_answer):
    global score
    start_time = time.time()
    
    print("\n" + question)
    for option in options:
        print(option)

    user_answer = input("Enter your answer (a/b/c/d): ").lower()
    end_time = time.time()

    time_taken = end_time - start_time
    if time_taken > 5:
        print("Time's up! No points for this question.")
    elif user_answer == correct_answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")

# Main function to run the quiz
def run_quiz():
    for question, options, correct_answer in questions:
        ask_question(question, options, correct_answer)
    print("\nQuiz Completed!")
    print(f"Your final score is {score} out of {len(questions)}.")

# Run the quiz
run_quiz()
