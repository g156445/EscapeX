# handwritten 9001 question

import random

def ask_question() -> bool:
    file_path = 'question.txt'
    with open(file_path, 'r') as f:
        lines = []
        for line in f:
            # Remove spaces and line breaks before and after each line
            stripped_line = line.strip()
            if stripped_line:  # if no empty, True
                lines.append(stripped_line)

    # random choice one line
    question_line = random.choice(lines)

    # question and answer
    user_input = input(f" {question_line}\nPlease Answer：").strip()
    if question_line == "(T/F)A class acts as a blueprint for defining objects？" and user_input.lower() == 't':
        return True
    elif question_line == "(T/F)The number of instance attributes in a class has to always be equal to the number of parameters of the __init__ method excluding self?" and user_input.lower() == 'f':
        return True
    elif question_line == "(T/F)A function can have no parameters?" and user_input.lower() == 't':
        return True
    elif question_line == "(T/F)You can have a variable with the same name inside and outside a function?" and user_input.lower() == 't':
        return True
    elif question_line == "(T/F)Printing inside a function is considered a side effect?" and user_input.lower() == 't':
        return True
    elif question_line == "(T/F)Lists can be initialised using either square brackets [] or round brackets () ?" and user_input.lower() == 'f':
        return True
    elif question_line == "(T/F)Lists can contain elements of different types?" and user_input.lower() == 't':
        return True
    elif question_line == "(T/F)Python lists and arrays are the same?" and user_input.lower() == 'f':
        return True
    elif question_line == "Which method is used to remove an element by value from a list in Python? pop()? remove()? delete()? discard()?" and user_input.lower() == 'remove()':
        return True
    elif question_line == "What stores the command line arguments? args? sys.argv? sys.args? sys.list?" and user_input.lower() == 'sys.argv':
        return True
    elif question_line == "(T/F)A tuple is the same as list except it is mutable?" and user_input.lower() == 'f':
        return True
    else:
        return False
