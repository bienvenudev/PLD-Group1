def Questionnaire(question, choices, correct_answer):
    print(question)
    for i in range(len(choices)):
        print(f"  {i+1}- {choices[i]}")
    answer = input("Enter the correct answer (between 1 and 3): ")
    check_answer(correct_answer, answer)
    print()

def check_answer(corr_answ, answ):
    if corr_answ == answ:
        print("Correct answer!")
    else:
        print("False answer!")

level = input("Choose a level (1, 2, or 3): ")

# level one questionnaire implementation
Questionnaire("Which python function displays a message on the screen ?",
              ["input", "print", "printf"], "2")
Questionnaire("Which of the following elements is a tuple?",
              ["a=[0,2]", "b={'name':'Gaga'}", "c=(8,5)"],"3")
Questionnaire("What does OOP stands for ?",
              ["Orient Object Programming", "Oriented Object Programming", "Oriental Object Programming"],
              "2")