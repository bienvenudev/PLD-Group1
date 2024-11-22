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
        except ValueError:
            print("ERROR!! The input must be a number")


def display_questionnaire(question):
    """Displaying the questionnaire and check the answer"""
    print(question[0])
    for i in range(len(question[1])):
        print(f"  {i+1}- {question[1][i]}")

    while True:
        answer = input("Enter your answer (1/2/3/4): ")
        try:
            answer_index = int(answer)
            if 1 <= answer_index <= len(question[1]):
                break
            else:
                print(f"Please enter a number between 1 and {
                      len(question[1])}")
        except ValueError:
            print("Please enter a valid number")

    if answer == question[2]:
        print(f"✓ Correct answer! {question[3]}\n")
        return True
    else:
        print(f"✗ Incorrect! The correct answer is '{
              question[2]}'. {question[3]}\n")
        return False


def start_questionnaire(questionnaire):
    marks = 0
    for question in questionnaire:
        if display_questionnaire(question):
            marks += 1
    return marks


# Level 1 Questionnaire (Expanded to 10 questions)
questionnaire_level_one = [
    ["\nWhat is the correct file extension for Python files?",
     [".pt", ".pyt", ".py", ".python"], "3", "'.py' is the standard file extension for Python source code files."],
    ["Which Python function displays a message on the screen?",
     ["input()", "print()", "printf()", "show()"], "2", "print() is the built-in Python function used to output text to the console."],
    ["Which of the following elements is a tuple?",
     ["a=[0,2]", "b={'name':'Gaga'}", "c=(8,5)", "d=(2)"], "3", "c=(8,5) is a tuple, defined with parentheses and containing multiple elements."],
    ["What is the correct way to create a comment in Python?",
     ["// This is a comment", "<!-- This is a comment -->", "/* This is a comment */", "# This is a comment"], "4", "# is used for single-line comments in Python."],
    ["What data type does the input() function return by default?",
     ["str", "int", "float", "list"], "1", "input() always returns a string, which can be converted to other types if needed."],
    ["What is the result of 3 * 2 in Python?",
     ["6", "32", "5", "15"], "1", "3 * 2 performs simple multiplication, resulting in 6."],
    ["Which of these is a valid variable name in Python?",
     ["2variable", "my-var", "my_variable", "variable@name"], "3", "my_variable is valid as it starts with a letter and uses an underscore, following Python naming conventions."],
    ["What does len() function do?",
     ["Adds items", "Multiplies numbers", "Returns the length of an object", "Converts to lowercase"], "3", "len() returns the number of items in an object like lists, strings, or dictionaries."],
    ["How do you start a function in Python?",
     ["function myFunction()", "define myFunction()", "def myFunction():", "start myFunction():"], "3", "def is used to define a function in Python, followed by the function name and a colon."],
    ["Which of these is NOT a Python data type?",
     ["list", "tuple", "dictionary", "array"], "4", "array is not a built-in Python data type; it requires importing the array module."]
]

# Level 2 Questionnaire (Expanded to 10 questions)
questionnaire_level_two = [
    ["Which method adds an element to a list?",
     ["append()", "add()", "push()", "insert()"], "1", "append() adds an element to the end of a list."],
    ["What is the output of range(3)?",
     ["[0, 1, 2]", "[1, 2, 3]", "0 1 2", "Error"], "1", "range(3) generates a sequence of numbers from 0 to 2."],
    ["What is the purpose of the 'break' statement?",
     ["To pause the loop", "To skip an iteration", "To stop the loop", "To continue the loop"], "3", "break immediately exits the current loop."],
    ["How do you handle exceptions in Python?",
     ["try-except", "if-else", "loop-control", "catch-finally"], "1", "try-except is used to catch and handle potential exceptions in code."],
    ["What does dict.get() do?",
     ["Adds a key", "Retrieves a value", "Removes a key", "Counts items"], "2", "dict.get() retrieves the value for a given key, with an optional default value."],
    ["How do you remove the last item from a list?",
     ["remove()", "delete()", "pop()", "erase()"], "3", "pop() removes and returns the last item from a list."],
    ["What does 'continue' do in a loop?",
     ["Stops the loop", "Skips current iteration", "Repeats the loop", "Exits the function"], "2", "continue skips the rest of the current iteration and moves to the next."],
    ["How do you convert a string to an integer?",
     ["str()", "int()", "float()", "convert()"], "2", "int() converts a string to an integer."],
    ["What is list comprehension used for?",
     ["Creating new lists", "Sorting lists", "Deleting lists", "Counting list items"], "1", "List comprehension creates new lists based on existing lists with a compact syntax."],
    ["What does 'global' keyword do?",
     ["Creates a global variable", "Imports all variables", "Stops global access", "Defines a function"], "1", "global allows modifying a global variable within a function's local scope."]
]

# Level 3 Questionnaire (More Complex Questions)
questionnaire_level_three = [
    ["What is a decorator in Python?",
     ["A design pattern", "A function that modifies another function", "A class method", "A way to print"], "2", "A decorator is a function that takes another function and extends its behavior without explicitly modifying it."],
    ["What does the @staticmethod decorator do?",
     ["Creates an instance method", "Defines a method without self parameter", "Makes a method private", "Adds a method to a class"], "2", "A static method doesn't require a class instance (self) and can be called directly on the class."],
    ["How do you create a generator in Python?",
     ["Using class", "Using def with yield", "Using lambda", "Using return"], "2", "def with yield creates a generator function that returns an iterator."],
    ["What is lambda used for?",
     ["Creating complex functions", "Creating small anonymous functions", "Defining classes", "Importing modules"], "2", "Lambda creates small, one-line anonymous functions without a formal def statement."],
    ["What is method overriding in OOP?",
     ["Defining multiple methods with same name", "Changing a method in child class", "Creating new methods", "Deleting methods"], "2", "Method overriding allows a child class to provide a different implementation of a method defined in its parent class."],
    ["What does *args do in a function definition?",
     ["Limits function arguments", "Allows variable number of arguments", "Creates a tuple", "Stops function execution"], "2", "*args allows a function to accept any number of positional arguments."],
    ["What is the purpose of __init__ method?",
     ["To delete an object", "To initialize object attributes", "To stop object creation", "To copy an object"], "2", "__init__ is a constructor method that initializes object attributes when an object is created."],
    ["What is polymorphism?",
     ["One method with different implementations", "Creating many variables", "Stopping inheritance", "Adding methods"], "1", "Polymorphism allows different classes to implement the same method differently."],
    ["What does the 'is' keyword do?",
     ["Checks value equality", "Checks object identity", "Assigns values", "Compares lists"], "2", "'is' checks if two variables point to the exact same object in memory."],
    ["What is method overriding in OOP?",
     ["Defining multiple methods with same name", "Changing a method in child class", "Creating new methods", "Deleting methods"], "2", "Method overriding allows a child class to provide a different implementation of a method defined in its parent class."]
]


def main():
    # Main program execution
    display_welcome_screen()
    level = select_difficulty()

    # Select questionnaire based on difficulty
    questionnaire_map = {
        1: questionnaire_level_one,
        2: questionnaire_level_two,
        3: questionnaire_level_three
    }

    questionnaire = questionnaire_map.get(level, questionnaire_level_one)

    score = start_questionnaire(questionnaire)
    print(f"Your score: {score}/10")


if __name__ == "__main__":
    main()
