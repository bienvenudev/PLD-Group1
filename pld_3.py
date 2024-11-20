def display_welcome_screen():
    """Display the welcome screen and rules."""
    print("=" * 45)
    print("\tPython Knowledge Assessment")
    print("=" * 45)
    print("\nRules & Guidelines:")
    print("- Each question has 4 multiple-choice options")
    print("- Select your answer by typing 1, 2, 3, or 4")
    print("- Each correct answer is worth 1 point")
    print("- No penalty for wrong answers")
    input("\nPress Enter to continue...")
    
def select_difficulty():
    """Allow user to select difficulty level."""
    while True:
        level = input("Select difficulty level (1, 2, or 3): ")
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
    answer = input("Enter your answer (1/2/3/4): ")

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

# level one questionnaire implementation
question1_1 = ["\nWhat is the correct file extension for Python files?",
              [".pt", ".pyt", ".py", ".python"], "3"]
question2_1 = ("Which python function displays a message on the screen ?",
              ["input()", "print()", "printf()", "show()"], "2")
question3_1 = ("Which of the following elements is a tuple?",
              ["a=[0,2]", "b={'name':'Gaga'}", "c=(8,5)", "d=(2)"],"3")
question4_1 = ("Which of the following is the correct way to create a comment in Python?",
              ["// This is a comment", "<!-- This is a comment -->", "/* This is a comment */",
               "# This is a comment"], "4")
question5_1 = ("What data type does the function input() return by default?",
              ["str", "int", "float", "list"], "1")
questionnaire_level_one = [question1_1, question2_1, question3_1, question4_1, question5_1]

# level two questionnaire implementation
question1_2 = ("\nWhich of the following methods is used to add an element to a list?",
              ["append()", "add()", "push()", "insert()"], "1")
question2_2 = ("""What is the output of the following code?
    for i in range(3):
        print(i, end=" ")\n""",
              ["1 1 2", "0 2 3", "0 1 2 (on separate lines)", "Error"], "2")
question3_2 = ("What is the purpose of the 'break' statement in Python loops?",
              ["To pause the loop temporarily", "To skip the current iteration",
               "To repeat the loop", "To terminate the loop immediately"], "4")
question4_2 = ("What is the correct way to handle exceptions in Python?",
              ["try-except", "if-else", ".loop-control", "catch-finally"], "1")

