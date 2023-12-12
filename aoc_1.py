# Day 1 of Advent of Coding Challenge
# Add the first and last numbers contained in some random strings in a list and add each result from the list together
# Some examples strings:
        # 's5sevenxrdfr4mhpstgbjcfqckronesix',
        # 'nkzjrdqrmpztpqninetwofour1znnkd',
        # '3four4',
        # 'sfdrtpvspsixsn5zbqmggb8vgkjseight',
        # '72666gxzflnsfqmndjdscvqmcqls5'

# Import Python modules to work with strings and lists and regular expressions
import re
import string

# Define a function that takes a string as a parameter and returns the combined first and last digit of the string
def combine_first_and_last_numbers(input_string):
    # Find all numbers in the string using regular expression
    numbers = [int(num) for num in re.findall(r'\d', input_string)]

    if numbers:
        # Combine the first and last numbers
        combined_result = str(numbers[0]) + str(numbers[-1])
        return int(combined_result)
    else:
        # If no numbers are found, return 0 or handle it as appropriate for your case
        return 0


# Define a function that takes a list of strings as a parameter
def add_numbers_list(strings_list):  
    # Initialize a variable to store the sum
    total_sum = 0
    # Loop through each string in the list
    for string in strings_list:
        # Call the combine_first_and_last_digit function on the string
        # and add the sum of the results to the total_sum
        #total_sum += sum(combine_first_and_last_numbers(string))
        print(f"The input string is: {string}")
        print(f"Combined first number and last number:{combine_first_and_last_numbers(string)}")
        # Change the string to integer so that the total_sum can be calculated
        
        total_sum += combine_first_and_last_numbers(string)
    
    # Return the total_sum
    return total_sum

# Define a function to open a file and read its contents which contains the list of strings to be SUM'd
def open_file(filename):
    # Open the file for reading
    with open(filename, 'r') as file:
        # Read the contents of the file
        contents = file.read()
    # Return the contents
    print(f"The contents of the file are: {contents}")
    return contents

# Define a function to create a list of string from sample data for development and testing purposes
def create_strings_list():
    # Manually Create a list of strings - DEBUG CODE
    strings_list = [
        's5sevenxrdfr4mhpstgbjcfqckronesix',
        'nkzjrdqrmpztpqninetwofour1znnkd',
        '3four4',
        'test123this456string',
        'sfdrtpvspsixsn5zbqmggb8vgkjseight',
        '72666gxzflnsfqmndjdscvqmcqls5'
    ]
    # Return the list of strings

    return strings_list

# main block

#answer = 0
# create a list of strings from sample data for development and testing purposes
strings_list = create_strings_list()

# use input file instead of sample data for development and testing purposes
# stringsfromfile = open_file('day1-inputs.txt')
# strings = open_file('day1-inputs.txt')

# print the list of strings (DEBUG when needed)
# print(strings) 
# print the sum of the numbers in each string in the list
answer = add_numbers_list(strings_list)

# print "The sum of the first number and last number for each string in the list equals: + result"
print(f"The sum of all the summed numbers in the strings list equals: {answer}")
print("----")


