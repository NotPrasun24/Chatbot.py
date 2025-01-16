'''1. Write and test a function that takes a string as a parameter and returns a sorted list
of all the unique letters used in the string. So, if the string is cheese, the list
returned should be ['c', 'e', 'h', 's'].'''

def single_string(word):
    return sorted(set(word)) #sorted() returns a new list containing the elements of the set in ascending order.

user_input = input("Enter your word: ")
print(single_string(user_input))


'''2. Write and test three functions that each take two words (strings) as parameters and
return sorted lists (as defined above) representing respectively:
Letters that appear in at least one of the two words.
Letters that appear in both words.
Letters that appear in either word, but not in both.
Hint: These could all be done programmatically, but consider carefully what topic we
have been discussing this week! Each function can be exactly one line.'''

def atleast_one(first,second):
    print("\n1.Letters that appear in at least one of the two words.")
    return sorted(set(first) | set(second)) #removes any duplicate elements from each input and | is union operator for sets

def both(first,second):
    print("2.Letters that appear in both words.")
    return sorted(set(first) & set(second)) # & is AND operator it only takes similar letters from each word

def either_word(first,second):
    print("3.Letters that appear in either word, but not in both.")
    return sorted(set(first) ^ set(second)) # ^ is XOR operator and it takes all value except for similar onces

first = input("Enter your first word: ")
second = input("Enter your second word: ")
print(atleast_one(first,second))
print(both(first,second))
print(either_word(first,second))

'''3. Write a program that manages a list of countries and their capital cities. It should
prompt the user to enter the name of a country. If the program already "knows"
the name of the capital city, it should display it. Otherwise it should ask the user to
enter it. This should carry on until the user terminates the program (how this
happens is up to you).
Note: A good solution to this task will be able to cope with the country being entered
variously as, for example, "Wales", "wales", "WALES" and so on.'''

storage_of_capital_cities = {} #for storing all the cites with its key
while True:
    user_input = input("Enter your country:(bye to exit the program) ")
    if user_input == "bye": 
        break # exit the program 
    if user_input in storage_of_capital_cities: #check if the city for the given country is available or not
        print(f"The capital of {user_input} is {storage_of_capital_cities[user_input]}")
    else:
        user_capital = input(f"What is the capital of {user_input}? ") 
        storage_of_capital_cities[user_input] = user_capital #Store all the key and its value
        

'''4. One approach to analysing some encrypted data where a substitution is suspected
is frequency analysis. A count of the dierent symbols in the message can be used
to identify the language used, and sometimes some of the letters. In English, the
most common letter is "e", and so the symbol representing "e" should appear most
in the encrypted text.
Write a program that processes a string representing a message and reports the six
most common letters, along with the number of times they appear. Case should
not matter, so "E" and "e" are considered the same.
Hint: There are many ways to do this. It is obviously a dictionary, but we will want
zero counts, so some initialisation is needed. Also, sorting dictionaries is tricky, so
best to ignore that initially, and then check the usual resources for the runes.
'''

from collections import Counter

def encrypted_data():
    while True:
        message = input("Enter your encrypted message: ").lower()
        if message:
            # Use filter to exclude non-alphabetic characters and count the occurrences of each letter
            count = Counter(filter(str.isalpha, message))
            return count.most_common(6) # Return the six most common letters and their counts

        else:
            print("Please enter a valid message.")

def common_letters(common_letters):
    print("The six most common letters are")
    for letter, count in common_letters:
        print(f"{letter}: {count}")

six_common_letters = encrypted_data() #Call the encrypted_data function to get the six most common letters
common_letters(six_common_letters)