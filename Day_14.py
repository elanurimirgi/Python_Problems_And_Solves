#Homework1
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    # Split the full name into words
    words = s.split()

    # Capitalize the first letter of each word
    capitalized_words = [word.capitalize() for word in words]

    # Join the capitalized words back into a single string
    capitalized_full_name = " ".join(capitalized_words)
    
    return capitalized_full_name  # Sonucu döndur


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


#Homework2
# Get the input string
input_string = input("Enter a string: ")

# Create a set to find unique characters
unique_characters = set(input_string)

# Convert the set elements into a sorted list to get the result in a list form
unique_characters_list = sorted(list(unique_characters))

# Print the result
print("Unique characters:", unique_characters_list)
