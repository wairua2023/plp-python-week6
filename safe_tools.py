def safe_divide(a, b):

    try:
        return a / b
        # Return a divided by b
    except ZeroDivisionError:
        # Return the text "Cannot divide by zero"
        return "Cannot divide by zero"


def safe_number(text):
    try:
        return int(text)
        # Return text converted with int()
    except ValueError:
    # Return text "Not a number"
        return "Not a number"



def get_field(learner, key):

    try:
        return learner[key]
        # Return the value at that key
    except KeyError:
        # Return the text "Field not found"
        return "Field not found"



print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_number("42"))
print(safe_number("abc"))

learner = {"name": "Amina", "score": 82}
print(get_field(learner, "score"))
print(get_field(learner, "email"))