###################################


#thus reverse a string
def rev(s): return s[::-1]

# this asks a question and return the answer.takes whether new line or not
def get_answer(s, newline):
    if newline:
        print(s)
        return (input())
    else:
        return(input(s))


# this asks a question and return the answer (ask in new line)
def get_answers(s): return (get_answer(s, True))


# function to check if a string is an int or not
def is_number(s): 
    try:
        int(s)
        return True
    except ValueError:
        return False


###################################
