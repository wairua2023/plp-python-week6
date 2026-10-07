Error handling and debugging assignment

This assignment demonstrates how Python's try/except can handle common runtime errors.

safe_divide.py — Safely divides two numbers and handles division by zero.

safe_number.py — Converts text to an integer and handles invalid numbers.

get_field.py — Gets a value from a dictionary and handles missing keys.

Why can't the if check catch abc on its own?

An if check can test conditions, but int("abc") raises a ValueError while Python is trying to perform the conversion. The try/except block is needed to catch that error and handle it safely.