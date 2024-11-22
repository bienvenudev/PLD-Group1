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
question5_2 = ("""What will be the output of the following code?
    my_dict = {"a": 1, "b": 2}
    print(my_dict.get("c", 'Not Found'))\n""",
              ["None", "0", "Error", "Not Found"], "4")
questionnaire_level_two = [question1_2, question2_2, question3_2, question4_2, question5_2]

# level three questionnaire implementation
question1_3 = ("\nWhich of the following is a correct syntax for defining a Python class?",
              ["define MyClass:", "def MyClass:", "class MyClass[]:", "class MyClass:"], "4")
question2_3 = ("What is the purpose of the @staticmethod decorator?",
              ["To define a method that doesn’t require a class instance",
               "To define a method that operates on the class itself",
               "To define a private method", "To define an asynchronous method"], "1")
question3_3 = ("What does the 'with' statement in Python help manage?",
              ["Loops", "file handling", "Memory allocation", "Multi-threading"], "2")
question4_3 = ("""What will be the output of this code?
def func(a, b, c=3):
    return a + b + c
print(func(2, 3))\n""", ["6", "Error", "5", "8"], "4")
question5_3 = ("Which of the following correctly describes the @property decorator in Python?",
              ["To make a method private to the class",
               "To create a method that is only callable by the class itself",
               "To define a method that acts as a getter for an attribute",
               "To automatically synchronize threads accessing a method"], "3")
questionnaire_level_three = [question1_3, question2_3, question3_3, question4_3, question5_3]

# Calling functions to start the assessment
display_welcome_screen()
level = select_difficulty()

questionnaire = []  # The list containing questionnaire of the selected level
if level == 1:
    questionnaire = questionnaire_level_one
elif level == 2:
    questionnaire = questionnaire_level_two
elif level == 3:
    questionnaire = questionnaire_level_three

score = start_questionnaire(questionnaire)
print(f"You have {score}/5")
