'''1. Write a function that accepts a positive integer as a parameter and then returns a
representation of that number in binary (base 2).
Hint: This is in many ways a trick question. Think! '''

def binary(n):
    if n <= 0:
        raise ValueError("Please enter positive number")
    return format(n, 'b')
print(binary(2))  


'''2. Write and test a function that takes an integer as its parameter and returns the
factors of that integer. (A factor is an integer which can be multiplied by another to
yield the original).'''

storage = []
def factor(number):
    for i in range(1, number + 1):
        if number % i == 0:  # Check if i is a factor of n
            storage.append(i) #Append the value in the list i.e in storage
    return storage 
print(factor(120))

'''3. Write and test a function that determines if a given integer is a prime number. A
prime number is an integer greater than 1 that cannot be produced by multiplying
two other integers. '''

def prime_number(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if (number % i) == 0:
            return False
        else:
            return True
print(prime_number(4))  


'''4. Computers are commonly used in encryption. A very simple form of encryption
(more accurately "obfuscation") would be to remove the spaces from a message
and reverse the resulting string. Write, and test, a function that takes a string
containing a message and "encrypts" it in this way. '''


def enc():
    message = input("Enter a message: ")
    enc_message = message.replace(" ", "")[::-1] # Remove spaces and reverse the string
    return enc_message
print(enc())
