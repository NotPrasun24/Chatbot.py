'''1. Modify your greeting program so that if the user does not enter a name (i.e. they
 just press enter), the program responds "Hello, Stranger!". Otherwise it should print
 a greeting with their name as before.'''

name = input("Enter your name: ") #ask for user name
if name == "": #checks if user has entred their name or not
    print("Hello, Stranger!") #if user didnot type anything it prints hello stranger
else:
    print("Hello, "+ name + " nice to meet you") #It will greet the user 

'''2. Write a program that simulates the way in which a user might choose a password.
 The program should prompt for a new password, and then prompt again. If the two
 passwords entered are the same the program should say "Password Set" or
 similar, otherwise it should report an error.'''

password = input("Set your password: ") #Ask user to set their password
print("Password has been saved! ")
guess = input("Enter your password: ")
if guess == password: #checks if user has enter the same password or not
    print("Access granted!")
else:
    print("Access denied!")

'''3. Modify your previous program so that the password must be between 8 and 12
characters (inclusive) long.'''

while True: #Infinite loop until the password is set
    password = input("Set your password between 8-12 letters: ")
    if len(password) >= 8 and len(password) <= 12:# Check if the password length is between 8 and 12 characters
        guess = input("Enter your password: ")
        if guess == password: #confirm the password has been set
            print("Password Set!")
        else:
            print("password doest match ")
        
    else:
        print("Password must be between 8-12 letters")  #inform user that they have not enter 8 or more letter of password


'''4. Modify your program again so that the chosen password cannot be one of a list of
common passwords, defined thus:
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']'''

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber'] #list of bad password
password = input("Set your password between 8-12 letters: ")
if len(password) >= 8 and len(password) <= 12 and password not in BAD_PASSWORDS: #checks the length of password and if it has bad password or not
    guess = input("ReEnter your password: ")
    if guess == password : 
        print("Password Set!")
    else:
        print("password doest match ")
elif password in BAD_PASSWORDS: #it will let the user know if user input bad password
    print("Your password is too week, Try again")
else:
    print("Password must be between 8-12 letters")


'''5. Modify your program a final time so that it executes until the user successfully
chooses a password. That is, if the password chosen fails any of the checks, the
program should return to asking for the password the first time.'''

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']  #list of bad password

# Infinite loop to repeatedly ask the user to set a valid password
while True:  
    password = input("Set your password between 8-12 letters: ")
    if len(password) >= 8 and len(password) <= 12 and password not in BAD_PASSWORDS: #checks the length of password and if it has bad password or not
        guess = input("ReEnter your password: ")
        if guess == password :
            print("Password Set!")
            break
        else:
            print("password doest match ")

    # If the password is a common/weak password, inform the user
    elif password in BAD_PASSWORDS:
        print("Common password, Try again")
    else:
        print("Password must be between 8-12 letters")


'''6. Write a program that displays the "Seven Times Table". That is, the result of
multiplying 7 by every number from 0 to 12 inclusive. The output might start:
0 x 7 = 0
1 x 7 = 7
2 x 7 = 14
and so on.'''

a = 0 
while a <= 12:
    print(f"{a} x 7 = {a * 7}")
    a += 1


'''7. Modify your "Times Table" program so that the user enters the number of the table
they require. This number should be between 0 and 12 inclusive.'''

a = 0
user_number = int(input("Enter your number: "))
while True:
    if 0 <= user_number <= 12:
        while a <= 12:
            print(f"{a} x {user_number} = {a * user_number}")
            a += 1
    else:
        print("ERROR!, Please enter a number between 1 to 12 only")
        break
       


'''8. Modify the "Times Table" again so that the user still enters the number of the table,
but if this number is negative the table is printed backwards. So entering "-7"
would produce the Seven Times Table starting at "12 times" down to "0 times". '''

b = 12
a = 0
while True:
    user_number = int(input("Enter your number: "))
    if 0 <= user_number <= 12:
        while a <= 12:
            print(f"{a} x {user_number} = {a * user_number}")
            a += 1
        break
    elif user_number < 0:
        while b >= 0:
            print(f"{b} x {user_number} = {b * user_number}")
            b -= 1
        break
    else:
        print("ERROR!, Please enter a number less than 12")

