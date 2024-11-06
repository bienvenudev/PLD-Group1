def Questionnaire(question, choices, correct_answer):
    print(question)
    for i in range(len(choices)):
        print(f"  {i+1}- {choices[i]}")
    answer = input("Enter the correct answer (between 1 and 3): ")
    check_answer(correct_answer, answer)
    print()