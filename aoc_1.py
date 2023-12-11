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

# Define a function that takes a string as a parameter - not used
def add_numbers(strings):
    # Use a regular expression to find all numbers in the string
    numbers = re.findall(r'\d+', strings)
    
    # Check if there are any numbers in the list
    if numbers:
        # Convert the numbers to integers
        numbers = [int(number) for number in numbers]
        # Add the first and last numbers in the list
        result = numbers[0] + numbers[-1]
        print(f"The sum of the first number {numbers[0]} and last number {numbers[-1]} in the string is: {result}")
        # Return the result
        return result
    else:
        # If no numbers are found, return 0 or handle it as appropriate for your case
        print("No numbers found in the string.")
        return 0
    
# Define a function combining the first digit and the last digit (in that order) to form a single two-digit number
def combine_first_and_last_digit(strings):
    # Use a regular expression to find all numbers in the string
    numbers = re.findall(r'\d', strings)
    
    # Check if there are any numbers in the list
    if numbers:
        # Convert the numbers to integers
        numbers = [int(number) for number in numbers]
        # Combine the first and last digits in the list
        result = numbers[0] * 10 + numbers[-1]
        print(f"The combined first number {numbers[0]} and last number {numbers[-1]} in the string is: {result}")
        # Return the result
        return result
    else:
        # If no numbers are found, return 0 or handle it as appropriate for your case
        print("No numbers found in the string.")
        return 0
    
    # Define a function that takes a string as a parameter

# Define a function that takes a list of strings as a parameter
def add_numbers_list(strings):  
    # Initialize a variable to store the sum
    sum = 0
    # Loop through each string in the list
    for string in strings:
        # Call the combine_first_and_last_digit function on the string and add the result to the sum
        sum += combine_first_and_last_digit(string)
    # Return the sum
    return sum

# Define a function to open a file and read its contents which contains the list of strings to be SUM'd
def open_file(filename):
    # Open the file for reading
    with open(filename, 'r') as file:
        # Read the contents of the file
        contents = file.read()
    # Return the contents
    return contents

# Define a function to create a list of string from sample data for development and testing purposes
def create_strings_list():
    # Create a list of strings
    strings_list = [
        's5sevenxrdfr4mhpstgbjcfqckronesix',
        'nkzjrdqrmpztpqninetwofour1znnkd',
        '3four4',
        'sfdrtpvspsixsn5zbqmggb8vgkjseight',
        '72666gxzflnsfqmndjdscvqmcqls5'
    ]
    # Return the list of strings
    return strings_list

# main block

#answer = 0
# create a list of strings from sample data for development and testing purposes
strings = create_strings_list()
# print the list of strings (DEBUG when needed)
# print(strings) 
# print the sum of the numbers in each string in the list
answer = add_numbers_list(strings)

# print "The sum of the first number and last number for each string in the list equals: + result"
print(f"The sum of all the summed numbers in the strings list equals: {answer}")
print("----")


