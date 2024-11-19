def display_welcome_screen():
    """Display the welcome screen and rules."""
    print("=" * 40)
    print("\tPython Knowledge Assessment")
    print("=" * 40)
    print("\nRules & Guidelines:")
    print("- Each question has 4 multiple-choice options")
    print("- Select your answer by typing 1, 2, 3, or 4")
    print("- Each correct answer is worth 1 point")
    print("- No penalty for wrong answers")
    input("\nPress Enter to continue...")
    
def select_difficulty():
    """Allow user to select difficulty level."""
    while True:
        level = input("Choose a level (1, 2, or 3): ")
        try:
            level = int(level)
            if level in [1, 2, 3]:
                return level
            else:
                print("ERROR!! Please choose 1, 2 or 3")
        except:
            print("ERROR!! The inpout must be an number")

def display_questionnaire(question):
    """Displaying the questionnaire and check the answer"""
    print(question[0])
    for i in range(len(question[1])):
        print(f"  {i+1}- {question[1][i]}")
    answer = input("Enter the correct answer (between 1 and 3): ")

    if answer == question[2]:
        print("✓ Correct answer!\n")
        return True
    else:
        print(f"✗ False answer! The correct answer is '{question[2]}'\n")
        return False
    
def start_questionnaire(questionnaire):
    marks = 0
    for question in questionnaire:
        if display_questionnaire(question): # if 'display_questionnaire' function returned 'True'
            marks +=1
    return marks