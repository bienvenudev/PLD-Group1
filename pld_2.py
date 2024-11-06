def Questionnaire(question, choices, correct_answer):
    print(question)
    for i in range(len(choices)):
        print(f"  {i+1}- {choices[i]}")