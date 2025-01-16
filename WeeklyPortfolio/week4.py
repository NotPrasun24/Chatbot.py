'''1. Functions are often used to validate input. Write a function that accepts a single
integer as a parameter and returns True if the integer is in the range 0 to 100
(inclusive), or False otherwise. Write a short program to test the function.'''

def check(n):
    if n >= 0 and n <= 100: # If the number is between 0 and 100 (inclusive), return True
        return True
    else: # If not return false
        return False
print(check(0))


'''2. Write a function that has a single string as its parameter, and returns the number of
uppercase letters, and the number of lowercase letters in the string. Test the
function with a short program.'''


def check_string(n): 
    uppercase = sum(1 for a in n if a.isupper()) # Count the uppercase letters in the string using a generator expression
    lowercase = sum(1 for a in n if a.islower()) # This counts lowercase letters
    return uppercase, lowercase # Returns count of uppercase and lowercase letters
uppercase,lowercase = check_string("PrAsUn SeDAi")
print(f"The uppercase letters is: {uppercase}")
print(f"The lowercase letter is: {lowercase}")


'''3. Modify your "greetings" program so that the first letter of the name entered is
always in uppercase with the rest in lowercase. This should happen even if the user
entered their name dierently. So if the user entered arthur, ARTHUR, or even
arTHur the name should be displayed as Arthur.'''


def capital(name): # Define a function to capitalize the first letter of the name
    return name.capitalize()
name = input("Enter your name: ")
if name == "": # Check if the user has entered a their name or not
    print("Hello, Stranger!") # IF not it will print stranger
else:
    print(f"Hello, {capital(name)}. Good to meet you.") #covert user first letter of input name to capitalize form


'''4. When processing data it is often useful to remove the last character from some
input (it is often a newline). Write and test a function that takes a string parameter
and returns it with the last character removed. (If the string contains one or fewer
characters, return it unchanged.)'''

def remove_last_character(word): # function to remove last letter of user input
    if len(word) <= 1: # check if user inputs only one letter
        return word # If one letter is writeen than it will not remove letter instead disply the original texrt
    else:
        return word[:-1]
print(remove_last_character("Prasun"))


'''5. Write and test a function that converts a temperature measured in degrees
centigrade into the equivalent in fahrenheit, and another that does the reverse
conversion. Test both functions. (Google will find you the formulae).'''


def celcius_to_fahrenheit(celcius):
    return ((celcius * 9/5) + 32) # Use the formula (Celsius * 9/5) + 32 to convert to Fahrenheit
# Use the formula (Celsius * 9/5) + 32 to convert to Fahrenheit
def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit - 32) * 5/9 # Use the formula (Celsius * 9/5) + 32 to convert to Fahrenheit

print(f"{celcius_to_fahrenheit(0)}F")
print(f"{fahrenheit_to_celcius(32)}C")



'''6. Write a program that takes a centigrade temperature and displays the equivalent in
fahrenheit. The input should be a number followed by a letter C. The output should
be in the same format.'''

def celcius_to_fahrenheit(celcius):
    celcius = float(celcius[ :-1]) # Remove the last character ('C') and convert the remaining part to a float
 # Convert the Celsius temperature to Fahrenheit using the formula (Celsius * 9/5) + 32
    return ((celcius * 9/5) + 32)
def user_input(): # Define a function to get user input for the temperature

    # Return the input in uppercase to handle cases like "32c" or "32C"
    user_input = input("Enter temperature in celcius followed by C (example 32C): ").upper()
    return user_input

def test():
    user = user_input() # Call the user_input function to get the input from the user
    # Call the celcius_to_fahrenheit function to convert the Celsius input to Fahrenheit
    fahrenheit_tempreture = celcius_to_fahrenheit(user)
    print(f"{user} is equal to {fahrenheit_tempreture}F")

test()



'''7. Write a program that reads 6 temperatures (in the same format as before), and
displays the maximum, minimum, and mean of the values.
Hint: You should know there are built-in functions for max and min. If you hunt, you
might also find one for the mean.'''


# Importing the 'mean' function from the statistics module and renaming it as 'prasun'
from statistics import mean as prasun

# Define a function to convert Celsius to Fahrenheit
def celcius_to_fahrenheit(celcius):
    celcius = float(celcius[ :-1]) 
    return ((celcius * 9/5) + 32)

# Define a function to get user input for the temperatures
def user_input():
    # Initialize an empty list to store the user's Celsius temperature inputs
    temp_celcius = []
    for i in range(6): # Loop to take 6 inputs from the user
        user_input = input(f"Enter your {i+1} temperature in celcius followed by C (example 32C): ").upper()
        temp_celcius.append(user_input)  # Append the input to the temp_celcius list
    return temp_celcius # Return the list of temperatures in Celsius

def test():
    temp_fer = [] # Initialize an empty list for storage store 
    user = user_input()
    for temp in user:
        fer = celcius_to_fahrenheit(temp)
        temp_fer.append(fer)
    
    # Loop through both the Celsius and Fahrenheit lists and print each pair
    for C,F in zip(user,temp_fer):
        print(f"{C} is equal to {F}F")  

    print("\n")
    print(f"Maximum temperature is {max(temp_fer)}F")
    print(f"Minimum temperature is {min(temp_fer)}F")
    print(f"Mean temperature is {prasun(temp_fer)}F")
test()


'''8. Modify the previous program so that it can process any number of values. The input
terminates when the user just pressed "Enter" at the prompt rather than entering a
value.'''

from statistics import mean 

def celcius_to_fahrenheit(celcius):
    celcius = float(celcius[ :-1])
    return ((celcius * 9/5) + 32)

def user_input():
    temp_celcius = []
    while True:
        user_input = input("Enter your temperature in celcius followed by C (example 32C), press 'q' to exit: ").upper()
        if user_input == 'Q':
            print("You did not enter any number for conversion! ")
            break
        temp_celcius.append(user_input)
    return temp_celcius

def test():
    temp_fer = []
    user = user_input()
    for temp in user:
        fer = celcius_to_fahrenheit(temp)
        temp_fer.append(fer)
    for C,F in zip(user,temp_fer):
        print(f"{C} is equal to {F}F")  

    print("\n")
    print(f"Maximum temperature is {max(temp_fer)}F")
    print(f"Minimum temperature is {min(temp_fer)}F")
    print(f"Mean temperature is {mean(temp_fer)}F")

test()