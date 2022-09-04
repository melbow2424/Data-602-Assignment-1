#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

high_score = 95 # change variable to match the one in function 
 
# Get the test scores.
test1 = input('Enter the score for test 1: ')
test2 = input('Enter the score for test 2: ')
test3 = input('Enter the score for test 3: ')   # Needed to add 3rd test
# Calculate the average test score.

average = (int(test1) + int(test2) + int(test3)) / 3 # Int() was added to convert string input to interger. Also () around the 3 test for average to compute correctly (PEMDAS)



# Print the average.
print('The average score is', average)
# If the average is a high score,
# congratulate the user.
if average >= high_score:
    print('Congratulations!')
    print('That is a great average!') # Needs to be indented under the if statement 

#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 

print('Enter length and width of first rectangle. ')
length1 = input('length: ')
width1 = input('width: ')

print('Enter length and width of second  rectangle. ')
length2 = input('length: ')
width2 = input('width: ')

area1 = int(length1) * int(width1)
area2 = int(length2) * int(width2)

print('The area of the first rectangle is ' + str(area1)+ '\n')
print('The area of the second rectangle is ' + str(area2)+ '\n')


#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.

first_name = input('Enter your first name: ')
age = input('Enter your age: ')

first_name_str = str(first_name)
age_int = int(age)


print(type(first_name_str))
print(type(age_int))



#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"

#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.

first_name = input('Enter your first name: ')
age = input('Enter your age: ')

first_name_str = str(first_name)
age_int = int(age)


#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"

print("Happy birthday, " + first_name_str + " ! You are " + str(age) + " years old today!")
