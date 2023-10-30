#Homework1
if __name__ == '__main__':
    s = input()


print(any(c.isalnum() for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))

#Homework2
# Read the two integers as input
start_year = int(input())
end_year = int(input())

# Use the range function to create a range of numbers
# Note that the range will start with the first input and end with the second input, excluding the end year
year_range = list(range(start_year, end_year))

# Print the list
print(year_range)
