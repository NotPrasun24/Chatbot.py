'''1. Last week you wrote a program that printed out a cheery greeting including your
name. Take a copy of it, and modify it so that the user enters their name at the
keyboard, and then receives a greeting. For example:
Hello, what is your name? Mr Apricot
Hello, Mr Apricot. Good to meet you! '''

name = input("Hello, what is your name? ")
print(f"Hello Mr {name}. Good to meet you! ")

'''2. Write a program that prompts a user to enter a temperature in Celsius, and then
displays the corresponding temperature in Fahrenheit, like so:
Enter a temperature in Celsius: 32.5
32.5C is equivalent to 90.5F. '''
                                                                                                
celsius = float(input("Enter a temperature in Celsius: "))
fahrenheit = celsius * (9 / 5) + 32
print(f"{celsius}C is equivalent to {fahrenheit}F") 

'''3. The Head of Computing at the University of Poppleton is tasked with dividing a
group of students into lab groups. A lab group is usually 24 students, but this is
sometimes varied to create groups of similar size. Write a program that prompts for
the number of students and group size, and then displays how many groups will be
needed and how many will be le over in a smaller group.
How many students? 113
Required group size? 22
There will be 5 groups with 3 students left over.
For bonus credit, see if you can fix the grammar in the output. So if there were 101
students in groups of 20 the output would be:
There will be 5 groups with 1 student left over. '''

students = int(input("How many students are there? "))
groups = int(input("What is your requied group size? "))
num_groups = students // groups
leftovers = students % groups 

if leftovers <=1:
    print(f"There will be {num_groups} group with {leftovers} student left over.")
else:
    print(f"There will be {num_groups} groups with {leftovers} students left over.")



'''4. A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
first count the sweets and then divide them according to how many pupils attend
that day. Write a program that will tell the teacher how many sweets to give to each
pupil, and how many she will have le over. '''

sweets = int(input("Enter how many sweets: "))
pupils = int(input("Enter how many pupils: "))
distrubutions = sweets//pupils
print(distrubutions)

