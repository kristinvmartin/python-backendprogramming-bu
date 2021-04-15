"""
Kristin Martin
CS 521
March 10, 2019
Term Project Submission

This file contains the input validation methods used in BeginSunday.py (the
main program file), and Child.py, the class constructor.
"""

class ValidationError(Exception):
    """Raised when input is not entered as expected, programmer should
    add print statement to user clarifying error."""
    pass

class Validation:
    """validation methods used for user input in program"""
    def validate_alpha(given_input):
        valid_input = False
        while not valid_input:
            try:
                expected_input = str(input(given_input))
                if expected_input.isalpha() is False:
                    raise ValidationError
                valid_input = True
                return expected_input
            except ValidationError:
                print("Only alphabetic input was expected. Try again.")
    
    def validate_age(given_input):
        valid_input = False
        while not valid_input:
            try:
                expected_input = int(input(given_input))
                if expected_input < 0 or expected_input > 18:
                    raise ValidationError
                valid_input = True
                return expected_input
            except ValidationError:
                print("Only an integer between 0 and 18 should be entered for age.")
            except ValueError:
                print("Your input was not numeric. Try again.")
    
    def validate_phone(given_input):
        valid_input = False
        while not valid_input:
            try:
                expected_input = str(input(given_input))
                if len(expected_input) != 10:
                    raise ValidationError
                valid_input = True
                return expected_input
            except ValidationError:
                print("Only enter 10 numbers. No dashes, spaces, parentheses, etc.")
            except ValueError:
                print("Your input was not numeric. Try again.")
